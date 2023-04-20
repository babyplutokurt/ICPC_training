def findLongestPalindromicSubstring(s: str) -> str:
    """Given a string, find the longest palindromic substring in it.

    Args:
        s (str): A string.

    Returns:
        str: The longest palindromic substring of s.
    """
    # TODO: Write your code here
    # odd
    res = s[0]
    for i in range(len(s)):
        expand = 1
        while i - expand >= 0 and i + expand <= len(s) - 1:
            if s[i - expand] == s[i + expand]:
                res = max(res, s[i - expand: i + expand + 1], key=lambda x: len(x))
                expand += 1
            else:
                break
    # even
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            res = max(res, s[i - 1: i + 1], key=lambda x: len(x))
            expand = 1
            while i + expand < len(s) and i - 1 - expand >= 0:
                if s[i - 1 - expand] == s[i + expand]:
                    res = max(res, s[i - 1 - expand: i + expand + 1], key=lambda x: len(x))
                    expand += 1
                else:
                    break
    return res


print(findLongestPalindromicSubstring('aabc'))
