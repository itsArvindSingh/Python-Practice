numbers=[1,23,34,35,46,5,76,876,9,6,3599,23,4,7,3,5,6]
biggest=numbers[0]
for number in numbers:
    if number>biggest:
        biggest=number
print(biggest)
