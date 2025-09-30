from flask import Flask, render_template

app = Flask(__name__)

def list_length(my_list):
    return len(my_list)

@app.route('/')
def home():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = list_length(numbers)
    return render_template('luminism_task1.html', numbers=numbers, result=result)

if __name__ == '__main__':
    app.run(debug=True)
