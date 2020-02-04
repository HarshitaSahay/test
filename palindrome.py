def is_palindrome(original):
    rev = ''
    for i in original:
        rev = i + rev
    if rev == original:
        return  True
    else:
        return False

while True:
    word = str(input("Enter a word: "))
    if is_palindrome(word):
        print(word, " is palindrome.")
    else:
        print(word, " is not palindrome")
    option = input("Want to continue? Y/N: ")
    if option == 'Y' or option == 'y':
        continue
    else:
        break