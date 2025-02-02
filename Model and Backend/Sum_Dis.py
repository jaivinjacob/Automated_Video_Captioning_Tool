import re
import pandas as pd
from transformers import BartTokenizer, BartForConditionalGeneration
import torch
from tqdm import tqdm

# Load the tokenizer and model
bart_tokenizer = BartTokenizer.from_pretrained('/content/drive/MyDrive/Test New Model/saved_model')
bart_model = BartForConditionalGeneration.from_pretrained('/content/drive/MyDrive/Test New Model/saved_model')


def process_and_summarize(descriptions):
    def extract_main_description(text):
        # Define a regex pattern to match the main description
        pattern = re.compile(r'^(.*?)(?:\.\s*(?:close-up|close up|slow motion|4k video footage).*)?$')
        match = pattern.match(text)
        if match:
            return match.group(1).strip()
        else:
            return text.strip()

    # Extract main descriptions from each item in the list
    extracted_descriptions = [extract_main_description(desc) for desc in descriptions]
    
    # Concatenate the list of descriptions into a single string
    input_text = ' '.join(extracted_descriptions)
    
    # Tokenize the input text
    inputs = bart_tokenizer.encode(input_text, return_tensors='pt')
    
    # Generate summary
    summary_ids = bart_model.generate(
        inputs,
        max_length=100,
        min_length=30,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    
    # Decode the summary
    summary = bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    summary = extract_main_description(summary)
    
    return summary
