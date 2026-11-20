from flask import Flask, render_template, request


QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "choices": [
            ("a", "London"),
            ("b", "Berlin"),
            ("c", "Madrid"),
            ("d", "Paris"),
        ],
        "answer": "d",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": [
            ("a", "Venus"),
            ("b", "Mars"),
            ("c", "Jupiter"),
            ("d", "Saturn"),
        ],
        "answer": "b",
    },
]

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answers = {
            str(index): request.form.get(f"question_{index}", "")
            for index in range(len(QUESTIONS))
        }

        for index, question in enumerate(QUESTIONS):
            valid_choices = {key for key, _ in question["choices"]}
            if answers[str(index)] not in valid_choices:
                return render_template(
                    "quiz.html",
                    questions=QUESTIONS,
                    answers=answers,
                    error="Please answer every question before submitting.",
                )

        results = []
        score = 0
        for index, question in enumerate(QUESTIONS):
            selected_key = answers[str(index)]
            choice_labels = dict(question["choices"])
            is_correct = selected_key == question["answer"]
            score += is_correct
            results.append(
                {
                    "question": question["question"],
                    "selected": choice_labels[selected_key],
                    "correct_answer": choice_labels[question["answer"]],
                    "is_correct": is_correct,
                }
            )

        return render_template(
            "quiz.html",
            results=results,
            score=score,
            total=len(QUESTIONS),
        )

    return render_template("quiz.html", questions=QUESTIONS)


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
