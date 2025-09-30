from flask import Flask, render_template
import string

app = Flask(__name__)

def word_lengths(sentence):
    words = sentence.split()
    lengths = {word.strip(string.punctuation): len(word.strip(string.punctuation)) for word in words}
    return lengths

@app.route('/')
def home():
    sentence = "task 3 of kane and norman."
    result = word_lengths(sentence)
    return render_template('luminism_task3.html', sentence=sentence, result=result)

if __name__ == '__main__':
    app.run(debug=True)
