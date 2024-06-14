# Program to read the content of a text file and print it to console

# Opening the text file in read mode
with open("input.txt", "r") as file:
    # Reading the content of the file
    content = file.read()

# Printing the content to the console
print("Content of the file:")
print(content)
