class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for this problem we need to use two pointers
        # so in my mind I am thinking where should i put the two pointers and how should
        # i iterate them both to get the target
        # my constraints in this problem is that I must have a space comp O(1), 
        # index1 < index2 and index1 != index2. Obv index1 + index2 = target
        # so if i cycle through the array at most length - 1 times then I will find the sol
        # so if i start my right pointer at the end then cycle till i reach left 
        # check for all constraints if they are not met then
        # make left++ and start right again till left
        # do this until find sol
        # the problem i am struggling with is how do i actually make the right loop start again
        # with a different end
        # what are my solutions to this
        # well we would truly be cycling length - 1 + length - 2 + length - 3,
        # where this continues till length = 2
        # what if i made a while loop instead
        # i make it equal to a true boolean value, it exits if loops through all combintaions 
        # and if no solutions found then returns false
        left = 0
        right = len(numbers) - 1
        while(True):
            if((numbers[right] + numbers[left] == target) and (right + 1!= left + 1) and (left + 1< right + 1)):
                solution = [left + 1, right + 1]
                return solution
            else:
                if(right == left):
                    if(left + 1 == len(numbers) - 1):
                        break;
                    else:
                        right = len(numbers) - 1
                        left += 1
                else:
                    right -= 1
