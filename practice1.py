def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(len(prefix)):
        char = prefix[i]
        for word in strs[1:]:
            if i > len(word) or char != word[i]:
                return prefix[:i]
    return ""


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
# longestCommonPrefix(strs)
