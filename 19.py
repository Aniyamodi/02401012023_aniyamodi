import string
string_with_punctuation = input("Enter a string with punctuation: ")
cleaned_string = string_with_punctuation.translate(str.maketrans("", "", string.punctuation))
print("String without punctuation:", cleaned_string)
