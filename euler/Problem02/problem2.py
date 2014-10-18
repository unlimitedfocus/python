fibonacci_sequence = [1, 2]

while True:
    num = sum(fibonacci_sequence[-2:])
    if 4000000 < num:
        break
    fibonacci_sequence.append(num)

print sum(filter(lambda x: x % 2 == 0, fibonacci_sequence), 0)

