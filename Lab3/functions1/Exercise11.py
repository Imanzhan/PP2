def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
word = input()
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
