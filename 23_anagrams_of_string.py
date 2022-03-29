# check whether or not two strings are anagram of each other or not , different methods

# naviely we can sort both strings and match, but dont do it , its gonna take nlogn
# use dictionary of characters
def ditit(string):
    sd = {}
    for char in string:
        if(char in sd.keys()):
            sd[char] += 1
        else:
            sd[char] = 1
    return sd

def anagrams(str1,str2):
    sd1 = ditit(str1)
    sd2 = ditit(str2)
    print(sd1,sd2)
    return sd1==sd2

if __name__ == "__main__":
    print(anagrams('ababababacssafg','ababababacssagf'))