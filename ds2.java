class Solution {
    public static int maxArea(int[] height) {
       int i = 0, j = height.length - 1;
    int max = 0;

    while (i < j) {
        int area = Math.min(height[i], height[j]) * (j - i);
        max = Math.max(max, area);
        if (height[i] < height[j]) {
            i++;
        } else {
            j--;
        }
    }

    return max; 
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String[] input=sc.nextLine().split(" ");
        int[] height=new int[input.length];
        for (int i = 0; i < input.length; i++) {
            height[i] = Integer.parseInt(input[i]);
        }
        int result=maxArea(height);
        System.out.println(result);
    }
}
