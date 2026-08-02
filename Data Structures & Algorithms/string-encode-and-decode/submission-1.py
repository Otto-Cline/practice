class Solution:

# ["he", "wo"]
    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        print(s)
        return s
        
# "2#he2#wo"
    def decode(self, s: str) -> List[str]:
        array = []
        i=0
        while i < len(s):
            num_of_chars = ""
            while s[i] != "#":
                num_of_chars += str(s[i])
                i+= 1
            num_of_chars = int(num_of_chars)

            j=0
            word = ""
            while j < num_of_chars:
                j+=1
                i+=1
                word += s[i]
            i+=1
            array.append(word)
            word = ""
        return array

    