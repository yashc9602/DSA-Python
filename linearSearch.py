def locate(nums, ele):
    pos = 0
    while True:
        if nums[pos] == ele:
            return pos
        pos += 1

        if pos == len(nums):
            return -1


n = int(input("Enter the number of digits"))
nums = []

for i in range(n):
    ele = int(input())
    nums.append(ele)

ele = int(input("Enter the number to be found"))

res = locate(nums, ele)
print(f"The position is {res}")