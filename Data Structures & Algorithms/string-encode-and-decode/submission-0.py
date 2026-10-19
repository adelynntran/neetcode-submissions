class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        j = i
        result = []
        while i < len(s):
            j = i
            while s[j] != "#": #move j until hit "#"
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + length + 1])
            i = j + length + 1
        return result

            

