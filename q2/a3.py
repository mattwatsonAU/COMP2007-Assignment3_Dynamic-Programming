n = int(input())
T = list(map(float, input().strip().split()))


optim_inc = [0] * n
optim_exc = [0] * n
soln=0.0
i=n-1
for _ in range(n):
	left_coord = 2*i+1
	right_coord = 2*i+2
	if(left_coord>(n-1)) or (right_coord>(n-1)):
		optim_inc[i] = T[i]
		optim_exc[i] = 0
	else:
		optim_exc[i] = max(optim_inc[left_coord],optim_exc[left_coord]) + max(optim_inc[right_coord],optim_exc[right_coord])
		optim_inc[i] = T[i] + optim_exc[left_coord] + optim_exc[right_coord]
	i=i-1
soln = max(optim_exc[0],optim_inc[0])
print('{:.2f}'.format(soln))