from flask import Flask, render_template

app = Flask(__name__)

def swap_variables(a, b):
    a, b = b, a
    return a, b

@app.route('/')
def home():
    x, y = 20, 30
    before = (x, y)
    x, y = swap_variables(x, y)
    after = (x, y)
    return render_template('luminism_task2.html', before=before, after=after)

if __name__ == '__main__':
    app.run(debug=True)
