class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt = {}

        for i in range(len(s)):
            if s[i] in dictt:
                dictt[s[i]] +=1
            else:
                dictt[s[i]] = 1


        dicttt = {}

        for i in range(len(t)):
            if t[i] in dicttt:
                dicttt[t[i]] +=1
            else:
                dicttt[t[i]] = 1

        return dictt == dicttt
