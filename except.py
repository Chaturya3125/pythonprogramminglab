try:
	l={1,2,3,6,8,9}
	a=len(1)
	if a>3:
	  raise NameError
	elif a<3:
	  raise TypeError

except NameError:
    print("no error")
except TypeError:
    print("error occured")
finally:
	print("Execution completed")


