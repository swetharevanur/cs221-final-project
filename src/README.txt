Script execution order:

1. Run web_crawler.py to generate a list of relevant Backpage URLs.
2. Run batch_parser.py to trace these URLs in batches and programmatically fetch post data.
3. Merge batch outputs and preprocess post texts with data_collator.py.

OUTPUT FILE: ../data/third_total_file_list.xlsx

Visit each subdirectory for a separate README (in this order: feature_engineering, lda, learning)