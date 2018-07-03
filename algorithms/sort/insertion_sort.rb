
def insertion_sort(arr)

  1.upto(arr.size - 1) do |index|
    sorted_end_index = index - 1

    sorted_end_index.downto(0) do |sorted_index|
      if arr[index] < arr[sorted_index]
        arr[index], arr[sorted_index] = arr[sorted_index], arr[index]
        index = sorted_index
      end
    end

  end

  arr
end
