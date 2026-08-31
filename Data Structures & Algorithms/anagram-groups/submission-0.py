class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We want to group all anagrams in an array and store all of those group within another array
        # we make to make a hashmap and the key is the list of key-value pairs of letters
        result = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(string)
            
        return list(result.values())


                
                
        