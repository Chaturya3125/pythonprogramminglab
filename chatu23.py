import random
user=0
comp=0
l=["r","p","s"]
d={'r':'rock','p':'paper','s':'scissor'}
while True:
	#take input from user
	u=input("enter your choice,press n to discontinue")
	#to exit
	if u=='n':
		print("Game over")
		print("user score is:",user)
		print("computer score is:",comp)
		exit()
	#input from computer
	c=random.choice(l)
	print ("computer chooses",d[c])
	print("user chooses",d[u])

	#compare the user and computer choice
	if u == c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")
		comp=comp+1
	elif u== 'r' and c =='s':
		print("user wins")
		user=user+1
	elif u=="s" and c=="r":
		print("comp wins")
		comp=comp+1
	elif u=="s" and c=='p':
		print("user wins")
		user=user+1
	elif u=="p" and c=="s":
		print("comp wins")
		comp=comp+1
	elif u=="p" and c=='r':
		print("user wins")
		user=user+1
