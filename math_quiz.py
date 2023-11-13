#------------modified code-----------
import random
# Function to generate a random integer within the specified range
def rand_int(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)
# Function to choose and return a random arithmetic operator
def rand_choice_ari_operation():
    """
    Random arithmetic operator.
    """
    return random.choice(['+', '-', '*'])
# Function to perform arithmetic operation based on two numbers and an operator
def calculation(n1, n2, o):
    """
    Perform arithmetic operation on two numbers based on the specified operator.

    Parameters:
    - n1 (int): The first operand.
    - n2 (int): The second operand.
    - o (str): The arithmetic operator (+, -, *).

    Returns:
    tuple: A tuple containing the arithmetic expression as a string and the result.
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a
# Function to run the math quiz game
def math_quiz():
    s = 0  # Initialize the score
    t_q = 3  # Number of quiz questions
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # Loop through the number of quiz questions
    for _ in range(t_q):
        n1 = rand_int(1, 10)
        n2 = rand_int(1, 5)  # corrected to use integers
        o = rand_choice_ari_operation()
        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        # Get user input for the answer
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)  # Convert user input to an integer
        # Check if the user's answer is correct
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Display the final score
    print(f"\nGame over! Your score is: {s}/{t_q}")
# Run the math quiz game if the script is executed directly
if __name__ == "__main__":
    math_quiz()
