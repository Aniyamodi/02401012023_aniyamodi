# Program to write a string to a text file

# Taking input string from user
input_string = input("Enter a string: ")

# Opening a text file in write mode
with open("output.txt", "w") as file:
    # Writing the input string to the file
    file.write(input_string)

print("String has been written to 'output.txt' file.")
