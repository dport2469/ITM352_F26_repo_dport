from flask import Flask, json, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        return redirect(url_for('result'))
    
    # Load the question and options to display
    return render_template('quiz.html')  # Displays the question and options

@app.route('/result')
def result():
    # Calculate and display the user's score
    score = 1  # Example score for demonstration
    return render_template('result.html', score=score)


if __name__ == "__main__":
    # load questions.json
    with open("questions.json", "r") as f:
        questionsJSON = f.read()
    questions = json.loads(questionsJSON)
    app.run(debug=True, host="127.0.0.1", port=5000)
