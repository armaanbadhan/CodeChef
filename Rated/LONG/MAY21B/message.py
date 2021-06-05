import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output2.txt", "w")

n = int(input())
for i in range(n):
	A = []
	D = []
	A.append(list(input()))
	D.append(A[0][0])
	D.append(A[0][1])
	D.append(A[0][2])
	A.append(list(input()))
	D.append(A[1][0])
	D.append(A[1][1])
	D.append(A[1][2])
	A.append(list(input()))
	D.append(A[2][0])
	D.append(A[2][1])
	D.append(A[2][2])
	X = D.count('X')
	O = D.count('O')
	ticktok = D.count('_')

	def diagonalX(a):
		c = 0
		if (a[0][0] == a[1][1] == a[2][2] and a[0][0] == "X") or ( a[0][2] == a[1][1] == a[2][0] and a[0][2] == "X"):
			c+= 1
		return c

	def diagonalO(a):
		c = 0
		if (a[0][0] == a[1][1] == a[2][2] and a[0][0] == "O" ) or (a[0][2] == a[1][1] == a[2][0] and a[0][2] == "O"):
			c+= 1
		return c

	def row1X(a):
		c = 0
		if (a[0] == ['X','X','X']):
			c+= 1
		return c
	def row1O(a):
		c = 0
		if (a[0] == ['O','O','O']):
			c+= 1
		return c

	def row2X(a):
		c = 0
		if (a[1] == ['X','X','X'] ):
			c+= 1
		return c

	def row2O(a):
		c = 0
		if (a[1] == ['O','O','O']):
			c+= 1
		return c


	def row3X(a):
		c = 0
		if (a[2] == ['X','X','X']):
			c+= 1
		return c

	def row3O(a):
		c = 0
		if (a[2] == ['O','O','O']):
			c+= 1
		return c

	def column1X(a):
		c = 0
		if (a[0][0] == a[1][0] == a[2][0] == 'X') :
			c+= 1
		return c
	def column1O(a):
		c = 0
		if (a[0][0] == a[1][0] == a[2][0] == 'O') :
			c+= 1
		return c

	def column2X(a):
		c = 0
		if (a[0][1] == a[1][1] == a[2][1] == 'X' ):
			c+= 1
		return c

	def column2O(a):
		c = 0
		if (a[0][1] == a[1][1] == a[2][1] == 'O'):
			c+= 1
		return c

	def column3X(a):
		c = 0
		if (a[0][2] == a[1][2] == a[2][2] == 'X') :
			c= 1
		return c

	def column3O(a):
		c = 0
		if (a[0][2] == a[1][2] == a[2][2] == 'O') :
			c= 1
		return c


	if diagonalX(A) or diagonalO(A) or row3O(A) or row3X(A) or row2X(A) or row2O(A) or row1O(A) or row1X(A) or column3O(A) or column3X(A) or column2O(A) or column2X(A) or column1O(A) or column1X(A) == 1:
		if diagonalX(A) + diagonalO(A) + row3O(A) + row3X(A) + row2X(A) + row2O(A) + row1O(A) + row1X(A) + column3O(A) + column3X(A) + column2O(A) + column2X(A) + column1O(A) + column1X(A) == 1:
			if column1O(A) or column2O(A) or column3O(A) or row1O(A) or row2O(A) or row3O(A) or diagonalO(A) == 1:
				if X == O:
					print("1")
				else:
					print("3")
					continue
			else:
				if X == O+1:
					print("1")
				else:
					print("3")
		elif column1X(A) + column2X(A) + column3X(A) + row1X(A) + row2X(A) + row3X(A) + diagonalX(A) == 2:
			if X - O == 1:
				print("1")
			else:
				print("3")
		else:
			print("3")
	elif X - O == 1 or X - O == 0:
		if ticktok>0:
			print('2')
		else:
			print(1)
	elif X - O == 1 and ticktok == 0:
		print('1')
	else:
		print("3")

'''
OOX
XXO
OXX
'''
