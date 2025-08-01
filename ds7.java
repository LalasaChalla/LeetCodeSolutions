import java.util.*;
class Solution {
    public static boolean isAnagram(String s, String t) {
        char[] char1 = s.toCharArray();
        Arrays.sort(char1);
        char[] char2 = t.toCharArray();
        Arrays.sort(char2);
        for (int i = 0; i < char1.length; i++) {
            if (char1[i] != char2[i]) {
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        String t=sc.nextLine();
        boolean result =isAnagram(s,t);
        System.out.println(result);
    }
}
