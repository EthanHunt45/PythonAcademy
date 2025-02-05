# Defining a 'Question' class
class Question:
    def __init__(self, question, answer):
        self.question = question  # Stores the question text
        self.answer = answer  # Stores the correct answer

# List of math questions
math_questions = [
    "What is 2+2?\na-) 3\nb-) 4\nc-) 5",  # Question 1
    "What is 2*2?\na-) 3\nb-) 4\nc-) 5"   # Question 2
]

# Creating a list of Question objects
exam = [
    Question(math_questions[0], "b"),  # Answer for first question: 'b'
    Question(math_questions[1], "b"),  # Answer for second question: 'b'
]

# Function to run the exam
def run_exam():
    score = 0  # Initial score
    for question in exam:
        # Ask the user the question and take input
        answer = input(question.question + "\nYour answer: ").lower()
        if answer == question.answer:  # Check if the answer is correct
            score += 1  # Increase score for correct answer
    print(f"Your final score: {score}/{len(exam)}")  # Print the final score

# Start the exam
run_exam()
