#best approach to find duolicate in an array
nums = [1,2,3,4,1]
hashset = set()
# for num in nums:
#     if num in hashset:
#         print("Duplicate found: ", num)
#     else:
#         hashset.add(num)

# #brute force
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
#             print("Duplicate found: ", nums[i])
#             break

# print(len(list(filter(lambda x: x%2==0, nums))))
# print(len(list(filter(lambda x: x%2!=0, nums))))
# print(nums)

# def is_subset(lst1, lst2):
#     # Your code goes here
#     if lst1 in lst2:
#         return True
#     else:
#         print(False)
        
#     pass
# print(is_subset([1, 2, 3],[1,2,3,4,5,6]))

