
def merge_sort(arr, start_index, end_index)

  if start_index < end_index
   mid_index = (start_index + end_index) / 2

   merge_sort(arr, start_index, mid_index)
   merge_sort(arr, mid_index + 1, end_index)
   merge(arr, start_index, mid_index, end_index)
  end

  arr
end

def merge(arr, start_index, mid_index, end_index)
  temp = arr.clone
  first_half_index = start_index
  second_half_index = mid_index + 1
  current = first_half_index

  while first_half_index <= mid_index && second_half_index <= end_index
    if temp[first_half_index] < temp[second_half_index]
      arr[current] = temp[first_half_index]
      first_half_index += 1
    else
      arr[current] = temp[second_half_index]
      second_half_index += 1
    end
    current += 1
  end

  first_half_index.upto(mid_index) do |index|

    arr[current] = temp[index]
    current += 1
  end

end
