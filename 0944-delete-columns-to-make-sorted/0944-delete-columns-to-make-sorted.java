class Solution {
    public static int minDeletionSize(String[] strs) {
        int k=0;
        int l = strs.length;
        for (int i = 0; i < strs[0].length(); i++) {
            for (int j = 0; j <l-1 ; j++) {
                if((int)strs[j].charAt(i)>(int)strs[j+1].charAt(i))
                {
                    k++;
                    break;
                }
            }
        }
        return k;
    }
}