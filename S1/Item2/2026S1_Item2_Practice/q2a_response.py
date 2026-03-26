"""
    Python submission file

    ITEM 2 (PRACTICE - TERTIARY) - QUESTION 2

    Provide your responses for Q2 here
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

with open("S1/Item2/2026S1_Item2_Practice/raw_cards.csv",mode="r") as f:
    z = f.readlines()
    x = []
    for i in z:
        i = i.strip('\n')
        if len(i.split(',')) == 2:

            x.append(i.split(','))
    for i in range(len(x)):
        for a in range(len(x[i])):
            x[i][a] = x[i][a].strip()
    print(x)

with open("S1/Item2/2026S1_Item2_Practice/cards_cleaned.csv",mode="w") as w:
    for i in x:
        w.write(f"{i[0]}|{i[1]}\n")