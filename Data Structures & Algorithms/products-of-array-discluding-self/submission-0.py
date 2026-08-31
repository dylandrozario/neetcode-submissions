class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we want to add elements except the one we are on
        # then we make sure that it fits a 32-bit integer
        # im not sure what this means but i will worry about the product part first
        # I want to make a default map, and and make the key index of the element and value
        # the product of the other elements
        # We will achieve this first part by making a for loop
        # the problem i just realized is that since it is not ordered then we cannot simply
        # search 
        # i just had another idea
        # what if we still use a default hashmap and the element we ignore index as the key
        # then then we check if that element is the ignore index then add all of the other 
        # elements and make it the value 
        # i just stumbled on another problem is that how do i skip, also i need a double for loop
        # there got to more of an efficient way
        # 
        
        output = [];
        for i in range(len(nums)):
            num = 1;
            for j in range(len(nums)):
                if(j != i):
                    num *= nums[j]
            output.append(num)
        

        return output
        
