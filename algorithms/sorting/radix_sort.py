from functools import reduce

# O(nk) where n is the size of the array and k is length of max integer
def radix_sort(arr):
    base = 10
    max_val = max(arr)
    power = 0

    # We'll loop until we've hit each digit of each number
    while True:
        # Create buckets for a base 10 number
        buckets = [ [] for i in range(base) ]
        # Go through our array of ints
        for num in arr:
            # Start with least significant digit and work up
            place = base**power
            # Isolate that digit
            digit = (num // place) % base
            # Add number to correct bucket
            buckets[digit].append(num)
        # Update array after each pass
        arr = reduce(lambda x, y: x + y, buckets)
        # Our arrays sorted if we reach a power of ten > max value
        if base**power >= max_val:
            return arr
        # Up our power for next iteration
        power += 1


def msd_radix_sort(arr, power):
    # Base case if we have arr length 1 or arr is all same digit
    if len(set(arr)) == 1:
        return arr

    # Create buckets for a base 10 number
    buckets = [ [] for i in range(10) ]
    for num in arr:
        # Start with most significant digit and work down
        place = 10**power
        # Isolate that digit
        digit = (num // place) % 10
        # Add number to correct bucket
        buckets[digit].append(num)

    # Sort each bucket with the next lowest significant digit
    buckets = [ msd_radix_sort(bucket, power - 1) for bucket in buckets if bucket ]
    # Return our concatenated buckets
    return reduce(lambda x, y: x + y, buckets, [])
