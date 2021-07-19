import sys

string_a = sys.stdin.readline().strip().upper()
string_b = sys.stdin.readline().strip().upper()
len_a = len(string_a)
len_b = len(string_b)
table = [[0] * (len_b + 1) for _ in range(len_a + 1)] 

for i in range(1, len_a + 1): 
    for j in range(1, len_b + 1): 
        if string_a[i - 1] == string_b[j - 1]: 
            table[i][j] = table[i - 1][j - 1] + 1 
        else: table[i][j] = max(table[i - 1][j], table[i][j - 1])
        
print(table[-1][-1])