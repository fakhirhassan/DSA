nums = [1,2,3,4]
# for i in range(len(nums)):
#     product = 1
#     for j in range(len(nums)):
#         if i != j:
#             product *= nums[j]
#     print(product)
# optimal approach
n = len(nums)

prefix = [1] * n
suffix = [1] * n
ans = [1] * n

for i in range(1, n):
    prefix[i] = prefix[i-1] * nums[i-1]
for i in range(n-2, -1, -1):
    suffix[i] = suffix[i+1] * nums[i+1]
for i in range(n):
    ans[i] = prefix[i] * suffix[i]

print(ans)