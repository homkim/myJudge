'''
7
15 11 4 8 5 2 4

뒤집어서 LIS 로 푼다
7
4 2 5 8 4 11 15
'''

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n # DP 테이블을 1로 초기화

# 가장 긴 증가하는 부분 수열(LIS: Longest Increasing Sequence) 알고리즘 적용
for i in range(1,n):  # 현재 체크하려는 원소
    for j in range(0, i):  # 현재 원소와 비교하여 체크하여야 하는 이전 원소
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))