
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    total = 0
    for i in range(n):
        for j in range(i, n):
            if len(arr[i:j+1]) != 1:
                if len(set(arr[i:j+1])) != 1:
                    total += 1
    print(total)

# for sub 1, Ai of arr is multiple of 2
# works but O(high)

'''
for all powers of 2
>> 1|2|4|8
15
>> 1|2|2|4|8
15
>> 3|3
3

for | -> ans = sum of all unique in range

>> 1&2&4&8&32
0
>> 1&1&2&4&8
0
>> 1&1
1
>> 0&2
0

for & -> ans = 0, if every element not equal, else = element

for a subarray:
    if all elements not equal:
        true
    elsE:
        false

so made a 2-d list, [element of arr, ]
then subtract the "ouuurence in order" from total subarrays

number of sub arrays = n*n-1 // 2
'''