import os
import json
import re
from collections import defaultdict

def build_inverted_index(data_dir):
    inverted_index = defaultdict(set)
    files = sorted([f for f in os.listdir(data_dir) if f.endswith('.txt')])

    for filename in files:
        # Extract Doc ID from filename (e.g., 'doc01.txt' -> 'Doc 1')
        doc_num = int(re.search(r'\d+', filename).group())
        doc_label = f"Doc {doc_num}"

        path = os.path.join(data_dir, filename)
        with open(path, 'r', encoding='utf-8') as f:
            # Tokenize: lowercase and remove punctuation
            text = f.read().lower()
            tokens = re.findall(r'\b\w+\b', text)

            for word in tokens:
                inverted_index[word].add(doc_label)

    # Convert sets to sorted lists for JSON
    return {word: sorted(list(docs), key=lambda x: int(x.split()[1]))
            for word in sorted(inverted_index.keys())}

print("✅ Indexer function defined.")