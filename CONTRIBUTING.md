# Contributing to SubScan

Thank you for your interest in contributing to SubScan! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the Repository**
   - Fork the SubScan repository to your GitHub account
   - Clone your fork locally:
     ```bash
     git clone https://github.com/YOUR_USERNAME/SubScan.git
     cd SubScan
     ```

2. **Set Up Development Environment**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Install development dependencies (optional)
   pip install pytest black flake8
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Making Changes

### Code Style

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and modular

### Testing Your Changes

Before submitting:

1. **Test the core functionality:**
   ```bash
   python SubScan.py examples/sample_alignment.aln
   ```

2. **Test with different inputs:**
   - Single file
   - Directory of files
   - Custom output names
   - Edge cases (empty files, malformed alignments)

3. **Run style checks (if installed):**
   ```bash
   black SubScan.py
   flake8 SubScan.py
   ```

### Commit Guidelines

- Write clear, concise commit messages
- Use present tense ("Add feature" not "Added feature")
- Reference issue numbers when applicable

Example:
```bash
git commit -m "Add support for custom delimiter in output"
git commit -m "Fix #123: Handle empty alignment blocks"
```

## Types of Contributions

### Bug Reports

When reporting bugs, include:
- SubScan version
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Sample input file (if applicable)

**Template:**
```markdown
**Bug Description:**
Clear description of the issue

**To Reproduce:**
1. Run command: `python SubScan.py ...`
2. Observe error: ...

**Expected Behavior:**
What should have happened

**Environment:**
- OS: Windows 10 / macOS 14 / Ubuntu 22.04
- Python: 3.9.7
- SubScan version: 1.0.0

**Sample Data:**
Attach or describe the input file causing the issue
```

### Feature Requests

When suggesting features:
- Explain the use case
- Describe the expected behavior
- Consider backward compatibility
- Provide examples if possible

### Pull Requests

1. **Before Starting:**
   - Check if an issue exists for your feature/fix
   - Discuss major changes in an issue first
   - Ensure your change fits the project scope

2. **PR Checklist:**
   - [ ] Code follows project style guidelines
   - [ ] Tested with multiple input types
   - [ ] Updated documentation if needed
   - [ ] Updated CHANGELOG.md (if applicable)
   - [ ] No breaking changes (or clearly documented)

3. **PR Description Template:**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Motivation
   Why is this change needed?
   
   ## Changes Made
   - List specific changes
   - Include file modifications
   
   ## Testing
   - How was this tested?
   - What input files were used?
   
   ## Screenshots (if applicable)
   
   ## Related Issues
   Closes #123
   ```

## Development Areas

Areas where contributions are especially welcome:

### High Priority
- [ ] Unit tests for core functions
- [ ] Support for additional alignment formats
- [ ] Performance optimization for large files
- [ ] Better error handling and validation

### Medium Priority
- [ ] CSV output option
- [ ] Batch processing improvements
- [ ] Configuration file support
- [ ] Progress bars for large datasets

### Documentation
- [ ] Tutorial videos
- [ ] More usage examples
- [ ] API documentation
- [ ] Troubleshooting guide expansion

## Code of Conduct

### Our Standards

- **Be Respectful:** Treat all contributors with respect
- **Be Constructive:** Provide helpful feedback
- **Be Collaborative:** Work together toward the best solution
- **Be Patient:** Remember that everyone is learning

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

## Questions?

- **General questions:** Open a GitHub Discussion
- **Bug reports:** Open a GitHub Issue
- **Security issues:** Email the maintainer directly
- **Feature ideas:** Start with a GitHub Issue for discussion

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes for significant contributions
- GitHub contributors page

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make SubScan better!
