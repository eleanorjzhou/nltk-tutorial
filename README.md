# NLTK Tutorial

The purpose of this tutorial is to explore the NLTK modules.

## Day 1 - Initial Project Setup

### Before anything
1. Install Python ([latest ver.](https://www.python.org/downloads/))
2. Install Numpy (optional): `pip install numpy`

### Flask - Initial Setup
1. Create an environment in the project folder: `py -3 -m venv .venv`
2. Activate the environment when working on the project: `.venv\Scripts\activate` (run `deactivate` when not using the environment)
3. Install Flask: `pip install Flask`
4. Create the `app.py` file that renders the app:
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)
```
5. Create the `static` and `templates` folders, and within them create the `index.html` and `style.css` files
6. To serve the app, run `Flask run`


### NLTK - Initial Setup
1. While Flask environment is activated, install NLTK: `pip install nltk`
2. Then install NLTK Data: `python -m nltk.downloader popular`, or in the Python interpreter `import nltk; nltk.download('popular')`

### NLTK-Flask Setup
1. In `App.py`, import the NLTK module: `import nltk`
2. To find out usages of NLTK modules, check out the [Module Index](https://www.nltk.org/py-modindex.html) of the NLTK Documentation
3. For example, we can use the `nltk.tokenize.word_tokenize` module to tokenize text input: 
```
# Example: Tokenization
    tokens = nltk.tokenize.word_tokenize(text)
```

### Getting results to the app
1. In the `App.py` file, add the process function for tokenization and returning the token to a result page: 
```
from flask import request

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
```
2. Create `result.html` in the `templates` folder to show the tokens:
```
<h2>Tokenized Text:</h2>
<ul>
    {% for token in tokens %}
        <li>{{ token }}</li>
    {% endfor %}
</ul>
```







