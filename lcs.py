# Recursive solution to find the length of the longest common subsequence between two strings
def lcs(list1, list2, len1=0, len2=0):
    # if the given lengths match the lengths of the lists, that means we have reached the end of one of the lists, and there's no common subsequence
    if len1 == len(list1) or len2 == len(list2):
        return 0
    # if one of the words match, the length of the longest common subsequence is at least 1. The function is called again with incremented indexes
    if list1[len1] == list2[len2]:
        return 1 + lcs(list1, list2, len1+1, len2+1)
    # if no match is found, return the maximum length subsequence of 2 function calls, with each call incrementing a different index
    else:
        return max(lcs(list1, list2, len1+1, len2), lcs(list1, list2, len1, len2+1))

def getLCSSim(data1, data2):
    sim = lcs(data1, data2) / len(data1) * 100
    return sim