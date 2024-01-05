from flask import *
import pandas as pd
from transformers import pipeline
import sys
import os
import tempfile
from io import StringIO
from werkzeug.utils import secure_filename
from tkinter import *
import re
from datetime import datetime
import urllib.request
import torch

# generate a secret key:
import secrets
generated_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = generated_key  # Set a secret key for session security

# Load the CSV file into a pandas DataFrame
# df = pd.read_csv('data/data.csv')

# Instantiate a question-answering pipeline using a pre-trained model
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

@app.route('/')
def home():
    date = datetime.now()
    date_now = date.strftime("%Y%M")

    if 'messages' not in session:
        session['messages'] = []

    return render_template('index.html', messages=session['messages'])

@app.route('/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        user_question = request.form['user_question']
        # abstracts = df['Abstract'].tolist()

        # Find the most relevant abstract for the question
        # best_answer = find_best_answer(user_question, abstracts)

        # Use the language model to answer the question based on the selected abstract
        # answer = qa_pipeline(question=question, context=best_answer)

        # AI response
        ai_answer = "here is your question:  {}".format(user_question)

        # Retrieve existing messages from session
        messages = session.get('messages', [])

        # Append user's question and AI's answer to messages
        messages.append(('user', user_question))
        messages.append(('ai', ai_answer))
        # Update session with the new messages
        session['messages'] = messages

        return render_template('index.html', messages=session['messages'])


def find_best_answer(question, abstracts):
    # Placeholder logic for finding the most relevant answer
    return abstracts[0]

if __name__ == '__main__':
    app.run(debug=True)

################################################################
# Currently use an in-memory session storage,
# if the Flask server restarts,
# the session data will be lost.
# For a more persistent solution,
# consider using a database to store conversation history