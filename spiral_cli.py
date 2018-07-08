#Script to Print the ulam spiral in command line
import math
m = int(input("Please Enter the number :"))
n = m**2
#Now We generate Primes upto n using Sieve of Eratosthenes

nums = [1]*(n+1)
nums[0]=nums[1]=0
for i in range(2,int(math.sqrt(n))+1):
	if nums[i]==1:
		for j in range(i**2,n+1,i):
			nums[j]=0

def spiral_print(Primes,m):
	trow = 0
	brow = m-1
	lcol = 0
	rcol = m-1
	matrix = [[0]*m for i in range(m)]
	k = len(Primes)-1
	while k>0:
		#bottom row print
		for i in range(rcol,lcol-1,-1):
			matrix[brow][i] = Primes[k]
			k-=1
		brow-=1
		#left col print
		for i in range(brow,trow-1,-1):
			matrix[i][lcol] = Primes[k]
			k-=1
		lcol+=1
		#top row print
		for i in range(lcol,rcol+1):
			matrix[trow][i] = Primes[k]
			k-=1
		trow+=1
		#right col print
		for i in range(trow,brow+1):
			matrix[i][rcol] = Primes[k]
			k-=1
		rcol-=1

	for i in range(m):
		for j in range(m):
			if matrix[i][j]==1:
				print(".",end='')
			else:
				print(" ",end='')
		print()

spiral_print(nums,m)