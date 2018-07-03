
def quick_sort(arr, start_index, end_index)
  if start_index < end_index
    partition_index = partition(arr, start_index, end_index)

    quick_sort(arr, start_index, partition_index - 1)
    quick_sort(arr, partition_index + 1, end_index)
  end
  arr
end

def partition(arr, start_index, end_index)
  partition_index = start_index
  partition_value = arr[end_index]

  start_index.upto(end_index - 1) do |index|
    if partition_value >= arr[index]
      arr[index], arr[partition_index] = arr[partition_index], arr[index]
      partition_index += 1
    end
  end
  arr[end_index], arr[partition_index] = arr[partition_index], arr[end_index]
  partition_index
end
