s=input("enter a word: ")
t=input("enter a word: ")
def check_anagram(s,t):
	counterS={}
	counterT={}
	#returnsorted(s)==sorted(t)
#result=check_anagram(s,t)
#print(result)
	if len(s)!=len(t):
		return False
	for letter in s:
		if letter in counterS:
			counterS[letter]=counterS[letter]+1
		else:
			counterS[letter]=1
	for letter in t:
		if letter in counterT:
			counterT[letter]=counterT[letter]+1
		else:
			counterT[letter]=1
	return counterS==counterT
	#for key in counterS:
		#if not key in counterT:
			#return False
		#if not counterS[key]== counterT[key]:
			#return False
		#else:
			#return True
result= check_anagram(s,t) 
print(result)
