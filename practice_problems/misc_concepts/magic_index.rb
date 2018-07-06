

def magic_index(arr)
  arr.each_with_index do |index, value|
    return index if index == value
  end

  nil
end
