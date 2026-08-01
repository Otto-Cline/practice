class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:

            letters = [0] * 26

            for char in word:
                letters[ord(char) - ord("a")] += 1
            
            letters_tuple = tuple(letters)

            if letters_tuple not in seen:
                seen[letters_tuple] = []
            
            seen[letters_tuple].append(word)

        return list(seen.values())

