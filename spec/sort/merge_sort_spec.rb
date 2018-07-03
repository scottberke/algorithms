require 'spec_helper'

describe 'Merge Sort' do
  it 'sorts a simple array with even number of elements' do
    sorted_arr = [4, 3, 2, 1].sort!
    unsorted_arr = sorted_arr.clone.shuffle!

    expect(merge_sort(unsorted_arr, 0, unsorted_arr.size - 1)).to eq sorted_arr
  end

  it 'sorts a simple array with odd number of elements' do
    sorted_arr = [5, 4, 3, 2, 1].sort!
    unsorted_arr = sorted_arr.clone.shuffle!

    expect(merge_sort(unsorted_arr, 0, unsorted_arr.size - 1)).to eq sorted_arr
  end

  it 'sorts an array with arbitrary number of elements' do
    sorted_arr = Array.new(rand(100)) { rand(100) }
    sorted_arr.sort!
    unsorted_arr = sorted_arr.clone.shuffle!

    expect(merge_sort(unsorted_arr, 0, unsorted_arr.size - 1)).to eq sorted_arr
  end


end
