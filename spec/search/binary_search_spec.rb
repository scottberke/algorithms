require 'spec_helper'

describe 'Binary Search' do
  describe 'recursive' do
    context 'item in data' do
      it 'finds the item and returns its index' do
        10.times do
          array = Array.new(100) { rand(1000) }
          array.sort!

          target_index = array.size / rand(3..10)
          target = array[target_index]

          result = binary_search(array, target, 0, array.size - 1)


          expect(array[result]).to eq target
        end
      end
    end

    context 'item NOT in data' do
      it 'doesnt find the item and returns nil' do
        array = Array.new(100) { rand(1000) }
        target = 1001

        array.sort!
        result = binary_search(array, target, 0, array.size - 1)

        expect(result).to be_nil
      end
    end
  end

  describe 'iterative' do
    context 'item in data' do
      it 'finds the item and returns its index' do
        10.times do
          array = Array.new(100) { rand(1000) }
          array.sort!

          target_index = array.size / rand(3..10)
          target = array[target_index]

          result = binary_search_iterative(array, target)

          expect(array[result]).to eq target
        end
      end
    end

    context 'item NOT in data' do
      it 'doesnt find the item and returns nil' do
        array = Array.new(100) { rand(1000) }
        target = 1001

        array.sort!
        result = binary_search_iterative(array, target)

        expect(result).to be_nil
      end
    end
  end
end
