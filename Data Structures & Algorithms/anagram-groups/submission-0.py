class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        #create the letter frequency count:
        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - ord('a')] += 1 #get the index of char then +1 the freq in count at that index
            
            key = tuple(counts) #tuple because its hashable
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word) #the word under current key that match counts freq patter
        
        return list(groups.values())

        
