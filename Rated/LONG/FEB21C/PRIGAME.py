

t = int(input())
for _ in range(t):
	x, y = map(int, input().strip().split())
	if y == 1:
		if x == 1 or x == 2:
			print('Chef')
		else:
			print('Divyam')
	else:
		if(primeless(x) <= y):
			print("Chef")
		else:
			print("Divyam")
