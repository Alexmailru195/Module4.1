def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

print("Число 123321 является палиндромом?", is_palindrome(123321))
print("Число 421987 является палиндромом?", is_palindrome(421987))