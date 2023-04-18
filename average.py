import random

def average(numbers):

    if len(numbers) == 0:
        return None
    
    sumTotal = 0
    for x in numbers:
        sumTotal += x
    
    return sumTotal/len(numbers)

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0]) == 0

random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2