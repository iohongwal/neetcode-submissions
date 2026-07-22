class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            // if 1 & 1 = 1 then let 1 << 1 = 10  
            int tmp = (a & b) << 1;
            // 0 ^ 0 = 0, 1 ^ 1 = 0, 1 ^ 0 = 1
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}
