# 정수 n, m 입력 받기
n,m=map(int, input().split())

# N개의 화폐 단위 정보 입력받기
arr = []
for i in range(n):
    arr.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d= [10001]*(m+1)

# 0을 만드는 방법은 0개가 있다고 가정. 다음 스텝에서 사용하기 위함
d[0] = 0;

for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != 10001: # (i-k) 원을 만드는 방법이 존재하면
            d[j] = min(d[j], d[j-arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])