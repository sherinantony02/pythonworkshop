x="sherin antony"
counter={}
for letter in x:
    if letter in counter:
       counter[letter]=counter[letter]+1
    else:
       counter[letter]=1
print(counter)
max=0
most=""
for letter in counter:
    if counter[letter]>max:
       max=counter[letter]
       most=letter
print(most)
