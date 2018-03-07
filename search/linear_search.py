def search(arr, target):
	# Grab index and value
	for index, val in enumerate(arr):
		# If we find our target
		if val == target:
			# Return index
			return index
	# Otherwise, return False
	return False 			
