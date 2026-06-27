
total = 0
num_terms = 1_000_000

for i in range(num_terms):
    term = 1 / (2 * i + 1)
    if i % 2 == 0:
        total += term
    else:
        total -= term

result = total * 4
print(result)
