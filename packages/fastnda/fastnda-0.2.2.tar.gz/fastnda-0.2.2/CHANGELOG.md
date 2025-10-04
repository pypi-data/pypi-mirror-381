# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [v2025.06.02]
### Fixed
- Higher-precision Timestamp interpolation.
- Compatibility with PEP 639.


## [v2025.05.15]
### Added
- Support for ndc file version 17


## [v2025.04.02]
### Added
- Support for current range -40000

### Changed
- Project moved to https://github.com/d-cogswell/NewareNDA


## [v2025.02.13]
### Added
- Millisecond timestamp accuracy for ndc 11 and 14
- Support for OCV step type
- Additional current range

### Fixed
- Timestamp interpolation bug that occasionally resulted in negative dt


## [v2025.01.02]
### Added
- Additional current range settings

### Fixed
- Addressed a PerformanceWarning related to the Timestamp field


## [v2024.12.02]
### Added
- Support for ndax aux temperature (ndc version 14, filetype 5)


## [v2024.10.01]
### Added
- Added regression tests for NewareNDAcli

### Changed
- Changed the NewareNDAcli flag from --software_cycle_number to --no_software_cycle_number


## [v2024.09.03]
### Added
- dtype specifications for auxiliary data.
- Addtional current range multipliers.
- Regression tests for software_cycle_number and cycle_mode keywords.

### Fixed
- Millisecond timing now read from BTS 9.1 files.

### Changed
- Refactored NewareNDAx.py to explicitly treat ndc files based on version and filetype.


## [v2024.08.01]
### Added
- Read aux temperature data from BTS 9.1 files.

### Fixed
- Bug fixes for BTS 9.1.

### Changed
- setup.py converted to pyproject.toml
- Reworked logging functionality with new log_level keyword.


## [v2024.07.01]
### Added
- Initial support for BTS 9.1 files.
- Additional auxiliary fields read for ndc version 11.

### Fixed
- Incorrect range multiplier


## [v2024.06.03]
### Added
- Active mass and comments are read and returned as a logging messages.
- More regression tests.
- Additional hardware ranges.
- Aux voltage is now read from nda files.

### Fixed
- Correct voltage, current, capacity scalings for ndax files with ndc version 14 data.
- Handling of timestamps now matches Neware. Dates are read as UTC and then converted to local time zone.

### Changed
- Warning now use logging.warning() instead of warnings.warn().


## [v2024.05.01]
### Added
- Unsupported nda versions now raise exceptions.

### Fixed
- More robust support for nda version 130


## [v2024.04.01]
### Added
- Github workflow with regression testing and code coverage.
- Hardware range settings.

### Fixed
- Issue #50 related to missing Aux data.


## [v2024.03.01]
### Added
- Additional range setting added.

### Fixed
- Resolved FutureWarnings for pandas 3.0


## [v2024.02.01]
### Added
- Expanded ndax aux channel support (ndc version 11).
- 'extras_require' added to setup.py for testing.


## [v2024.01.02]
### Added
- Support for nda files from BTS9.
- New 'cycle_mode' keyword argument to specify how cycle number should be generated.
- Additional current ranges.

### Fixed
- Bug fixes for ndax support.


## [v2023.12.01]
### Added
- Support for ndax from BTS Server 8.
- Additional ndax verison information now returned as logging.

### Changed
- 'software_cycle_number=True' is now the default for ndax.


## [v2023.11.01]
### Added
- Ability to read auxiliary data from ndax files.
- pytest regression tests for code development.

### Fixed
- Support for constant power charge and discharge.
- Additional current ranges.

### Changed
- 'software_cycle_number=True' is one again the default behavior for nda.


## [v2023.10.02]
### Added
- Support for constant power charge and discharge.
- Additional current ranges.


## [v2023.07.03]
### Added
- Support for reading ndax.


## [v2023.06.01]
### Added
- Missing current range.
- Performance improvements

### Changed
- The cycle number is now read directly from the nda file for compatibility with the newest version of BTSDA. Previous numbering can be restored with the new 'software_cycle_number' flag.


## [v2023.05.01]
### Fixed
- Issue #20, files failing to load.
- Updates to README.


## [v2023.04.14]
### Added
- Significant performance improvement.
- PEP8 code formatting consistency.

### Fixed
- Issue #22 that occasionally resulted in incorrect temperature values.


## [v2023.02.01]
### Added
- Support for additional current ranges and states

### Fixed
- Maintenance updates and code cleanup

### Changed
- Conditions used for locating first data record


## [v2022.10.03]
### Added
- Additional current ranges

### Fixed
- Improved performance and reduced memory usage.


## [v2022.09.06]
### Added
- Commandline nda file conversion tool
- Performance improvements

### Fixed
- Added missing status and current ranges

### Changed
- 'Jump' field removed
- Default index is used for the DataFrame and set_index() is no longer called


## [v2022.08.01]
### Added
- Performance improvements

### Fixed
- Added missing status and current range


## [v2022.07.01]
### Added
- Ability to read temperature fields

### Fixed
- Step field now matches Neware output
- Correct handling of 'SIM' steps

### Changed
- Charge/discharge capacity/energy are now separate fields


## [2022.06.01]
### Added
- More robust error handling
- Additional hardware ranges implemented

### Fixed
- Cycle and Step now match Neware


## [v0.1.0] - 2022-05-10
### Added
- Initial release tested on nda versions 7.6 and 8.0.