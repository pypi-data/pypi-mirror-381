# Copyright (C) 2024 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: MIT

"""
Load license detectors
"""

from __future__ import annotations

from ..config.licenses import LicenseConfig
from .askalono import AskalonoLicenseDetector
from .base import LicenseDetector, LicenseDetectorNotAvailableError
from .scancode import ScancodeLicenseDetector
from .trivy import TrivyLicenseDetector

DETECTORS: dict[str, type[LicenseDetector]] = {
    AskalonoLicenseDetector.NAME: AskalonoLicenseDetector,
    ScancodeLicenseDetector.NAME: ScancodeLicenseDetector,
    TrivyLicenseDetector.NAME: TrivyLicenseDetector,
}


def get_detectors(
    cli_config: dict[str, str],
    license_config: LicenseConfig,
    detectors: dict[str, type[LicenseDetector]] = DETECTORS,
    find_only: bool = False,
) -> tuple[dict[str, LicenseDetector], dict[str, LicenseDetectorNotAvailableError]]:
    found: dict[str, LicenseDetector] = {}
    errored: dict[str, LicenseDetectorNotAvailableError] = {}
    for name, class_ in detectors.items():
        try:
            detector = class_(cli_config, license_config, find_only)
        except LicenseDetectorNotAvailableError as exc:  # noqa PERF203
            errored[name] = exc
        else:
            found[name] = detector
    return found, errored
