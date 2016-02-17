from sys import stdin

inputs = []
answers = {}
largest = 0
done = {}

stdin.next()
for N in map(int, stdin):
	inputs.append(N)
	answers[N] = None
	if N > largest: largest = N

step = 5
while true:
	for A in answers:
		if A >= step:

			


for N in answers:
	ret = 0
	step = 5
	while N >= step:
		ret += N/step
		step *= 5
	answers[N] = ret

for N in inputs:
	print answers[N]
	
