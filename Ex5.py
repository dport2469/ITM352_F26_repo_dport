# Ask for a sentence from the user (using input()).  Turn the sentence into a list of strings. Reverse the list.  Join the reversed list back into a string.
sentence = input("Enter a sentence: ")
chars = list(sentence)
chars.reverse()
reversed_sentence = "".join(chars)
print(reversed_sentence)