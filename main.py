"""
Multiplication Table

Write a function named "print_multiplication_table" which gets the following arguments passed: two integer values, first a
certain number for which the multiplication table shall be printed and secondly a number that specifies the numbers of rows.
Only numbers bigger than 0 are valid numbers. Print an error message if either the number or the rows are zero or negative.
Make use of type hints when declaring the function.

Example calls of function:
    print_multiplication_table(6, 3) >>
    1 * 6 = 6
    2 * 6 = 12
    3 * 6 = 18

    print_multiplication_table(10, 2) >>
    1 * 10 = 10
    2 * 10 = 20

    print_multiplication_table(-10, 2) >>
    Number and rows cannot be less than 1.

    print_multiplication_table(2, -2) >>
    Number and rows cannot be less than 1.

    print_multiplication_table(0, 0) >>
    Number and rows cannot be less than 1.

"""


def print_multiplication_table(number: int, rows: int):
    if number < 1 or rows < 1:
        print("number and rows cannot be less than 1")
    else:
        i = 1
        while i <= rows:
            print(f"{i} * {number} = {i * number}")
            i += 1


"""
Palindromes

Write a function called is_palindrome that takes a string as parameter input and returns True if the string is a palindrome,
and False otherwise. A palindrome is a word or phrase, that reads the same forward and backward, ignoring spaces and capitalization.
Make use of type hints when declaring the function.
Hint: to replace a specific character in a string you can use replace method, eg.: "hello".replace("e", "o") will replace all occurences of "e" with "o" -> "hollo"

Example calls of function:
    is_palindrome("taco cat") -> True
    is_palindrome("Step on no pets") -> True
    is_palindrome("Never odd or even") -> True
    is_palindrome("Me no palindrome") -> False
"""


def is_palindrome(word: str) -> bool:
    # first remove all capitalization and white spaces
    word = word.lower().replace(" ", "")
    # reverse the word
    # check if both are the same
    return word == word[::-1]

    # for i in range(len(word) -1, -1, -1):
    #     reversed += word[i]
    # return reversed == word


if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values.")
    print_multiplication_table(6, 3)
    print_multiplication_table(10, 2)
    print_multiplication_table(-2, 3)
    print_multiplication_table(6, -3)
    print(is_palindrome("taco cat"))
    print(is_palindrome("Step on no pets"))
    print(is_palindrome("Never odd or even"))
    print(is_palindrome("Me no palindrome"))



