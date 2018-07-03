
def bubble_sort(arr)
  swapped = true

  while swapped
    swapped = false
    0.upto(arr.size - 2) do |index|
      comp_index = index + 1

      if arr[index] > arr[comp_index]
        arr[index], arr[comp_index] = arr[comp_index], arr[index]
        swapped = true
      end

    end
  end

  arr
end
