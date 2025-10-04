import random
import json
import importlib.resources as pkg_resources
from codegnan_quest.quest_engine import QuestTracker

class QuizEngine:
    def __init__(self):
        self.tracker = QuestTracker()

        with pkg_resources.open_text("codegnan_quest.resources", "mcqs.json") as f:
            self.mcqs = json.load(f)

        with pkg_resources.open_text("codegnan_quest.resources", "coding_questions.json") as f:
            self.coding_questions = json.load(f)

    def ask_random_mcq(self):
        mcq = random.choice(self.mcqs)
        print(f"\nMCQ #{mcq['id']}: {mcq['question']}")
        for opt in mcq['options']:
            print(opt)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer == mcq['answer']:
            print("✅ Correct! 🎉", mcq['explanation'])
            self.tracker.award_badge(f"MCQ_{mcq['id']}")
            return True
        else:
            print(f"❌ Wrong! {mcq['explanation']}")
            return False

    def ask_random_coding_question(self):
        question = random.choice(self.coding_questions)
        print(f"\nCoding Challenge #{question['id']}: {question['question']}")
        print("Enter your function code (e.g., 'def is_palindrome(s): ...'):")
        user_code = input("Your code:\n")

        try:
            local_env = {}
            exec(user_code, {}, local_env)

            func_name = question['function_name']
            func = local_env.get(func_name)
            if not func:
                print("Error: Function not found in your code.")
                return False

            for test in question['test_cases']:
                result = func(test['input'])
                if result != test['output']:
                    print(f"❌ Test failed: Input {test['input']} expected {test['output']}, got {result}")
                    return False

            print("✅ All tests passed! 🎉 Learn more: https://codegnan.com/coding-challenges")
            self.tracker.award_badge(f"Coding_{question['id']}")
            return True
        except Exception as e:
            print(f"Error in code: {e}")
            return False

def start_python_quest():
    quiz = QuizEngine()
    print("\nWelcome to CodegnanQuest! Choose your challenge:")
    choice = input("1) MCQ or 2) Coding Question? (Enter 1 or 2): ")
    if choice == "1":
        quiz.ask_random_mcq()
    elif choice == "2":
        quiz.ask_random_coding_question()
    else:
        print("Invalid choice! Try again.")
