from flask import Flask, render_template, request
import nltk


app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/process', methods=['POST'])
def process():
    # Extract the text from the request
    text = request.form['text']

    # Perform NLTK operations on the text
    # Example: Tokenization
    tokens = nltk.tokenize.word_tokenize(text)

    # Print the tokenized text in the console
    print("Tokenized Text:")
    for token in tokens:
        print(token)

    # Return the results
    return render_template('result.html', tokens=tokens)


