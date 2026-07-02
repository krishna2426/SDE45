
class Solution(object):
    def compareVersion(self, version1, version2):
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        len1 = len(version1_list)
        len2 = len(version2_list)

        for i in range(max(len1,len2)):
            i1 = int(version1_list[i]) if i < len1 else 0
            i2 = int(version2_list[i]) if i < len2 else 0

            if i1 != i2:
                return 1 if i1> i2 else -1
        return 0 

class Solution(object):
    def isAnagram(self, s, t):
        #3rd solution 
        return sorted(s) == sorted(t)

        #2nd solution using Counter
        return Counter(s) == Counter(t)

       #1st solution  
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True


class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for i in range(1,n):
            current = res[0]
            count = 1
            newdata= ""
            for c in res[1:]:
                if c == current:
                    count+=1
                else:
                    newdata = newdata + str(count)+ current
                    current = c
                    count = 1
            res = newdata + str(count) + current
        return res
        
        