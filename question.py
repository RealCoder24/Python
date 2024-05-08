<<<<<<< HEAD
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_next_question(self):
        return self.questions[self.question_index]

    def play(self):
        while self.question_index < len(self.questions):
            current_question = self.get_next_question()
            print(f"Q{self.question_index + 1}: {current_question['question']}")
            for i, choice in enumerate(current_question['choices']):
                print(f"{i + 1}: {choice}")
            answer = input("Your answer (1-4): ")
            if int(answer) - 1 == current_question['answer_index']:
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")
            self.question_index += 1
        print(f"Game Over! Your final score is: {self.score}")

# Example questions
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["New York", "London", "Paris", "Tokyo"],
        "answer_index": 2,
    },
    {
        "question": "Which is NOT a prime number?",
        "choices": ["2", "3", "4", "5"],
        "answer_index": 2,
    },
    # Add more questions as needed
]

# Start the quiz
quiz = Quiz(questions)
quiz.play()
=======
print('Welcome to AskPython Quiz')
answer = input('Are you ready to play the Quiz? (yes/no): ')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1: What is your favorite programming language? ')
    if answer.lower() == 'python':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    answer = input('Question 2: Do you follow any author on AskPython? ')
    if answer.lower() == 'yes':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    answer = input('Question 3: What is the name of your favorite website for learning Python? ')
    if answer.lower() == 'askpython':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    print(f'Thank you for playing this small quiz game. You attempted {score} questions correctly!')
    mark = (score / total_questions) * 100
    print(f'Marks obtained: {mark:.1f}')
else:
    print('Goodbye!')
>>>>>>> 899b366d3988126237f74144bed115599f8702bc
