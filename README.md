# Python Practice Solutions: Loops

Three beginner Python programs that use loops. Each one has a hard-coded input at the top, so you can change the value and run it again.

## Programs

### 1. Sum of Natural Numbers using a for loop
Adds up all integers from 1 to `n`.

- **Input:** `n = 10`
- **How it works:** A `for` loop over `range(1, n + 1)` adds each number to `total_sum`.
- **Output:** `The sum of natural numbers up to 10 is: 55`

### 2. Factorial of a number using a loop
Multiplies all positive integers from 1 up to `n`.

- **Input:** `n = 5`
- **How it works:** `factorial` starts at 1, and a `for` loop multiplies it by each number from 1 to `n`.
- **Output:** `The factorial of 5 is: 120`

### 3. Armstrong number check using a loop
Checks whether a number equals the sum of its digits, each raised to the power of the number of digits.

- **Input:** `num = 153`
- **How it works:** A `while` loop pulls out each digit with `% 10`, raises it to the power of the digit count, adds it to `armstrong_sum`, then drops the digit with `// 10`. The sum is compared with the original number.
- **Output:** `153 is an Armstrong number.`
- **Why 153 qualifies:** 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

## Concepts Covered

- `for` loops with `range()`
- `while` loops
- Accumulator variables
- Modulo (`%`) and floor division (`//`)
- f-strings for output

## Running

Requires Python 3.6 or newer (f-strings). Save a program to a file and run:

```
python program.py
```

To try other values, change the input variable at the top of the program (`n` or `num`).
