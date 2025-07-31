import java.util.*;

class Solution {
    public static int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2]; 
        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int currSum = nums[i] + nums[left] + nums[right];

                if (Math.abs(currSum - target) < Math.abs(closestSum - target)) {
                    closestSum = currSum;
                }

                if (currSum == target) {
                    return currSum; 
                } else if (currSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return closestSum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] input = sc.nextLine().split(" ");
        int[] nums = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            nums[i] = Integer.parseInt(input[i]);
        }

        int target = sc.nextInt();

        int result = threeSumClosest(nums, target);
        System.out.println(result);
    }
}
