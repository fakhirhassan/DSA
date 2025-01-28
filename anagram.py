s= "anagram"
t= "nagaram"
# def isAnagram(s,t):
#     if len(s)!=len(t):
#         return False
#     hashsetS = {} 
#     hashsetT = {}
#     for i in range(len(s)):
#         hashsetS[s[i]] = hashsetS.get(s[i],0)+1
#         hashsetT[t[i]] = hashsetT.get(t[i],0)+1
#     for c in hashsetS:
#         if c not in hashsetT or hashsetT[c]!=hashsetS[c]:
#             return False
#     return True
# print(isAnagram(s,t))
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    sortedS = sorted(s)
    sortedT = sorted(t)
    for i in range(len(sortedS)):
        if sortedS[i]!=sortedT[i]:
            return False
    return True
print(isAnagram(s,t))
