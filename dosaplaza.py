import copy
import math

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest][1] < arr[left][1]:
        largest = left

    if right < n and arr[largest][1] < arr[right][1]:
        largest = right

    if largest != i:
        arr[i][1], arr[largest][1] = arr[largest][1], arr[i][1]
        arr[i][0], arr[largest][0] = arr[largest][0], arr[i][0]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i][1], arr[0][1] = arr[0][1], arr[i][1]
        arr[i][0], arr[0][0] = arr[0][0], arr[i][0]
        heapify(arr, i, 0)

""" File Handling """

with open("inputPS10.txt", "r") as file:
    readline = file.read().splitlines()

n = int(readline[0])
row = []
arr = []

for line in readline:
    row.append(line.split(" "))
    
removed_element = row.pop(0)

for i in range(n):
    conv_int = [int(item) for item in row[i]]
            
    arr.append(conv_int)

""" File Handling """

# arr = [[0,3], [1,9], [2,6]]
cust_arr = copy.deepcopy(arr)
time_sum = 0
wait_time = 0

heapSort(arr)
# n = len(arr)

pos_arr = [0]*n

print("Input List : ")
print(cust_arr)
print("Sorted List : ")
print(arr)

for i in range(n):
    time_sum += arr[i][1]
    int_time = time_sum - arr[i][0]
    wait_time += int_time
    
line1 = "Minimum average waiting time : " + str(math.floor(wait_time/n))
print(line1)

line2 = "Dosas should be served in the following order :"
print(line2)

with open("outputPS10.txt", "w") as op_file:
    op_file.write('{}\n{}\n'.format(line1,line2))
    
    for i in range(n):
        pos_arr[i] = cust_arr.index(arr[i])
        line3 = "Customer " + str(pos_arr[i])
        print(line3)
        op_file.write('{}\n'.format(line3))
