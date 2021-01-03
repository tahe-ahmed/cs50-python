import string
import math

text = input("Text : ")

letters = 0
words = 1
sentence = 0

for char in text:
    if char == " ":
        words += 1
    elif char == '?' or char == "!" or char == ".":
        sentence += 1
    elif char in string.ascii_lowercase or char in string.ascii_uppercase:
        letters += 1

# the average chars and sentence per 100 words
L = float(letters) / float(words) * 100.0
S = float(sentence) / float(words) * 100.0

# calculate the index
index = 0.0588 * L - 0.296 * S - 15.8
round_index = round(index)

if round_index < 0:
    grade = 1
else:
    grade = round_index if round_index <= 16 else '16+'

print(f"Grade : {grade}")
