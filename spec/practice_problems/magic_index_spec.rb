require 'spec_helper'

describe 'Magic Index' do
  it 'finds a magic index when its in the array' do
    arr = [ -1, 0, 1, 2, 4, 6 ] # arr[4] = 4

    expect(magic_index(arr)).to eq 4
  end

  it 'finds magic index with a larger array' do
    arr = [-9, -4, -1, 0, 1, 2, 6, 8, 9, 15, 20 ] # arr[6] = 6

    expect(magic_index(arr)).to eq 6
  end

  it 'returns nil if no magic index exists' do
    arr = [ -1, 0, 1, 2, 5, 6 ]

    expect(magic_index(arr)).to be_nil
  end


end
