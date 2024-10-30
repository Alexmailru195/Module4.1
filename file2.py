def print_even_numbers(start, end):
    if start > end:
        start, end = end, start
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    print("Четные числа между", start, "и", end, "|", even_numbers)

print_even_numbers(5, 15)