

def triple_step(stairs, memo: nil)
  memo = { 1 => 1, 2 => 2, 3 => 4 } if memo.nil?

  if memo.keys.include?(stairs)
    return memo[stairs]
  end

  memo[stairs] = triple_step(stairs - 1, memo: memo) + triple_step(stairs - 2, memo: memo) + triple_step(stairs - 3, memo: memo)

  memo[stairs]
end
