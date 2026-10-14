class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort the input into groups dictionary
        groups = {}

        # grab the common key among anagrams
        for word in strs:
            key = ''.join(sorted(word))
        
            if key not in groups:
                groups[key] = []
        
            #else
            groups[key].append(word) #add word to current key
        
        return list(groups.values())

        

        