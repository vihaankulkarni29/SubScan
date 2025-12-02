#!/usr/bin/env python3
"""
SubScan - Amino Acid Substitution Analyzer
Extracts amino acid substitutions from EMBOSS alignment files.
"""

import os
import re
import sys
import argparse
from pathlib import Path
import pandas as pd


def find_simple_substitutions(block_text):
    """
    Detect amino acid substitutions and indels in a single alignment block.
    
    Handles EMBOSS NEEDLE/WATER and Waterman-Eggert formats.
    - NEEDLE/WATER: Reference on top, Query on bottom
    - Waterman-Eggert: Query on top, Reference on bottom
    
    Match line indicators:
    - '|' = identical match
    - '.' or ':' = substitution (similar or dissimilar)
    - ' ' (space) = gap or mismatch
    
    Args:
        block_text: String containing 3-line alignment block (Line1, Match, Line2)
    
    Returns:
        List of variant strings (e.g., ["L7F", "del_109", "ins_162_K"])
    """
    lines = block_text.strip().split('\n')
    if len(lines) != 3:
        return []

    line1 = lines[0]
    match_line = lines[1]
    line2 = lines[2]

    variants = []

    # Extract sequence information from both lines
    line1_match = re.search(r'(\S+)\s+(\d+)\s+([A-Z\-]+)\s+(\d+)', line1)
    line2_match = re.search(r'(\S+)\s+(\d+)\s+([A-Z\-]+)\s+(\d+)', line2)

    if not line1_match or not line2_match:
        return []

    line1_name = line1_match.group(1)
    line1_start = int(line1_match.group(2))
    line1_seq = line1_match.group(3)
    
    line2_name = line2_match.group(1)
    line2_start = int(line2_match.group(2))
    line2_seq = line2_match.group(3)

    # Detect format by checking sequence names
    # NEEDLE/WATER typically has "Reference" or "WP_" first
    # Waterman-Eggert has "Query" or "NZ_" first
    if 'Reference' in line1_name or 'WP_' in line1_name or line1_name.startswith('ref'):
        # NEEDLE/WATER format: Reference on top
        ref_seq = line1_seq
        ref_start = line1_start
        query_seq = line2_seq
        query_start = line2_start
    else:
        # Waterman-Eggert or reverse format: Query on top, Reference on bottom
        ref_seq = line2_seq
        ref_start = line2_start
        query_seq = line1_seq
        query_start = line1_start

    # Find the match string position aligned with sequences
    seq_start_index = line1.find(line1_seq)
    if seq_start_index == -1:
        return []
    
    match_str_start = seq_start_index
    match_str_end = match_str_start + len(line1_seq)
    
    if match_str_start < 0 or match_str_end > len(match_line):
        return []
    
    match_str = match_line[match_str_start:match_str_end]

    if len(ref_seq) != len(query_seq) or len(ref_seq) != len(match_str):
        return []

    # Track position in reference sequence (accounting for gaps)
    ref_pos = ref_start

    for i in range(len(ref_seq)):
        ref_aa = ref_seq[i]
        query_aa = query_seq[i]
        match_char = match_str[i]

        # Case 1: Both sequences have amino acids (no gaps)
        if ref_aa != '-' and query_aa != '-':
            # Check if it's a substitution (match_char is NOT '|')
            if match_char != '|':
                # It's a mismatch/substitution
                variants.append(f"{ref_aa}{ref_pos}{query_aa}")
            ref_pos += 1
        
        # Case 2: Deletion in query (gap in query, amino acid in ref)
        elif ref_aa != '-' and query_aa == '-':
            variants.append(f"del_{ref_pos}")
            ref_pos += 1
        
        # Case 3: Insertion in query (amino acid in query, gap in ref)
        elif ref_aa == '-' and query_aa != '-':
            # Insertion after the previous reference position
            variants.append(f"ins_{ref_pos - 1}_{query_aa}")

    return variants


