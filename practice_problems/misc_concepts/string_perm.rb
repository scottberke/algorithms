

def string_perm(string, result: [], base: '')
  if string.empty?
    result << base
  end

  string.each_char.with_index do |char, index|
    remaining_string = string[0...index] + string[index + 1..-1]
    new_base = base + char
    string_perm(remaining_string, result: result, base: new_base)
  end
  result
end
