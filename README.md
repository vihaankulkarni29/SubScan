# SubScan
# SubstituScan

**SubstituScan** is a lightweight Python tool designed to extract amino acid substitutions from EMBOSS alignment files. Built with Biopython and ready to run in Google Colab, it simplifies comparison between protein sequences—especially for AMR gene variation studies across lab isolates.

## 🔍 Features
- Extracts amino acid substitutions from pairwise EMBOSS alignments
- Outputs clean reports in Excel (.xlsx) format
- Automatically labels gene names using filenames
- Google Colab-compatible for easy execution without local setup

## 🧪 Ideal Use Cases
- Antimicrobial resistance (AMR) gene comparisons
- Mutational analysis across multiple protein alignments
- Easy visualization and tabulation of substitutions

## 📂 Input Format
- A folder of EMBOSS alignment files (`.txt`, `.aln`, etc.)
- Each file contains 3-line aligned blocks (Ref, Match, Query)

## 📤 Output
A single Excel spreadsheet with:
| Gene Name | Substitutions |
|-----------|----------------|
| acrB      | I348T          |
| tetA      | L219F          |

## 🚀 How to Use
1. Upload the folder of alignment files via file picker
2. Run the notebook in Google Colab
3. Download the Excel output

## 💡 Example
```bash
acrB.aln → I348T
marR.aln → P20L


    

