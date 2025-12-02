# SubScan

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**SubScan** is a lightweight Python command-line tool designed to extract amino acid substitutions from EMBOSS alignment files. It simplifies comparison between protein sequences—especially for AMR gene variation studies across lab isolates.

## 🔍 Features
- ✅ Extracts amino acid substitutions from pairwise EMBOSS alignments
- ✅ Outputs clean reports in Excel (.xlsx) format
- ✅ Automatically labels gene names using filenames
- ✅ Process single files or entire directories
- ✅ Cross-platform support (Windows, macOS, Linux)
- ✅ Command-line interface with flexible options

## 🧪 Ideal Use Cases
- Antimicrobial resistance (AMR) gene comparisons
- Mutational analysis across multiple protein alignments
- Easy visualization and tabulation of substitutions
- High-throughput screening of sequence variants

## 📂 Input Format
- EMBOSS alignment files (`.txt`, `.aln`, `.align`)
- Each file contains 3-line aligned blocks:
  ```
  Ref     1 MIKLSTLAIL  10
            ||||||.|||
  Query   1 MIKLSTTAIL  10
  ```

## 📤 Output
A single Excel spreadsheet with:
| Gene Name | Substitution |
|-----------|--------------|
| acrB      | I348T        |
| tetA      | L219F        |
| marR      | P20L         |

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pandas openpyxl
```

## 💻 Usage

### Basic Usage

**Process a single alignment file:**
```bash
python SubScan.py alignments/acrB.aln
```

**Process all alignment files in a directory:**
```bash
python SubScan.py alignments/
```

**Specify custom output filename:**
```bash
python SubScan.py alignments/ -o my_results.xlsx
```

### Command-Line Options
```
usage: SubScan.py [-h] [-o OUTPUT] input

positional arguments:
  input                 Path to alignment file or directory containing alignment files

optional arguments:
  -h, --help            Show help message and exit
  -o OUTPUT, --output OUTPUT
                        Output Excel filename (default: Amino_Acid_Substitution_Report.xlsx)
```

## 📖 Examples

### Example 1: Single File
```bash
python SubScan.py data/acrB.aln
```
Output:
```
🔬 SubScan - Amino Acid Substitution Analyzer
==================================================
📂 Processing file: acrB.aln
   ✓ Found 1 substitution(s)

✅ Report saved as 'Amino_Acid_Substitution_Report.xlsx'
📊 Processed 1 file(s), found 1 result(s)
```

### Example 2: Directory with Custom Output
```bash
python SubScan.py alignments/ -o amr_analysis_2024.xlsx
```

## 🗂️ Project Structure
```
SubScan/
├── SubScan.py              # Main application script
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
└── examples/             # Sample data and documentation
    ├── sample_alignment.aln
    └── USAGE.md
```

## 🛠️ Development

### Running Tests
```bash
# Test with sample data
python SubScan.py examples/sample_alignment.aln
```

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📋 Requirements
- Python 3.7+
- pandas >= 2.0.0
- openpyxl >= 3.1.0

## 🐛 Troubleshooting

**Issue: "No module named 'pandas'"**
```bash
pip install pandas openpyxl
```

**Issue: "Permission denied"**
- Ensure you have write permissions in the output directory
- Try specifying a different output path using `-o`

**Issue: "No files found in directory"**
- Check that alignment files have extensions: `.txt`, `.aln`, or `.align`
- Verify the directory path is correct

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍🔬 Author
**Vihaan Kulkarni** – Bioinformatics Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/vihaan-kulkarni)

## 🙏 Acknowledgments
- Built with [pandas](https://pandas.pydata.org/) for data manipulation
- Uses [openpyxl](https://openpyxl.readthedocs.io/) for Excel generation
- Designed for EMBOSS alignment output format

## 📞 Support
For issues, questions, or contributions, please open an issue on GitHub.

---

**Note:** This is a standalone command-line tool. The original Google Colab version is no longer maintained. For local usage, please follow the installation instructions above.
