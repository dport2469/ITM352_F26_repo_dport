def ask_question(question, options):
   """Present a question to the user and return True if the answer is correct."""
   print(question)
   for letter, option in zip('abcd', options):
       print(f"{letter}) {option}")
  
   while True:
       answer = input("Your answer (a/b/c/d): ").lower()
       if answer in 'abcd':
           return answer == options[4]  # The correct answer is stored at index 4
       print("Invalid input. Please enter a, b, c, or d.")


def run_quiz(questions):
   """Run the quiz and return the final score."""
   score = 0
   total_questions = len(questions)
  
   for i, q in enumerate(questions, 1):
       print(f"\nQuestion {i} of {total_questions}:")
       if ask_question(q['question'], q['options']):
           print("Correct!")
           score += 1
       else:
           print(f"Sorry, that's incorrect. The correct answer was: {q['options'][4]}")
  
   return score, total_questions


def main():
#    questions = load_questions('quiz_questions.json')
   questions = [
   {
       "question": "What is the capital of France?",
       "options": ["London", "Berlin", "Madrid", "Paris", "d"]
   },
   {
       "question": "Which planet is known as the Red Planet?",
       "options": ["Venus", "Mars", "Jupiter", "Saturn", "b"]
   }
]
   print("Welcome to the Quiz Game!")
   score, total = run_quiz(questions)
   print(f"\nQuiz completed! Your final score is {score} out of {total}.")


if __name__ == "__main__":
   main()
