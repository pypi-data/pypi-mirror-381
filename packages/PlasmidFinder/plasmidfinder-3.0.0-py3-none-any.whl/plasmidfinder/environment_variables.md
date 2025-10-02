# Environment Variables for PlasmidFinder

Environment variables recognized by PlasmidFinder, the flag they replace and the default value for the flag. Provided command line flags will always take precedence. Set environment variables takes precedence over default flag values.

Additional Environment variables can be added by appending entries to the table below. The 'Flag' entry in the table must be the double dash flag recognised by PlasmidFinder. The 'Default Value' entry is just for information.

## Environment Variables Table

| Environment Variabel       | Flag                | Default Value  |
|----------------------------|---------------------|----------------|
| CGE_PLASMIDFINDER_DB       | db_path             | None           |
| CGE_PLASMIDFINDER_GENE_COV | min_cov             | 0.60           |
| CGE_PLASMIDFINDER_GENE_ID  | threshold           | 0.90           |
| CGE_METHOD                 | method_path         | None           |
