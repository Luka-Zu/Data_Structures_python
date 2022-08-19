from re import X
from Dynamic_Array import Dynamic_Array

test_array = Dynamic_Array()
print(test_array.n, test_array.capacity, str(test_array.array) ) 

test_array.append(1)
test_array.append(2)
test_array.append(3)
test_array.insertAt(0,0)

for x in range(0,4):
    print(test_array[x])

test_array.delete()

for x in range(0,3):
    print(test_array[x])


test_array.removeAt(0)

for x in range(0,2):
    print(test_array[x])


