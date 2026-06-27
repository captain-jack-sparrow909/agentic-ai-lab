```python
total = 0.0
for i in range(1_000_000):
    term = ((-1)**i) / (2 * i + 1)
    total += term
result = total * 4
print(result)
```I wrote a Python program named `series_calculator.py` to calculate the sum of the first 1,000,000 terms of the series 1 - 1/3 + 1/5 - 1/7 + ... and then multiplied the total by 4.

Here's the Python code I used:


I then executed this file in the sandbox.

The final result is:
3.1415916535897743
