with open("source.txt", "r") as source_file:
    content = source_file.read()
with open("destination.txt", "w") as destination_file:
    destination_file.write(content)
print("Contents copied from 'source.txt' to 'destination.txt'.")