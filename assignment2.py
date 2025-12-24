#task1

num = int(input('enter the number'))
print(f'{num} is a even number') if num % 2 ==0 else print(f'{num} is a odd number.')


#tasks 2
sum = 0

for i in range(1, 51):
    sum = sum + i

print("Sum of integers from 1 to 50 is:", sum)
