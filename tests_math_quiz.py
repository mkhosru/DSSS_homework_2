import unittest
from math_quiz import rand_int, rand_choice_ari_operation, calculation

class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        """
        Test rand_int to ensure it generates random numbers within the specified range.

        It runs the function 1000 times and checks if each generated number is within the range [1, 10].
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_choice_ari_operation(self):
        """
        Test rand_choice_ari_operation to ensure it returns one of the specified operators {+, -, *}.

        It runs the function 1000 times and checks if each result is in the set {+, -, *}.
        """
        operators = {'+', '-', '*'}
        for _ in range(1000):
            rand_operator = rand_choice_ari_operation()
            self.assertIn(rand_operator, operators)

    def test_calculation(self):
        """
        Test calculation with predefined test cases.

        It checks if the function produces the correct arithmetic expressions and answers for each test case.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            # Add more test cases here
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
