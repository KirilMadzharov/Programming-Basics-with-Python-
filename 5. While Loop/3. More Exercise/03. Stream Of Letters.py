"""
Write a program that reads a hidden message into a string of characters.

They are received one at a time until the "End" command is received.
Words are formed from the letters in the order they are read.

Non-Latin characters should be ignored. The words hidden in the stream
are separated by a secret command of three letters - "c", "o" and "n".

The first time one of these letters is received, it is marked as encountered,
but not saved in the word. At each subsequent encounter, it is recorded normally
in the word.

After all three characters of the command are present, the word " " and a space are printed.

A new word is started, which similarly waits for the secret command to be printed.
"""



letter = input()

complete_word, skip_letters_count, guess_word = "",  "",  ""

while letter != "End":
    if letter in "con":
        skip_letters_count += letter
    elif letter.islower() or letter.isupper():
        guess_word += letter

    if "c" in skip_letters_count and "o" in skip_letters_count and "n" in skip_letters_count:
        complete_word += f"{guess_word} "
        guess_word, skip_letters_count = "", ""
    if skip_letters_count.count(letter) > 1:
        guess_word += letter

    letter = input()

print(complete_word)

