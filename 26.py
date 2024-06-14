string = input("Enter a string: ")
prefix = input("Enter prefix to check: ")
suffix = input("Enter suffix to check: ")
if string.startswith(prefix):
    print("String starts with the prefix.")
else:
    print("String does not start with the prefix.")
if string.endswith(suffix):
    print("String ends with the suffix.")
else:
    print("String does not end with the suffix.")
