# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:44:26 2023

@author: DELL
"""
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import json
import unittest

# Load the list of questions from the qs.txt file
with open('qs.txt', 'r') as f:
    questions = [q.strip() for q in f.readlines()]

# Load the Hugging Face tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

# Initialize the Flask app
app = Flask(__name__)

# Define a function to get the most similar questions to the user input
def get_similar_questions(user_input, k=5):
    # Tokenize the user input
    inputs = tokenizer(user_input, return_tensors='pt')
    # Get the model output for the user input
    outputs = model(**inputs)
    # Get the predicted label for the user input
    predicted_label = torch.argmax(outputs.logits)
    # Get the indices of the questions with the same label as the user input
    similar_question_indices = [i for i, q in enumerate(questions) if torch.argmax(model(**tokenizer(q, return_tensors='pt')).logits) == predicted_label]
    # Get the top-k most similar questions
    similar_questions = [questions[i] for i in similar_question_indices[:k]]
    return similar_questions

# Define a Flask route to get similar questions
@app.route('/get_similar_questions', methods=['POST'])
def get_similar_questions_route():
    # Get the user input from the JSON payload
    user_input = request.json['user_input']
    # Get the most similar questions to the user input
    similar_questions = get_similar_questions(user_input)
    # Return the top-k most similar questions as a JSON response
    return jsonify({'similar_questions': similar_questions})


if __name__ == '__main__':
    app.run()


