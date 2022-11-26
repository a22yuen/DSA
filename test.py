# function that takes in 2 parameters and returns the sum of those 2 parameters

# for loop through array in reverse and print even number

# declare list from 1 to 20
arr = [x for x in range(1, 21)]

for i in range(len(arr)-1, -1, -1):
    if arr[i] % 2 == 0:
        print(arr[i])
