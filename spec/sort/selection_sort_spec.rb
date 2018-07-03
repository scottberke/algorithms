require 'spec_helper'

describe 'Selection Sort' do
  it 'sorts a simple array with even number of elements' do
    sorted_arr = [4, 3, 2, 1].sort!
    unsorted_arr = sorted_arr.clone.shuffle!

    expect(selection_sort(unsorted_arr)).to eq sorted_arr
  end

  it 'sorts a simple array with odd number of elements' do
    sorted_arr = [5, 4, 3, 2, 1].sort!
    unsorted_arr = sorted_arr.clone.shuffle!

    expect(selection_sort(unsorted_arr)).to eq sorted_arr
  end

  it 'sorts an array with arbitrary number of elements' do
    sorted_arr = Array.new(rand(100)) { rand(100) }
    sorted_arr.sort!
    unsorted_arr = sorted_arr.clone.shuffle!

    expect(selection_sort(unsorted_arr)).to eq sorted_arr
  end



end
