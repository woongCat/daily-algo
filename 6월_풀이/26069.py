n = int(input())
rainbow_dance = set()

# 시간 복잡도 O(n)
for i in range(n):
    a,b = input().split()
    if a == "ChongChong" or b == "ChongChong":
        rainbow_dance.add(a)
        rainbow_dance.add(b)
    elif a in rainbow_dance or b in rainbow_dance:
        rainbow_dance.add(a)
        rainbow_dance.add(b)

print(len(rainbow_dance))