"""Provides information about installed packages and their status."""


from datetime import datetime as dt
import logging
import msgspec
import os
from pathlib import Path
import platform
import subprocess
import sys

from .reporter import Reporter


logger = logging.getLogger("wheel_getter")


class PackageSource(msgspec.Struct):
    registry: str | None = None
    editable: str | None = None
    virtual: str | None = None
    
    def resolve_editable(self, base_dir: Path) -> Path | None:
        """Converts location of editable installation to Path object and resolves it."""
        if self.editable is None:
            return None
        else:
            return (base_dir / self.editable).resolve()


class PackageSdist(msgspec.Struct):
    url: str
    hash: str  # format: "sha256:<hash>"
    size: int
    upload_time: dt | None = None  # format: "2024-11-30T04:30:14.439Z"


class PackageWheel(msgspec.Struct):
    url: str | None = None
    hash: str = ""  # format: "sha256:<hash>"
    size: int = 0
    path: str = ""
    upload_time: dt | None = None  # format: "2024-11-30T04:30:14.439Z"


class PackageInfo(msgspec.Struct):
    name: str
    version: str
    source: PackageSource
    wheels: list[PackageWheel] = []
    sdist: PackageSdist | None = None


class UvLockfile(msgspec.Struct):
    version: int
    revision: int
    package: list[PackageInfo]


class PackageListItem(msgspec.Struct):
    """Information about an installed module provided by `uv pip list`"""
    name: str
    version: str
    location: Path | None = None
    info: PackageInfo | None = None  # to be supplied from other sources


def get_installed_packages(
            lockfile_dir: Path,
            reporter: Reporter,
            ) -> list[PackageListItem]:
    """Returns a list of PackageListItem objects for installed packages."""
    try:
        r = subprocess.run(
                ["uv", "export", "--project", str(lockfile_dir)],
                capture_output=True,
                check=True,
                )
    except subprocess.CalledProcessError:
        reporter.error("could not list installed modules")
        raise ValueError("could not list installed modules")
    
    platform_info = dict(
            implementation_name=platform.python_implementation(),
            os_name=os.name,
            platform_machine=platform.machine(),
            platform_python_implementation=platform.python_implementation(),
            python_full_version=f"{sys.version_info.major}.{sys.version_info.minor}",
            sys_platform=sys.platform,
            # what else??
            )
    
    result: list[PackageListItem] = []
    here = Path.cwd()
    for line in r.stdout.decode().splitlines():
        if line.startswith(" "):
            continue
        elif line.startswith("-e"):
            option, path = line.split()
            base = here / path
            if (pyp_path := base / "pyproject.toml").exists():
                logger.debug("found editable installation at %s", base)
                pyp = msgspec.toml.decode(pyp_path.read_bytes())
                try:
                    name = pyp["project"]["name"]
                    version = pyp["project"]["version"]
                except KeyError:
                    reporter.error(
                            "project information not found in %s",
                            str(pyp_path),
                            )
                    continue
                pkg = PackageListItem(name=name, version=version)
        elif line.strip().startswith("#"):
            continue
        else:
            raw_spec = line.strip().rstrip("\\").strip()
            if ";" in raw_spec:
                ver_spec, cond = raw_spec.split(";", 1)
                if not eval(cond, None, platform_info):
                    continue
            else:
                ver_spec = raw_spec
            spec = ver_spec.split()[0]
            logger.debug("found dependency on %s", spec)
            if "==" not in spec:
                logger.error("unrecognized version spec “%s”", spec)
                continue
            name, version = spec.split("==")
            pkg = PackageListItem(name=name, version=version)
        result.append(pkg)
    
    return result


def get_lockfile_data(
            lockfile_dir: Path,
            reporter: Reporter,
            ) -> UvLockfile:
    """Reads a uv lockfile and returns important information."""
    lf_path = lockfile_dir / "uv.lock"
    lf_data = msgspec.toml.decode(lf_path.read_bytes(), type=UvLockfile)
    if lf_data.version > 1:
        reporter.warning("incompatible version %s of uv lockfile found")
        # try carrying on regardless
    
    return lf_data


def get_locklist(
            lockfile_dir: Path,
            reporter: Reporter,
            ) -> list[PackageListItem]:
    """Gets a list of extended information on installed packages."""
    lf_data = get_lockfile_data(lockfile_dir, reporter=reporter)
    
    pkg_dict = {pkg.name: pkg for pkg in lf_data.package}
    
    pkg_list = get_installed_packages(lockfile_dir, reporter=reporter)
    for pkg in pkg_list:
        pkg.info = pkg_dict.get(pkg.name)
        if pkg.info is None:
            reporter.warning("package %s not found in lockfile", pkg.name)
        # we shouldn't experience KeyError here as lockfile and list of
        # installed packages come from the same source – but it happens
    
    return pkg_list
