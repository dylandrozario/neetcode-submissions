class Solution:
    # So this problem wants me to give a list of strings to a single string and return that
    # with that new string i need to convert it back to the orginal list of strings
    # the first thought in my head to add the strings together and have an ' or something like that
    # when we decode it we can call a split function to make the string into an array
    # [] [] [] [] 
    # the problem we encounter is empty arrays and now that i think of it what if the separator
    # we use it actually in the array it self, then the split function will not work properly
    # 
    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return "empty"
        
        new_string = ""

        for i in range(len(strs)):
            if(i == len(strs) - 1):
                new_string += strs[i]
            else:
                new_string += strs[i] + "SEPERATE"

        return new_string

    def decode(self, s: str) -> List[str]:
        if(s == "empty"):
            return []
        
        return s.split("SEPERATE")