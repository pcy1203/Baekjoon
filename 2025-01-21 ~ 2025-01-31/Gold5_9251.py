import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

lcs_list = [[0 for j in range(len(string2) + 1)] for i in range(len(string1) + 1)]
lcs_list[1][1] = int(string1[0] == string2[0])

for sum in range(3, len(string1) + len(string2) + 1):
    for len1 in range(1, min(sum + 2, len(string1) + 1)):
        len2 = sum - len1
        if len2 > len(string2) or len2 <= 0:
            continue
        # LCS[0 ~ i][0 ~ j] = 0  (i = 0, j = 0)
        #                   = LCS[0 ~ i-1][0 ~ j-1] + 1  (string1[i] = string2[j])
        #                   = max(LCS[0 ~ i-1][0 ~ j], LCS[0 ~ i][0 ~ j-1])  
        if string1[len1 - 1] == string2[len2 - 1]:
            lcs_list[len1][len2] = lcs_list[len1 - 1][len2 - 1] + 1
        else:
            lcs_list[len1][len2] = max(lcs_list[len1 - 1][len2], lcs_list[len1][len2 - 1])

print(lcs_list[len(string1)][len(string2)])