class Solution {

    public void nextPermutation(int[] nums) {
        if (nums.length < 2) return;

        int firstDecreasing = -1;

        for (int i = nums.length-2;i>= 0;i--){
            if (nums[i] < nums[i+1]){
                firstDecreasing = i;
                break;
            }
        }

        if (firstDecreasing != -1){
            int temp = -1;

            for(int i = firstDecreasing+1;i<nums.length;i++){
                if(nums[i] > nums[firstDecreasing]){
                    temp = temp != -1 && nums[temp] < nums[i]? temp:i;

                }
                else{
                    break;
                }
            }

            int current = nums[temp];
            nums[temp] = nums[firstDecreasing];
            nums[firstDecreasing] = current;
        }

        int index = firstDecreasing+1;
        
        int left = index;
        int right = nums.length-1;
        int temp;
        
        while(left<right){
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left = left+1;
            right = right-1;
        }
        
        
    }
}
