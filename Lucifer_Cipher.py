x= [x for x in range(1,27)]
z="abcdefghijklmnopqrstuvwxyz"
dic={z[i-1]:x[i-1] for i in range(1,27)}

def inp():
	s=input()
	if(len(s)<=10):
		return s.lower()
	else:
		inp()
	
def chpal(a):
	x=a
	y=[x[len(x)-i] for i in range(1,len(x)+1)]
	x=list(x)
	if(x==y):
		print("Palindrome")
	else:
		m=1
		for i in a:
			k=dic[i]
			m*=k
		print(m)
s=inp()
s=chpal(s)




