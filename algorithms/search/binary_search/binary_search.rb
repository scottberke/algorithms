

def binary_search(data, target, low, high)
  return nil if low > high

  mid = (low + high) / 2

  if data[mid] == target
    return mid
  elsif data[mid] < target
    binary_search(data, target, mid + 1, high )
  else
    binary_search(data, target, low, mid - 1)
  end
end


def binary_search_iterative(data, target)
  low = 0
  high = data.size - 1

  while low <= high
    mid = (low + high) / 2
    if data[mid] == target
      return mid
    elsif data[mid] < target
      low = mid + 1
    else
      high = mid
    end
  end
end
