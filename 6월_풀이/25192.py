n = int(input())
login = set()
nums = 0

for i in range(n):
    a = input()
    if a != "ENTER":
        login.add(a)
    else:
        nums += len(login)
        login.clear()
        
nums += len(login)

print(nums)