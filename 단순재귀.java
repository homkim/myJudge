/**
 * 단순재귀
 */
public class 단순재귀 {

    public static int NUM = 1001;
    public static long[] d = new long[NUM];

    private static long fibo(int x) {

        if(d[x] != 0) return d[x];
        else {
            d[x] = fibo(x-1) + fibo(x-2);
            return d[x];
        }
    }
    public static void main(String[] args) {
        for (int i = 0; i < NUM; i++) {
            d[i] = 0;
        }

        d[1] = d[2] = 1;
        System.out.println(fibo(50));
    }

}