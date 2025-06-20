# Function to process data frame and create separate multi-page PDFs for each column
makeFeaturePlots <- function(seurat_obj, df, output_dir) {
  
  # Loop through each column in the data frame
  for (col_name in colnames(df)) {
    
    # Extract the column, remove empty cells, and process
    gene_list <- df[[col_name]] %>%
      .[nzchar(.)] %>%          # Remove empty strings and NA values
      trimws() %>%              # Trim whitespace
      tolower() %>%             # Convert to lowercase
      tools::toTitleCase()      # Capitalize first letter of each word
    
    # Check if the gene list is not empty
    if (length(gene_list) > 0) {
      
      # Create PDF filename based on column name
      pdf_filename <- file.path(output_dir, paste0(col_name, ".pdf"))
      
      # Open PDF device for this specific column/cell type
      pdf(pdf_filename, width = 15, height = 8)
      
      # Loop through each marker in the gene list
      for (marker in gene_list) {
        
        # Check if the marker exists in the Seurat object
        if (marker %in% rownames(seurat_obj)) {
          
          # Create FeaturePlot for individual marker
          feature_plot <- FeaturePlot(seurat_obj, features = marker) + 
            ggtitle(paste("Feature Plot for:", marker, "(", col_name, ")"))
          
          print(feature_plot)  # Print to current page of PDF
          
        } else {
          # If marker not found, create a warning plot or skip
          message(paste("Marker", marker, "not found in Seurat object for", col_name))
          
          # Optional: Create a blank page with warning message
          plot.new()
          text(0.5, 0.5, paste("Marker", marker, "not found"), 
               cex = 2, col = "red")
          title(paste("Missing Marker:", marker, "(", col_name, ")"))
        }
      }
      
      # Close the PDF device for this column
      dev.off()
      
      message(paste("Created PDF:", pdf_filename, "with", length(gene_list), "pages"))
      
    } else {
      message(paste("No valid genes found in column:", col_name))
    }
  }
  
  return(seurat_obj)  # Return the Seurat object
}
