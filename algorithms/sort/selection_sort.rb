
def selection_sort(arr)
  0.upto(arr.size - 1) do |smallest_index|
    start = smallest_index + 1

    start.upto(arr.size - 1) do |index|
      if arr[index] <= arr[smallest_index]
        arr[index], arr[smallest_index] = arr[smallest_index], arr[index]
      end
    end
  end

  arr
end
