from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=130, min_length=30):
    # Some models have a token limit (~1024 for BART), so truncate if needed
    if len(text.split()) > 1000:
        text = ' '.join(text.split()[:1000])

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


if __name__ == "__main__":
    sample_text = """
    The European Space Agency has announced a new mission to study exoplanets. 
    Scientists are excited to learn more about planets outside our solar system 
    and potentially find signs of life. The mission, which will launch in 2026, 
    will use advanced telescopes to scan distant stars and their planetary systems.
    """
    print("Summary:\n", summarize_text(sample_text))
