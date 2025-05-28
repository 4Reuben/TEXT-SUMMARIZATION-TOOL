# Task-1: Text Summarization using NLP and Python
# This script reads a text file, summarizes its content using NLP techniques, and saves the summary to a new file.
# Requirements: Install spacy and download the English model using `python -m spacy download en_core_web_sm`

import spacy
from string import punctuation
from heapq import nlargest

# Load English tokenizer, POS tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def read_text_from_file(filename):
    """Reads text content from a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def summarize_text(text, num_sentences=3):
    """Summarizes the text using frequency-based extractive summarization"""
    doc = nlp(text)
    
    # Calculate word frequencies (excluding stopwords and punctuation)
    word_frequencies = {}
    for token in doc:
        if token.text.lower() not in nlp.Defaults.stop_words and token.text.lower() not in punctuation:
            if token.text.lower() not in word_frequencies:
                word_frequencies[token.text.lower()] = 1
            else:
                word_frequencies[token.text.lower()] += 1

    # Normalize frequencies
    max_freq = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    # Score sentences
    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_frequencies:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Select top N sentences as the summary
    summarized_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    final_summary = ' '.join([sent.text for sent in summarized_sentences])
    
    return final_summary

def save_summary_to_file(summary, filename="Task-1/output_summary.txt"):
    """Saves the summary to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(summary)

def main():
    print("📄 Text Summarization Tool - Using NLP & Python")
    input_path = "Task-1/sample_input.txt"
    print(f"Reading input text from {input_path}...\n")
    
    input_text = read_text_from_file(input_path)
    
    print("Original Text:")
    print(input_text[:500] + "\n... [truncated] ...\n")  # Print first 500 chars

    print("Generating summary...\n")
    summary = summarize_text(input_text, num_sentences=3)

    print("🔍 Summary:")
    print(summary)

    save_summary_to_file(summary)
    print("\n✅ Summary saved to 'output_summary.txt'")

if __name__ == "__main__":
    main()
