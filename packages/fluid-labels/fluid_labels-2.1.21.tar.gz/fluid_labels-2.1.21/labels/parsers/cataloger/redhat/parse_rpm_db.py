import logging
import struct
from pathlib import Path

from packageurl import PackageURL
from pydantic import ValidationError

from labels.model.ecosystem_data.redhat import RpmDBEntry
from labels.model.file import Location, LocationReadCloser
from labels.model.package import Language, Package, PackageType
from labels.model.relationship import Relationship
from labels.model.release import Environment, Release
from labels.model.resolver import Resolver
from labels.parsers.cataloger.redhat.rpmdb import open_db
from labels.parsers.cataloger.redhat.rpmdb.entry import header_import
from labels.parsers.cataloger.redhat.rpmdb.package import PackageInfo, get_nevra
from labels.parsers.cataloger.utils import get_enriched_location, log_malformed_package_warning

LOGGER = logging.getLogger(__name__)


def package_url(  # noqa: PLR0913
    *,
    name: str,
    arch: str | None,
    epoch: int | None,
    source_rpm: str,
    version: str,
    release: str,
    distro: Release | None,
) -> str:
    namespace = ""
    if distro:
        namespace = distro.id_
    qualifiers: dict[str, str] = {}
    if arch:
        qualifiers["arch"] = arch
    if epoch:
        qualifiers["epoch"] = str(epoch)
    if source_rpm:
        qualifiers["upstream"] = source_rpm

    return PackageURL(
        type="rpm",
        namespace=namespace,
        name=name,
        version=f"{version}-{release}",
        qualifiers=qualifiers,
        subpath="",
    ).to_string()


def to_int(value: int | None, default: int = 0) -> int:
    return int(value) if isinstance(value, int) else default


def to_el_version(epoch: int | None, version: str, release: str) -> str:
    if epoch:
        return f"{epoch}:{version}-{release}"
    return f"{version}-{release}"


def new_redhat_package(
    *, entry: PackageInfo, location: Location, env: Environment
) -> Package | None:
    name = entry.name
    version = entry.version

    if not name or not version:
        return None

    ecosystem_data = RpmDBEntry(
        name=name,
        version=version,
        epoch=entry.epoch,
        arch=entry.arch,
        release=entry.release,
        source_rpm=entry.source_rpm,
    )

    new_location = get_enriched_location(location)

    try:
        return Package(
            name=name,
            version=to_el_version(entry.epoch, version, entry.release),
            locations=[new_location],
            language=Language.UNKNOWN_LANGUAGE,
            licenses=[entry.license],
            type=PackageType.RpmPkg,
            ecosystem_data=ecosystem_data,
            p_url=package_url(
                name=name,
                arch=entry.arch,
                epoch=entry.epoch,
                source_rpm=entry.source_rpm,
                version=version,
                release=entry.release,
                distro=env.linux_release,
            ),
        )
    except ValidationError as ex:
        log_malformed_package_warning(new_location, ex)
        return None


def parse_rpm_db(
    _: Resolver,
    env: Environment,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    packages: list[Package] = []

    if not reader.location.coordinates:
        return packages, []

    database = open_db(reader.location.coordinates.real_path)

    if not database:
        return packages, []

    for entry in database.list_packages():
        package = new_redhat_package(entry=entry, env=env, location=reader.location)
        if package is not None:
            packages.append(package)
    return packages, []


def parse_rpm_file(
    _: Resolver,
    env: Environment,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    """Parse an individual .rpm file to extract package metadata.

    An RPM file structure:
    - Lead (96 bytes) - legacy header
    - Signature Header - signatures and checksums
    - Header - package metadata (what we need)
    - Payload - compressed files
    """
    packages: list[Package] = []

    if not reader.location.coordinates:
        return packages, []

    try:
        with Path(reader.location.coordinates.real_path).open("rb") as rpm_file:
            # Skip the lead (96 bytes)
            rpm_file.seek(96)

            # Read and skip the signature header
            # Magic number for header: 0x8eade801 (3 bytes) + 0x00 (1 byte)
            sig_magic = rpm_file.read(8)
            if len(sig_magic) < 8:
                return packages, []

            # Check for RPM header magic
            if sig_magic[:3] != b"\x8e\xad\xe8":
                return packages, []

            # Read signature header structure: il (4 bytes) + dl (4 bytes)
            sig_il = int.from_bytes(rpm_file.read(4), byteorder="big")
            sig_dl = int.from_bytes(rpm_file.read(4), byteorder="big")

            # Calculate signature section size
            # Each index entry is 16 bytes (tag + type + offset + count)
            sig_index_size = sig_il * 16
            sig_data_size = sig_dl

            # Skip signature index and data
            rpm_file.seek(sig_index_size + sig_data_size, 1)

            # Align to 8-byte boundary after signature
            current_pos = rpm_file.tell()
            alignment = (8 - (current_pos % 8)) % 8
            rpm_file.seek(alignment, 1)

            # Now we're at the main header
            # Read header magic
            header_magic = rpm_file.read(8)
            if len(header_magic) < 8 or header_magic[:3] != b"\x8e\xad\xe8":
                return packages, []

            # Read header structure: il (4 bytes) + dl (4 bytes)
            header_il = int.from_bytes(rpm_file.read(4), byteorder="big")
            header_dl = int.from_bytes(rpm_file.read(4), byteorder="big")

            # Calculate header data size (without magic bytes)
            # header_import expects: il (4) + dl (4) + index entries (il * 16) + data (dl)
            header_index_size = header_il * 16
            header_data_size = header_dl
            total_header_data = 8 + header_index_size + header_data_size  # il+dl + indexes + data

            # Go back to before il and dl to read complete header (without magic)
            rpm_file.seek(-8, 1)  # Go back 8 bytes (il + dl)
            header_data = rpm_file.read(total_header_data)

            if len(header_data) < total_header_data:
                return packages, []

            # header_import expects: il (4) + dl (4) + index entries + data
            index_entries = header_import(header_data)

            if index_entries:
                package_info = get_nevra(index_entries)
                package = new_redhat_package(
                    entry=package_info,
                    env=env,
                    location=reader.location,
                )
                if package:
                    packages.append(package)

    except (OSError, ValueError, struct.error) as ex:
        # Log error but return empty list instead of failing
        LOGGER.warning(
            "Failed to parse RPM file %s: %s",
            reader.location.coordinates.real_path,
            ex,
        )

    return packages, []
