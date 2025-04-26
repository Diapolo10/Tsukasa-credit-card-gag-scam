
# Project Changelog

All notable changes to this project will be documented in this file.

The format is based on [CHANGELOG.md][CHANGELOG.md]
and this project adheres to [Semantic Versioning][Semantic Versioning].

<!-- 
TEMPLATE

## [major.minor.patch] - yyyy-mm-dd

A message that notes the main changes in the update.

### Added

### Changed

### Deprecated

### Fixed

### Removed

### Security

_______________________________________________________________________________
 
 -->

<!--
EXAMPLE

## [0.2.0] - 2021-06-02

Lorem Ipsum dolor sit amet.

### Added

- Cat pictures hidden in the library
- Added beeswax to the gears

### Changed

- Updated localisation files

-->

<!--
_______________________________________________________________________________

## [1.1.1] - 2025-04-26

This bugfix release fixes a deprecation warning from Nuitka, and adds the
ability to optionally read logs from the program if launched via a terminal.

### Added

- If you launch the program via a terminal, you can now read logs from it.
  Previously, no logs were available at all

### Fixed

- Nuitka no longer warns about the `--disable-console` command-line option
  being deprecated; it's been switched to the newer `--windows-console-mode`

-->

_______________________________________________________________________________

## [1.1.1] - 2025-04-26

This bugfix release fixes a deprecation warning from Nuitka, and adds the
ability to optionally read logs from the program if launched via a terminal.

### Added

- If you launch the program via a terminal, you can now read logs from it.
  Previously, no logs were available at all

### Fixed

- Nuitka no longer warns about the `--disable-console` command-line option
  being deprecated; it's been switched to the newer `--windows-console-mode`

_______________________________________________________________________________

## [1.1.0] - 2025-04-26

This release migrates the project from Poetry to uv, updates dependencies,
reformats parts of the codebase, and updates the README instructions.

### Changed

- Switched all Poetry parts to uv equivalents
- Updated dependencies
- Reformatted some parts of the program source code
- Updated the README to have better usage instructions
- Updated localisation files

_______________________________________________________________________________

## [0.1.2] - 2023-03-26

This release fixes problems with Nuitka, and updates Poetry to use grouped
dependencies.

### Changed

- Poetry now treats linters as a separate group
- Updated localisation files

### Fixed

- Nuitka builds in GitHub Actions now work properly

_______________________________________________________________________________

## [0.1.1] - 2023-03-24

This release adds automatic builds, improves the `README.md` file, updates
dependencies, and does some additional cleanup.

### Added

- Releases are now built automatically
- Bunch of metadata files, including this changelog

### Changed

- Added example GIF to `README.md`
- Updated dependencies
- Updated localisation files

_______________________________________________________________________________

## [0.1.0] - 2021-08-25

This is the initial version of the project.

### Added

- The base project

[CHANGELOG.md]: https://web.archive.org/web/20220330064336/https://changelog.md/
[Semantic Versioning]: http://semver.org/

<!-- markdownlint-configure-file {
    "MD024": false
} -->
<!--
    MD024: No duplicate headings
-->
