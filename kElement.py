nums = [1,1,1,2,2,3]
k = 2
def kElement(nums,k):
    hashset = {}
    freq = [[]for i in range(len(nums)+1)]
    for n in nums:
        hashset[n] = hashset.get(n,0)+1
    for n , key in hashset.items():
        freq[key].append(n)
    res = []
    for i in range(len(freq)-1,0,-1):
        res+=freq[i]
        if len(res)>=k:
            break
    return res
print(kElement(nums,k))