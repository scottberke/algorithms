

def linear_search(data, target)
  data.each_with_index do |item, index|
    return index if item == target
  end

  nil 
end
