#creating a funtion

def func1():
	print("hii")



func1()
#with parameters
def func2(a):
	print("hii"+a)

func2("nizzu")


#with 2 parameters
def func3(a,b):
	c=a+b
	print(c)
func3(2,7)


#with 2/3 parameters
def func3(a,b,c):
	d=a+b+c
	print(d)
func3(2,7,3)


#with default parameter
def func4(university="IITB"):
	print("Iam in" + "\t" + university)
func4("IITG")
func4("IITD")
func4()

#calling one function from other

def func5(a,b):
	print("hii other function")
	c=a+b
	return c
def func6():
	print("hellloo,iam going to call other function")
	s=func5(2,7)
	print("addition is",s)
func6()