# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

from pathlib import Path

TESTS_DIR = Path(__file__).parent
DATA_DIR = TESTS_DIR / "data"
SPEC_MINIMAL = DATA_DIR / "spec_minimal"
SPEC_RPMAUTOSPEC = DATA_DIR / "spec_rpmautospec"
SPEC_TRADITIONAL = DATA_DIR / "spec_traditional"
SPEC_AUTOSETUP = DATA_DIR / "spec_autosetup"
SPEC_AUTOPATCH = DATA_DIR / "spec_autopatch"
SPEC_PATCHLIST = DATA_DIR / "spec_patchlist"
SPEC_INCLUDES = DATA_DIR / "spec_includes"
SPEC_MACROS = DATA_DIR / "spec_macros"
SPEC_PRERELEASE = DATA_DIR / "spec_prerelease"
SPEC_PRERELEASE2 = DATA_DIR / "spec_prerelease2"
SPEC_MULTIPLE_SOURCES = DATA_DIR / "spec_multiple_sources"
SPEC_COMMENTED_PATCHES = DATA_DIR / "spec_commented_patches"
SPEC_SHELL_EXPANSIONS = DATA_DIR / "spec_shell_expansions"
SPEC_NO_TRAILING_NEWLINE = DATA_DIR / "spec_no_trailing_newline"
SPEC_CONDITIONALIZED_CHANGELOG = DATA_DIR / "spec_conditionalized_changelog"
SPEC_CONDITIONALIZED_VERSION = DATA_DIR / "spec_conditionalized_version"

SPECFILE = "test.spec"
