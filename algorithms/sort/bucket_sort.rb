
def bucket_sort(arr)
  max = arr.max
  arr_size = arr.size
  buckets = Array.new(arr_size) { [] }

  arr.each do |element|
    bucket_index = element * arr_size / (max + 1)
    buckets[bucket_index].push(element)
  end

  buckets.flat_map do |bucket|
    bucket.sort
  end
end
