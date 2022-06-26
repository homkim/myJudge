/**
 내림차순 전투력이 되게끔 하는 최소 열외 병사 수를 구하는 문제
 
 7
 15 11 4 8 5 2 4
 */

import java.util.*;
public class 병사배치하기 {
    static int n;
    static ArrayList<Integer> v = new ArrayList<Integer>();
    static int[] dp = new int[2000];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            v.add(sc.nextInt());
        }
        // 배열의 순서를 뒤집어 LIS로 푼다.
        Collections.reverse(v);
        for (int i = 0; i < n; i++) dp[i] = 1;
        for (int i = 1; i < n; i++) 
            for(int j = 0; j < i; j++)
                if(v.get(i) > v.get(j)) dp[i] = Math.max(dp[i], dp[j] + 1);
        int max = 0;
        for(int i = 0; i < n; i++) max = Math.max(max, dp[i]);
        System.out.println(n-max);

    }
    
}