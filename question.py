"""
question.py

A simple interactive quiz game that asks the user three questions 
related to programming and Python learning resources.

- Greets the user and asks if they are ready to play.
- Asks three questions, checks answers, and keeps score.
- Displays the user's score and percentage at the end.
- Exits gracefully if the user is not ready to play.

Usage:
    Run the script and follow the prompts in the terminal.
"""
print('Welcome to AskPython Quiz')
answer = input('Are you ready to play the Quiz? (yes/no): ')

TOTAL_QUESTIONS = 3

def run_quiz():
    """Run the quiz game, ask questions, and calculate the score."""
    print('Let\'s start the quiz!')
    score = 0
    ans = input('Question 1: What is your favorite programming language? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    ans = input('Question 2: Do you follow any author on AskPython? ')
    if ans.lower() == 'yes':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    ans = input('Question 3: What is the name of your favorite website for learning Python? ')
    if ans.lower() == 'askpython':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    print(f'Thank you for playing this small quiz game. You attempted {score} questions correctly!')
    mark = (score / TOTAL_QUESTIONS) * 100
    print(f'Marks obtained: {mark:.1f}')

if answer.lower() == 'yes':
    run_quiz()
else:
    print('Goodbye!')
