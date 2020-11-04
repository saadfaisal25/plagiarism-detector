# Recursive solution to find the length of the longest common subsequence between two strings
def lcs(str1, str2, len1=0, len2=0):
    if len1 == len(str1) or len2 == len(str2):
        return 0
    if str1[len1] == str2[len2]:
        return 1 + lcs(str1, str2, len1+1, len2+1)
    else:
        return max(lcs(str1, str2, len1+1, len2), lcs(str1, str2, len1, len2+1))

def getSimilarity(data1, data2):
    sim = []
    for i in data1:
        for j in data2:
            l1 = i.split()
            l2 = j.split()
            sim.append(lcs(l1, l2) / min(len(l1), len(l2)))
    
    return sim