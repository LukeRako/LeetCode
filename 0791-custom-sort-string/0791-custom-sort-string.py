class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_map = {char: 0 for char in order}
        for char in s:
            if char in char_map:
                char_map[char] += 1
        
        sort_s =  ''
        for char in order:
            if char in char_map:
                sort_s += char * char_map[char]

        for char in s:
            if char not in order:
                sort_s += char

        return sort_s
            