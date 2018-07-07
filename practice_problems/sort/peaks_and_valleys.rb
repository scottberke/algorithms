
def peaks_and_valleys(arr)
  (1..(arr.size - 1)).step(2) do | index|
    max_index = index

    (index - 1..index + 1).each do |sub_index|
      if sub_index < arr.size && arr[sub_index] > arr[max_index]
        max_index = sub_index
      end
    end

    arr[index], arr[max_index] = arr[max_index], arr[index]
  end

  arr
end
