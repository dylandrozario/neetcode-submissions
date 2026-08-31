class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Lets create a structure that adds each num into it, if it not in it then it is created
        # if it is in it then we add to the count
        # finally we loop through the structure and compare what has the highest count via
        # if statements 
        # what data structure should we use
        # i am thinking arrays or hashmaps
        # maps seems better
        # what should be the key and value
        # the key should be the number itself in the array then the value should be the count
        # how should we aquire all of the numbers
        # use a for loop with len(list) then make an hashmap so that if it doesnt encounter 
        # the num then it adds it 
        # now we have to deal with finding k most frquent elements
        # we can create an array and store values in them
        # then we can index the k most frequent elements
        # then loop through map to find the key associated with them

        frequency_map = defaultdict(int)
        for i in range(len(nums)):
            frequency_map[nums[i]] += 1
        
        
        values = list(frequency_map.values())
        values.sort(reverse=True)
        values = values[0:k]

        result = list()

        for key in frequency_map.keys():
            if frequency_map[key] in values:
               result.append(key)

        return result
