def reverse_string(original):
    rev = ''
    for i in original:
        rev = i + rev
    return rev
word = str(input("Enter the string"))
print("reversed string: ", reverse_string(word))