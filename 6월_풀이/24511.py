# queuestack.py
from collections import deque

# 기존 큐스택 리스트
n = int(input())
# 큐면 0이고 뒤로 추가 앞으로 나감, 스택 1이고 뒤로 추가 뒤로 나감
queue_stack_type = list(map(int,input().split()))
# 원래 있던 숫자들
queue_stack_numbers = list(map(int,input().split()))
queue = deque([queue_stack_numbers[i] for i in range(n) if queue_stack_type[i] == 0])

# 넣을 큐스택 리스트
m = int(input())
# 넣을 숫자들
push_numbers = list(map(int,input().split()))

result = []
# queue_numbers에 queue로만 진행하면됨
# queue랑 stack이랑 합치면 queue가 되다니 신기하다.
for i in push_numbers:
    queue.appendleft(i)
    result.append(queue.pop())
    
print(*result)