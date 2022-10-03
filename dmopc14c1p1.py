n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

nums.sort()

mean = 0
if n % 2 == 1:
    mean = int((nums[n // 2]) + 0.5)
else:
    mean = int(((nums[(n // 2 - 1)] + nums[n // 2]) / 2) + 0.5)

print(mean)
