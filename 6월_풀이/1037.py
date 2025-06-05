# 그냥 가장 큰 수와 가장 작은 수 곱하면 되네?

N = int(input())
진짜_약수들 = sorted(list(map(int, input().split())), reverse=True)
print(진짜_약수들[0] * 진짜_약수들[-1])

