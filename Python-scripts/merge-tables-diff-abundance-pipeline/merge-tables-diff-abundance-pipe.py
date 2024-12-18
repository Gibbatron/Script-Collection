## Script to merge normalised, variance stabilised, and DEG tables together following the differential abundance pipeline.

import pandas as pd

# Load the data
normalised_counts = pd.read_csv("processed_abundance/all.normalised_counts.tsv", sep="\t")
vst_counts = pd.read_csv("processed_abundance/all.vst.tsv", sep="\t")
degs = pd.read_csv("differential/hpv-vs-naive.deseq2.results.tsv", sep="\t")

# Select the relevant columns
normalised_selected = normalised_counts[["gene_id"] + ["Hpb_1", "Hpb_2", "Hpb_3", "Hpb_5", "Naive_1", "Naive_2", "Naive_3", "Naive_5"]]

vst_selected = vst_counts[["Hpb_1", "Hpb_2", "Hpb_3", "Hpb_5", "Naive_1", "Naive_2", "Naive_3", "Naive_5"]]

degs_selected = degs  # Assuming DEGs.tsv has 'gene_id' as the first column

# Concatenate the tables
merged_table = pd.concat([normalised_selected, vst_selected, degs_selected.drop(columns=["gene_id"])], axis=1)

# Create a row indicating the source of each column
source_row = ["normalised_counts"] * (1 + 8) + ["vst_counts"] * 8 + ["degs"] * (len(degs_selected.columns) - 1)
source_row_df = pd.DataFrame([source_row], columns=merged_table.columns)

# Change the first column value of the source row to 'data_type'
source_row_df.iloc[0, 0] = "data_type"

# Add the source row above the merged table
merged_table_with_source = pd.concat([source_row_df, merged_table], ignore_index=True)

# Save the merged table
merged_table_with_source.to_csv("merged_table.tsv", sep="\t", index=False)

print("Merged table created >> saved to 'merged_table.tsv'.")
