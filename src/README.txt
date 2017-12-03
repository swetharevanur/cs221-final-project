Script execution order:

1. Run web_crawler.py to generate a list of relevant Backpage URLs.
2. Run batch_parser.py to trace these URLs in batches and programmatically fetch post data.
3. Merge batch outputs and preprocess post texts with data_collator.py.