require 'spec_helper'

describe 'Linear Search' do
  context 'item in data' do
    it 'finds the item and returns its index' do
      array = Array.new(100) { rand(1000) }
      target = array[array.size / 2]
      result = linear_search(array, target)

      expect(array[result]).to eq target
    end
  end

  context 'item NOT in data' do
    it 'doesnt find the item and returns nil' do
      array = Array.new(100) { rand(1000) }
      target = 1001
      result = linear_search(array, target)

      expect(result).to be_nil
    end
  end
end
