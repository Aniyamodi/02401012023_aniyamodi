numbers = [int(num) for num in input("Enter numbers separated by spaces: ").split()]
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print("Occurrences of", element, "in the list:", count)
