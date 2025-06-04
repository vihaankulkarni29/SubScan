
!pip install openpyxl > /dev/null

import os
import re
import pandas as pd
from google.colab import files

# 🔬 Substitution detection
def find_simple_substitutions(block_text):
    lines = block_text.strip().split('\n')
    if len(lines) != 3:
        return []

    ref_line = lines[0]
    match_line = lines[1]
    query_line = lines[2]

    substitutions = []

    ref_match = re.search(r'(\d+)\s+([A-Z\-]+)', ref_line)
    query_match = re.search(r'(\d+)\s+([A-Z\-]+)', query_line)

    if not ref_match or not query_match:
        ref_seq_fallback_match = re.search(r'([A-Z\-]+)', ref_line)
        query_seq_fallback_match = re.search(r'([A-Z\-]+)', query_line)
        if ref_seq_fallback_match and query_seq_fallback_match:
            ref_seq = ref_seq_fallback_match.group(1)
            query_seq = query_seq_fallback_match.group(1)
            ref_start = None
        else:
            return []
    else:
        ref_start = int(ref_match.group(1))
        ref_seq = ref_match.group(2)
        query_seq = query_match.group(2)

    ref_seq_start_index = ref_line.find(ref_seq, ref_line.find(str(ref_start)) if ref_start is not None else 0)
    if ref_seq_start_index == -1:
        match_str_start_index = len(ref_line) - len(ref_seq)
    else:
        match_str_start_index = ref_seq_start_index

    if match_str_start_index < 0 or match_str_start_index + len(ref_seq) > len(match_line):
        adjusted_len = min(len(ref_seq), len(match_line) - max(0, match_str_start_index))
        if adjusted_len <= 0:
            return []
        match_str = match_line[max(0, match_str_start_index) : max(0, match_str_start_index) + adjusted_len]
        ref_seq = ref_seq[:adjusted_len]
        query_seq = query_seq[:adjusted_len]
    else:
        match_str = match_line[match_str_start_index : match_str_start_index + len(ref_seq)]

    if len(ref_seq) != len(query_seq) or len(ref_seq) != len(match_str):
        return []

    for j in range(len(ref_seq)):
        if match_str[j] in ['.', ':'] and ref_seq[j] != '-' and query_seq[j] != '-' and ref_seq[j] != query_seq[j]:
            pos = ref_start + j if ref_start is not None else f"Index {j+1}"
            substitutions.append(f"{ref_seq[j]}{pos}{query_seq[j]}")

    return substitutions

def find_substitutions_from_full_alignment(alignment_text):
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


print("📤 Upload your EMBOSS alignment files (one or more):")
uploaded = files.upload()


results = []
for filename, file in uploaded.items():
    text = file.decode('utf-8')
    subs = find_substitutions_from_full_alignment(text)
    for sub in subs:
        results.append({"Gene Name": os.path.splitext(filename)[0], "Difference": sub})


output_file = "Amino_Acid_Substitution_Report.xlsx"
if not results:
    results.append({"Gene Name": "None", "Difference": "No substitutions found"})

df = pd.DataFrame(results)
df.to_excel(output_file, index=False)
print(f"✅ Report saved as {output_file}")


files.download(output_file)
