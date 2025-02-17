def length_of_longest_substring(s):
    char_index_map = {}
    start = 0
    max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# 예시 입력
s1 = "abcabcbb"
s2 = "bbbbb"

# 예시 출력
print(length_of_longest_substring(s1))  # 출력: 3
print(length_of_longest_substring(s2))  # 출력: 1