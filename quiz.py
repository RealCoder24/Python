"""
quiz.py

An interactive multiple-choice quiz game implemented with a Quiz class.

- Presents a series of questions with multiple choices to the user.
- Accepts user input and checks answers.
- Tracks and displays the user's score at the end.

Usage:
    Run the script and follow the prompts in the terminal.
"""
class Quiz:
    """
    A class to represent a multiple-choice quiz game.

    Attributes:
        questions (list): List of question dictionaries.
        score (int): The user's current score.
        question_index (int): The index of the current question.
    """
    def __init__(self, question_data):
        """
        Initialize the Quiz with a list of questions.

        Args:
            question_data (list): List of question dictionaries.
        """
        self.questions = question_data
        self.score = 0
        self.question_index = 0

    def get_next_question(self):
        """
        Retrieve the next question in the quiz.

        Returns:
            dict: The next question dictionary.
        """
        return self.questions[self.question_index]

    def play(self):
        """
        Start the quiz game, prompt the user for answers, and display the final score.
        """
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
