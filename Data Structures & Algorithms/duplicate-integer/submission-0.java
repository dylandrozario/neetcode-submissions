
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numbersHashed = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(numbersHashed.contains(nums[i])){
                return true;
            }
            numbersHashed.add(nums[i]);
        }
        return false;
        
    }
}