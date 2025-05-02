import pandas as pd
from summarizer_core import summarize_text

# Load mini dataset
df = pd.read_csv("mini_cnn_dataset.csv")

# Run summarizer on first 5 rows
for i in range(5):
    article = df.iloc[i]["article"]
    reference_summary = df.iloc[i]["highlights"]

    try:
        generated_summary = summarize_text(article)
    except Exception as e:
        print(f"Error at index {i}: {e}")
        continue

    print(f"\n📰 Article #{i+1}")
    print("-" * 40)
    print(f"Original Article (first 300 chars):\n{article[:300]}...\n")
    print(f"📌 Reference Summary:\n{reference_summary}\n")
    print(f"🧠 Generated Summary:\n{generated_summary}")
    print("=" * 60)
