# Changelog

All notable changes to SubScan will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-12-02

### 🎉 Major Release - Windows/Local Compatibility

This release transforms SubScan from a Google Colab-only tool to a cross-platform command-line application.

### Added
- **Command-line interface** with argparse support
- **Directory processing** - analyze multiple alignment files at once
- **Custom output filenames** via `-o` flag
- **Comprehensive documentation**:
  - Detailed README with installation and usage
  - USAGE.md with examples and workflows
  - CONTRIBUTING.md for contributors
  - Sample alignment file for testing
- **Professional repository structure**:
  - MIT License
  - .gitignore for Python projects
  - requirements.txt with dependencies
  - examples/ directory
- **Enhanced error handling** and user feedback
- **Progress indicators** showing files processed and results found
- **Cross-platform support** (Windows, macOS, Linux)

### Changed
- **Removed Google Colab dependencies** (`google.colab.files`)
- **Local file system operations** instead of upload/download interface
- **Improved code structure** with docstrings and modular functions
- **Better output formatting** with emoji indicators and clear messages
- **Updated column name** from "Difference" to "Substitution" for clarity

### Fixed
- File encoding issues with UTF-8 support
- Path handling for different operating systems
- Empty file and directory handling

### Removed
- Google Colab-specific code and pip install commands
- Dependency on Colab file upload/download widgets

## [1.0.0] - 2024

### Initial Release
- Basic amino acid substitution extraction
- Google Colab notebook interface
- Excel output generation
- Support for EMBOSS alignment format

---

## Legend
- 🎉 Major feature
- ✨ New feature
- 🐛 Bug fix
- 📝 Documentation
- ♻️ Refactoring
- ⚡ Performance improvement
- 🔒 Security fix
