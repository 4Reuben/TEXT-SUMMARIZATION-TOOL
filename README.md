# TEXT-SUMMARIZATION-TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: REUBEN THOMAS JOHN

*INTERN ID*:CTO4DN1267

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH

## Project Description

This project is a simple yet effective demonstration of Natural Language Processing (NLP) techniques to generate a concise summary from a large chunk of text. The objective is to extract the most relevant information from a given input and generate a shorter version that retains the original meaning. 

The summarizer is based on **frequency-based extractive summarization**, which uses the frequency of words to score sentences and select the top-ranking ones. It’s not abstractive or AI-generated text—it pulls the most meaningful lines from the original content. This type of summarization is fast, lightweight, and doesn't require any external API calls.

The script was developed as part of an internship at **CodTech IT Solutions**, and it serves as Task 1 in the internship’s deliverables.

## Technologies & Tools Used

- **Python 3.x**
- **spaCy** – for NLP processing (tokenization, sentence segmentation, stopwords, etc.)
- **Heapq module** – for selecting top-scoring sentences
- **Jupyter Notebook / VS Code / Any Python IDE**
- **Command Line Interface (CLI)** – for running the script
- **Plain Text Files (.txt)** – for input and output

## File Structure

Codtech IT Solutions/

│

├── Task-1/

│ ├── summarizer.py # Main Python script

│ ├── sample_input.txt # Input text file with content to summarize

│ ├── output_summary.txt # Automatically generated summary

│ └── README.md # Project documentation (this file)

## How It Works

1. **Input**: The script reads text from `sample_input.txt`.
2. **Processing**: Using `spaCy`, the text is tokenized and processed to:
   - Remove stopwords and punctuation
   - Count word frequencies
   - Score each sentence based on those frequencies
3. **Summary Generation**: The top 3 scored sentences are selected and stitched together to form a summary.
4. **Output**: The result is printed on the terminal and saved to `output_summary.txt`.

## What I Did

- Installed and configured `spaCy`, and downloaded the `en_core_web_sm` model.
- Wrote a function to read text input from a file.
- Built a frequency-based sentence scoring system.
- Implemented summary generation using the `heapq` module.
- Saved the summary to a new file.
- Tested the script on Wikipedia-style content.

## What I Didn't Do (Yet)

- No abstractive summarization or use of advanced ML/DL models like BERT.
- No web interface or GUI (it's a CLI tool only).
- No dynamic input from user (file name is hard-coded).
- Didn’t integrate it with any API or real-world application—yet.

## What I Learned

- How NLP libraries like `spaCy` tokenize and process text.
- How to use `heapq` to select top items based on scoring.
- File handling in Python using UTF-8 encoding.
- Debugging path and module errors using CLI.
- How to build a functional mini project that outputs real results.

## Acknowledgments

Special thanks to **CodTech IT Solutions** for providing this opportunity. This was my first ever NLP project, and it helped me get familiar with the basics of text summarization and using Python for automation tasks.

## OUTPUT

![Image](https://github.com/user-attachments/assets/59d10bf0-914b-4c09-ac14-6acfb7bfbbfa)
