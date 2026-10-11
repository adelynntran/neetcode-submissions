class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # count the freq of chars in s, then subtract it with
        # those in t
        count = {} #dict
        for char in s:
            #get value of key 'char' then plus 1,
            #if char is not in count, assign ) then plus 1
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count:
                return False #doesnt appear in s => not valid anagram
            count[char] -= 1 #else, minus its freq by 1

            if count[char] < 0:
                return False #appears in t more than in s
        return True