def find_substitutions_from_full_alignment(alignment_text):
    """
    Process complete alignment file and extract all substitutions.
    
    Args:
        alignment_text: Full text content of alignment file
    
    Returns:
        List of substitution strings
    """
    lines = alignment_text.strip().splitlines()
    substitutions = []
    i = 0
    while i < len(lines) - 2:
        block = '\n'.join(lines[i:i+3])
        if lines[i].strip() == '' or lines[i+1].strip() == '' or lines[i+2].strip() == '':
            i += 1
            continue
        block_subs = find_simple_substitutions(block)
        substitutions.extend(block_subs)
        i += 3
    return substitutions


def process_alignment_files(input_path, output_file="Amino_Acid_Substitution_Report.xlsx"):
    """
    Process alignment files and generate Excel report.
    
    Args:
        input_path: Path to alignment file or directory of alignment files
        output_file: Name of output Excel file
    """
    input_path = Path(input_path)
    results = []
    files_processed = 0

    if input_path.is_file():
        # Process single file
        print(f"📂 Processing file: {input_path.name}")
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                text = f.read()
            subs = find_substitutions_from_full_alignment(text)
            gene_name = input_path.stem
            if subs:
                for sub in subs:
                    results.append({"Gene Name": gene_name, "Variant": sub})
                print(f"   ✓ Found {len(subs)} variant(s)")
            else:
                results.append({"Gene Name": gene_name, "Variant": "No variants found"})
                print(f"   ℹ No variants found")
            files_processed += 1
        except Exception as e:
            print(f"   ✗ Error processing file: {e}")
            
    elif input_path.is_dir():
        # Process all files in directory
        print(f"📂 Processing directory: {input_path}")
        alignment_files = list(input_path.glob('*.*'))
        
        if not alignment_files:
            print("   ⚠ No files found in directory")
            return
            
        for file_path in alignment_files:
            if file_path.is_file() and file_path.suffix.lower() in ['.txt', '.aln', '.align']:
                print(f"   Processing: {file_path.name}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text = f.read()
                    subs = find_substitutions_from_full_alignment(text)
                    gene_name = file_path.stem
                    if subs:
                        for sub in subs:
                            results.append({"Gene Name": gene_name, "Variant": sub})
                        print(f"     ✓ Found {len(subs)} variant(s)")
                    else:
                        results.append({"Gene Name": gene_name, "Variant": "No variants found"})
                        print(f"     ℹ No variants found")
                    files_processed += 1
                except Exception as e:
                    print(f"     ✗ Error: {e}")
    else:
        print(f"❌ Error: '{input_path}' is not a valid file or directory")
        return

    # Generate Excel report
    if files_processed == 0:
        print("❌ No files were processed successfully")
        return
        
    if not results:
        results.append({"Gene Name": "None", "Variant": "No variants found"})

    df = pd.DataFrame(results)
    df.to_excel(output_file, index=False)
    print(f"\n✅ Report saved as '{output_file}'")
    print(f"📊 Processed {files_processed} file(s), found {len(results)} result(s)")


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="SubScan - Extract amino acid substitutions from EMBOSS alignment files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process a single alignment file
  python SubScan.py alignments/acrB.aln
  
  # Process all alignment files in a directory
  python SubScan.py alignments/
  
  # Specify custom output filename
  python SubScan.py alignments/ -o my_results.xlsx
        """
    )
    
    parser.add_argument(
        'input',
        help='Path to alignment file or directory containing alignment files'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='Amino_Acid_Substitution_Report.xlsx',
        help='Output Excel filename (default: Amino_Acid_Substitution_Report.xlsx)'
    )
    
    args = parser.parse_args()
    
    print("🔬 SubScan - Amino Acid Substitution Analyzer")
    print("=" * 50)
    
    process_alignment_files(args.input, args.output)


if __name__ == "__main__":
    main()
