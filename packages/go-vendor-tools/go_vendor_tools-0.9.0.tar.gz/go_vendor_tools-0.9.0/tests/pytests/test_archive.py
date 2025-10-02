# Copyright (C) 2024 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: MIT

from __future__ import annotations

import sys
from pathlib import Path

from pytest_mock import MockerFixture

from go_vendor_tools.cli.go_vendor_archive import (
    CreateArchiveArgs,
    OverrideArgs,
    create_archive,
    override_command,
)
from go_vendor_tools.config.base import create_base_config, load_config

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomlkit as tomllib


def test_vendor_archive_base(mocker: MockerFixture, tmp_path: Path) -> None:
    patched_run_command = mocker.patch(
        "go_vendor_tools.cli.go_vendor_archive.run_command"
    )
    mocked_add_files_to_archive = mocker.patch(  # noqa F841
        "go_vendor_tools.cli.go_vendor_archive.add_files_to_archive"
    )
    (directory := tmp_path / "directory").mkdir()
    config = create_base_config(
        {
            "archive": {
                "dependency_overrides": {"golang.org/x/sys": "v0.6.0"},
                "post_commands": [["echo", "Hello world!"]],
            }
        }
    )
    args = CreateArchiveArgs(
        path=directory,
        output=Path("vendor.tar.xz"),
        use_top_level_dir=False,
        use_module_proxy=False,
        tidy=True,
        idempotent=False,
        compression_type=None,
        compresslevel=None,
        config_path=tmp_path / "go-vendor-tools.toml",
        config=config,
        write_config=False,
    )
    create_archive(args)
    expected_calls = [
        ["go", "get", "golang.org/x/sys@v0.6.0"],
        ["go", "mod", "tidy"],
        ["go", "mod", "vendor"],
        ["echo", "Hello world!"],
    ]
    calls = [list(c.args[1]) for c in patched_run_command.call_args_list]
    assert expected_calls == calls


def test_vendor_archive_write_config(tmp_path: Path) -> None:
    args = CreateArchiveArgs.construct(
        subcommand="create",
        path=tmp_path,
        output=Path("vendor.tar.bz2"),
        idempotent=False,
        compression_type="bz2",
        compresslevel=9,
        config_path=tmp_path / "go-vendor-tools.toml",
        write_config=True,
    )
    args.write_config_opts()
    with open(args.config_path, "rb") as fp:
        data = tomllib.load(fp)
    assert data == {"archive": {"compression_type": "bz2", "compresslevel": 9}}


def test_vendor_archive_override(tmp_path: Path) -> None:
    config_path = tmp_path / "config.toml"
    args = OverrideArgs(
        config_path=config_path, import_path="golang.org/x/sys", version="v0.6.0"
    )
    override_command(args)
    output_config = load_config(config_path)
    expected_dependency_overrides = {"golang.org/x/sys": "v0.6.0"}
    gotten_dependency_overrides = output_config["archive"]["dependency_overrides"]
    assert expected_dependency_overrides == gotten_dependency_overrides
