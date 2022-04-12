def main():
	s = 0
	arr = input().split(' ')
	lst = [int(n) for n in arr]
	for x in range(0, lst[0]):
		xy = input().split(' ')
		if int(xy[0]) + int(xy[1]) >= lst[1]:
			s+=1
		xy = ""
	print(s)

if __name__ == '__main__':
	main() 
 