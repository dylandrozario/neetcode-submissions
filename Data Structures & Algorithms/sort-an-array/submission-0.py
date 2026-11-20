class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        # i am thinking of doing merge sort
        # so for this we need to find the midpoint
        # we can calculate by calling two merge methods on 0 to m and then m+1 to end
        # then calling a merge method at end
        # the question is how do we build these methods
        def merge(arr, l, m, r):
            left, right = arr[l:m + 1], arr[m + 1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
            
        def mergeSort(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr,m+1, r)
            merge(arr, l, m, r)
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums


    