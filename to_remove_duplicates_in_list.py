numbers=[1,23,5,5,5,55,55,55,55,55,45,67,3,4,34,34,34,35]
count=1
for number in numbers:
    for i in range(numbers.count(number)-1):
        if numbers.count(number) > count:
            numbers.remove(number)
print(numbers)
