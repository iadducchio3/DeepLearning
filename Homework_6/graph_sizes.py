
def print_to_file(label,value):
	f = open("sizes.txt","a+")
	sb = label + str(value) + '\n'
	f.write(sb)
	f.close()