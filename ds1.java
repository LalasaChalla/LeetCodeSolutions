import java.util.HashMap;
import java.util.Scanner;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>(); // value -> index
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        
        return new int[] {-1, -1}; // no solution found
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = 10;

        int[] arr = new int[n];
        System.out.println("Enter " + n + " elements:");
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        System.out.print("Enter target value: ");
        int target = sc.nextInt();

        Solution sol = new Solution();
        int[] result = sol.twoSum(arr, target);
        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}
