# SNP-Seek Chat Assistant

This project is a web-based chatbot that helps users navigate the SNP-Seek database using natural language questions. Instead of searching through long user guides or FAQs, users can simply ask questions like “How do I filter SNPs by chromosome?” and receive a response based on the files uploaded on the vector

The chatbot was built using OpenAI’s Assistant API and Streamlit. It uses uploaded files (e.g., SNP-Seek FAQs, user guides, and reference papers) to provide document-based responses. This project was created to make it easier for students and researchers to interact with bioinformatics tools.

## Features

- Chat interface with document-based answers
- Cites the file where the answer came from
- Easy to run locally with Python and Streamlit
- Supports both web interface and CLI version

## Requirements

- Python 3.8+
- Streamlit
- OpenAI Python package

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/PatrickHenryGarcia/SNP-SeekChatBot.git
   cd SNP-SeekChatBot
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key and Assistant ID inside the `SNP-SeekChat.py` file:
   ```python
   openai.api_key = "your_api_key_here"
   ASSISTANT_ID = "your_assistant_id_here"
   ```

4. Run the chatbot locally:
   ```bash
   streamlit run SNP-SeekChat.py
   ```

5. Ask your questions and receive answers with file citations.

## Purpose

This project was developed as part of a research presentation to explore how AI can be used to support bioinformatics platforms like SNP-Seek. It aims to make genomic tools more accessible by improving user support through AI-enhanced interaction.

## Author

**Patrick Henry W. Garcia**  
UPLB CAS - Institute of Physics
