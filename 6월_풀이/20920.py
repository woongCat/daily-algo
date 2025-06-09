# 자주 나오는 단어 -> dict
# 길수록 -> len
# 알파벳 순서 -> sorted

# 길이가 M 이상인 단어만 외움

N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
            
sorted_words = sorted(
    words.items(),
    key = lambda x : (-x[1], -len(x[0]), x[0])
)

for word, count in sorted_words:
    print(word)
