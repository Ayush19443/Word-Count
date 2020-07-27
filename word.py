#%%
f=open("hadoop.txt","r")
string=f.read()
wordlist = string.split()
counts=dict()
for word in wordlist:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
for i in counts:
    print(i,' ',counts[i], 'times')
    



