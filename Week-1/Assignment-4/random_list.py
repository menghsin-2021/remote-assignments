import random


randomlist = []

for i in range(0,42):
	n = random.randint(1,100)
	randomlist.append(n)

sorted_randomlist = sorted(randomlist)

# test
print(sorted_randomlist)
