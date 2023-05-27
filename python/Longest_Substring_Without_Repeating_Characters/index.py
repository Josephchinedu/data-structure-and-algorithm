def lengthOfLongestSubstring(s: str) -> int:
    len_of_string = len(s)
    unique_set_of_strings = set()
    max_len = 0
    start = 0
    end = 0

    while end < len_of_string:

        if s[end] not in unique_set_of_strings:
            unique_set_of_strings.add(s[end])
            
            end += 1

            max_len = max(max_len, (end - start))
        
        else:
            unique_set_of_strings.remove(s[start])
            start += 1

        

    
    return max_len


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))