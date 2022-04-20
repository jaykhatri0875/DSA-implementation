
'''arr = [1,5,5,5,6,7,7,8]

ans = []
curr_sum = 0

for ele in arr:
    curr_sum = curr_sum+ele
    ans.append(curr_sum)

print(ans)'''

'''Python: In a string of only lowercase charachters, 
count the occurrence of vowels and print the index of all the occurences for the vowel which occurred maximum number of time. 
If the two or more vowels occurred same number of tie, print the vowel whose ascii value is less. 

str = 'aaabbabbbssscxciioo'


1. for each ele -> if its in vowel(a,e,i,o,u), keep increase that count
2. find max count of of vowel_count
3  for max_count vowel, get index and append in list,

    '''

def ch(s):
    l = len(s)
    v = ''
    for index in range(l):
        v = s[index]
        print(v)
print(ch('ABCA'))