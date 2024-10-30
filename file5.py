def product_in_range(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product

print("Произведение чисел от 1 до 5:", product_in_range(1, 5))