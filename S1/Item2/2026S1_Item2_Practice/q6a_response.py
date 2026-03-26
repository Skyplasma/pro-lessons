"""
    Python submission file

    ITEM 2 (PRACTICE - TERTIARY) - QUESTION 6

    Provide your responses for Q6 here
    Unless otherwise indicated, no other files will be assessed for this question

    If you delete a file or it is otherwise missing from your submission,
    you will automatically score 0 for the question.
    If you think you are missing a file, ask your teacher for help.

    Test your code! Read any errors which are reported by the interpreter and fix them.

    Code which does not execute will be heavily penalized!

    Avoid the use of any imports/modules which were not covered in our lesson notes.
    When in doubt about whether you can include something, ask your teacher.

    Comment your code if it helps you, but only working code will earn marks.
    Do your best to write a functional program, even if it is not perfect.

    When writing your Python program, prioritize:
    1. Correctness - the program should do what is required by the question
    2. Simplicity - do not use a more complex technique when a simpler one will do
    3. Style - natural naming for variables and functions, line length, etc.
"""

#!/usr/bin/python3

Token = input("gimme dat token  ")
upperc = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"
num = "0123456789"
listed = []
for i in Token:
    listed.append(i)
print(len(listed))
if len(listed) == 5:
    print("Length Valid")
    if listed[0] in upperc and listed[1] in upperc and listed[4] in upperc and listed[2] in num and listed[3] in num:
        print("a")
    else:
        print("b")