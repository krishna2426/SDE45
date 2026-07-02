#reverse words
class Solution(object):
    def reverseWords(self, s):
        k = s.split()
        left, right = 0, len(k)-1
        while(left <=right):
            k[left], k[right] = k[right], k[left]
            left +=1
            right -= 1
        result_string = " ".join(k)

        return result_string


#longest palindromic substring 
    def longestPalindrome(self, s):
       res = ""
       resLen = 0

       for i in range(len(s)):
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            #even length palindrome
            l,r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
       return res

#roman to integer 

    def romanToInt(self, s):
        #largest to smallest - add them up
        #SMALLEer before the larger - subtract them
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
        
