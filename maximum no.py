numbers=[50, 40, 23, 22,70, 56, 12, 5, 10, 7] 
i=0
count=0
while i<len(numbers):
    a=numbers[i]
    if a>20 and a<40:
        count=count+1
    i=i+1
print(count,)