"""
Utility functions for loading and selecting random quotes from a JSONL file.
"""
import json
import random
import re


def load_quotes(jsonl_path):
    """
    Load quotes from a JSONL file.

    Each line should be a JSON object with 'quote' and 'author'.
    """
    quotes = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line)
                quotes.append({
                    'text': re.sub(r'[“”]', '', entry.get('quote')),
                    'author': entry.get('author')
                })
            except json.JSONDecodeError:
                continue
    return quotes

def get_random_quotes(quotes, n=4):
    """Return n random quotes from the list of quotes."""
    return random.sample(quotes, n)

if __name__ == "__main__":
    quotes = load_quotes("src/data/quotes_extended.jsonl")
    random_quotes = get_random_quotes(quotes, 4)
    print("\n")
    for i, q in enumerate(random_quotes, 1):
        print(
            f"{i}. “{q['text']}” - {q['author']}\n"
        )
