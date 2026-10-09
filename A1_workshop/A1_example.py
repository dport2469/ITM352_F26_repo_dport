import json
import random
from pathlib import Path

QUIZ_FILE = Path(__file__).with_name("quiz_data.json")


def load_quiz(path=QUIZ_FILE):
     with open(path, encoding="utf-8") as f:
          return json.load(f)


LETTERS = "abcd"
WIDTH = 60


def print_header(title):
     print("=" * WIDTH)
     print(title.center(WIDTH))
     print("=" * WIDTH)


def display_question(number, total, question, options):
     print(f"\nQuestion {number} of {total}")
     print("-" * WIDTH)
     print(question if question.endswith("?") else question + "?")
     print()
     for letter, option in zip(LETTERS, options):
          print(f"   {letter.upper()}) {option}")
     print()


def get_choice(num_options):
     valid = LETTERS[:num_options]
     prompt = f"Your answer ({valid[0].upper()}-{valid[-1].upper()}): "
     while True:
          choice = input(prompt).strip().lower()
          if len(choice) == 1 and choice in valid:
               return valid.index(choice)
          print("  Invalid choice. Please enter one of the listed letters.")


def ask_question(number, total, question, info):
     """Ask one question until answered correctly; return the number of guesses."""
     options = random.sample(info["options"], len(info["options"]))
     display_question(number, total, question, options)

     attempts = 0
     while True:
          attempts += 1
          if options[get_choice(len(options))] == info["correct"]:
               print("  ✔ Correct!" if attempts == 1 else f"  ✔ Correct! (took {attempts} tries)")
               return attempts
          print("  ✘ Not quite. Try again.")


def print_results(first_try_correct, total_attempts, total):
     print()
     print_header("RESULTS")
     print(f"Correct on first try: {first_try_correct} of {total}")
     print(f"Total guesses:        {total_attempts}")
     print(f"Score:                {first_try_correct / total:.0%}")


def run_quiz(data):
     print_header("QUIZ TIME")
     questions = list(data.items())
     random.shuffle(questions)

     first_try_correct = 0
     total_attempts = 0
     for number, (question, info) in enumerate(questions, start=1):
          attempts = ask_question(number, len(questions), question, info)
          total_attempts += attempts
          if attempts == 1:
               first_try_correct += 1

     print_results(first_try_correct, total_attempts, len(questions))


if __name__ == "__main__":
     run_quiz(load_quiz())