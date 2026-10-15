# Input: upper limit
n = 10  
total_sum = 0

# Loop from 1 to n
for i in range(1, n + 1):
    total_sum += i

print(f"The sum of natural numbers up to {n} is: {total_sum}")

n = 5  
factorial = 1

# Loop to multiply numbers
for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is: {factorial}")

num = 153  
temp = num
num_digits = len(str(num))
armstrong_sum = 0

# Loop to extract digits and calculate power sum
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10

# Check if the sum matches the original number
if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")