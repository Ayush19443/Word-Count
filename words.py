#%%
f=open("hadoop.txt","r")
string=f.read()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
for char in string:
   if char not in punctuations:
       no_punct = no_punct + char
wordlist = no_punct.split()
counts=dict()
for word in wordlist:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
for i in counts:
    print(i,' ',counts[i], 'times')
    






# %%
