def draw_square(size, symbol, filled):
    for i in range(size):
        if filled:
            print(symbol * size)
        else:
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + '' * (size - 2) + symbol)

draw_square(5, '***', True)
print()
draw_square(5, '***', False)