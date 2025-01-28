#    brute force approach 
from collections import defaultdict
str = ["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagram(str):
    res = []
    for i in range(len(str)):
        if str[i] != "":
            temp = [str[i]]
            for j in range(i+1, len(str)):
                if sorted(str[i]) == sorted(str[j]):
                    temp.append(str[j])
                    str[j] = ""
            res.append(temp)
    return res
print(groupAnagram(str))

#   optimal approach

str = ["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagram(str):
    res = defaultdict(list)
    for s in str:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')]+=1
        res[tuple(count)].append(s)
    return list(res.values())
print(groupAnagram(str))
