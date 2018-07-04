BASE = 10

def radix_sort(arr)
  max = arr.max
  power = 0

  while true
    buckets = Array.new(BASE) { [] }

    arr.each do |num|
      place = BASE**power

      digit = (num / place) % BASE
      buckets[digit].push(num)
    end

    arr = buckets.flatten!

    return arr if BASE**power >= max

    power += 1
  end
end
