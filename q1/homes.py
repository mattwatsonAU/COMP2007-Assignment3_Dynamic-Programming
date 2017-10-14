def max_value(house_values, num_houses):
	
	# O(1)
	if num_houses == 0:
		return 0
	
	# O(1)
	if num_houses == 1:
		return house_values[0]
	
	# O(1) to run max operation
	if num_houses == 2:
		return max(house_values[0],house_values[1])

	curr_max_value = [0]*num_houses
	curr_max_value[0] = house_values[0]
	curr_max_value[1] = max(house_values[0],house_values[1])

	# O(N)
	for i in range(2,num_houses):
		curr_max_value[i] = max(house_values[i] + curr_max_value[i-2], curr_max_value[i-1])
		print(curr_max_value)
	
	# return the last value in the curr_max_value array as our result (called using index '-1')

	return curr_max_value[-1]


def main():
	n = int(input())
	house_values = []
	for _ in range(n):
		h = int(input())
		house_values.append(h)

	num_houses = len(house_values)
	max_val = max_value(house_values,num_houses)
	print("Maximum value:", max_val)

if __name__ == '__main__':
    main()