
total = 0.0
for i in range(1_000_000):
    term = ((-1)**i) / (2 * i + 1)
    total += term
result = total * 4
print(result)
