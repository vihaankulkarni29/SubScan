# SubScan Usage Guide

## Quick Start

### 1. Process a Single Alignment File

```bash
python SubScan.py examples/sample_alignment.aln
```

This will:
- Read the alignment file
- Extract amino acid substitutions
- Generate `Amino_Acid_Substitution_Report.xlsx` in the current directory

### 2. Process Multiple Files in a Directory

```bash
python SubScan.py path/to/alignments/
```

This will:
- Scan the directory for all `.txt`, `.aln`, and `.align` files
- Process each file individually
- Combine all results into one Excel file

### 3. Specify Output Filename

```bash
python SubScan.py examples/sample_alignment.aln -o my_report.xlsx
```

## Understanding the Output

The Excel file contains two columns:

| Column Name  | Description                                              |
|--------------|----------------------------------------------------------|
| Gene Name    | Extracted from the input filename (without extension)    |
| Substitution | Amino acid change in format: `[Ref AA][Position][Query AA]` |

### Example Output

| Gene Name        | Substitution |
|------------------|--------------|
| sample_alignment | L219F        |
| sample_alignment | Q485R        |

This means:
- At position 219: Leucine (L) → Phenylalanine (F)
- At position 485: Glutamine (Q) → Arginine (R)

## Input File Format

SubScan expects EMBOSS alignment format with 3-line blocks:

```
Ref      1 MIKLSTLAIL  10
           ||||||.|||
Query    1 MIKLSTTAIL  10
```

Where:
- Line 1: Reference sequence with position and amino acids
- Line 2: Match indicators (| for match, . or : for mismatch)
- Line 3: Query sequence with position and amino acids

### Match Line Indicators
- `|` - Identical amino acids
- `.` or `:` - Substitution (reported by SubScan)
- ` ` (space) - Gap or alignment issue (ignored)

## Advanced Usage

### Processing Specific File Types

By default, SubScan processes files with these extensions:
- `.txt`
- `.aln`
- `.align`

To process other extensions, you can:
1. Rename your files to use supported extensions
2. Or modify the `alignment_files` filter in `SubScan.py`

### Batch Processing Example

**Windows PowerShell:**
```powershell
# Process multiple directories
python SubScan.py data/batch1/ -o batch1_results.xlsx
python SubScan.py data/batch2/ -o batch2_results.xlsx
python SubScan.py data/batch3/ -o batch3_results.xlsx
```

**Linux/macOS:**
```bash
# Process multiple directories in one command
for dir in data/*/; do
    python SubScan.py "$dir" -o "${dir%/}_results.xlsx"
done
```

## Common Workflows

### Workflow 1: AMR Gene Analysis

```bash
# 1. Place all AMR gene alignment files in a folder
mkdir amr_genes
cp acrB.aln tetA.aln marR.aln amr_genes/

# 2. Run SubScan
python SubScan.py amr_genes/ -o amr_substitutions.xlsx

# 3. Open the Excel file for analysis
```

### Workflow 2: Single Gene Variant Screening

```bash
# Process individual gene across multiple isolates
python SubScan.py isolate1/acrB.aln -o isolate1_acrB.xlsx
python SubScan.py isolate2/acrB.aln -o isolate2_acrB.xlsx
python SubScan.py isolate3/acrB.aln -o isolate3_acrB.xlsx
```

## Interpreting Results

### Substitution Notation

SubScan uses standard notation for amino acid substitutions:

- **I348T**: Isoleucine at position 348 changed to Threonine
- **L219F**: Leucine at position 219 changed to Phenylalanine
- **P20L**: Proline at position 20 changed to Leucine

### Common Amino Acid Codes

| Code | Amino Acid    | Code | Amino Acid   |
|------|---------------|------|--------------|
| A    | Alanine       | M    | Methionine   |
| C    | Cysteine      | N    | Asparagine   |
| D    | Aspartic acid | P    | Proline      |
| E    | Glutamic acid | Q    | Glutamine    |
| F    | Phenylalanine | R    | Arginine     |
| G    | Glycine       | S    | Serine       |
| H    | Histidine     | T    | Threonine    |
| I    | Isoleucine    | V    | Valine       |
| K    | Lysine        | W    | Tryptophan   |
| L    | Leucine       | Y    | Tyrosine     |

## Tips and Best Practices

1. **File Naming**: Use descriptive gene names as filenames (e.g., `acrB.aln`, `tetA.aln`) since these become the "Gene Name" in the output

2. **Quality Control**: Review alignment files before processing to ensure proper formatting

3. **Backup Data**: Keep original alignment files separate from output reports

4. **Excel Analysis**: Use Excel's filtering and sorting features to analyze substitution patterns

5. **Version Control**: Include SubScan output files in your analysis documentation

## Troubleshooting

### No Substitutions Found

If SubScan reports "No substitutions found":
- Check that your alignment has mismatch indicators (`.` or `:`)
- Verify the alignment follows EMBOSS 3-line block format
- Ensure amino acids differ between reference and query sequences

### File Not Recognized

- Verify file extension is `.txt`, `.aln`, or `.align`
- Check file is not empty
- Ensure file has read permissions

### Unicode/Encoding Errors

SubScan expects UTF-8 encoding. If you encounter errors:
```bash
# Convert file to UTF-8 (Linux/macOS)
iconv -f ISO-8859-1 -t UTF-8 input.aln > output.aln

# Then process
python SubScan.py output.aln
```

## Getting Help

For additional help:
```bash
python SubScan.py --help
```

For issues or feature requests, please visit the GitHub repository.
