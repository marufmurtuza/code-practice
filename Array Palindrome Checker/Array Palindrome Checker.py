def palindromechecker(arr, n):

	check = 0
	i = 0
	while (i <= n // 2 and n != 0):


		if (arr[i] != arr[n - i - 1]):
			check = 1;
			break;
		i += 1;

	if (check == 1):
		print("False")
	else:
		print("True")


arr = [30,20,10,0,0,0,10,20,30]
n = len(arr)

palindromechecker(arr, n)
