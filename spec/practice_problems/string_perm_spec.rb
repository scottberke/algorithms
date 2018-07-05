require 'spec_helper'

describe 'String Permutations' do
  describe 'simple string' do
    it 'returns the permutations' do
      string = '123'
      permutations = string.split('').permutation.flat_map { |i| i.join }

      expect(string_perm(string)).to eq permutations
    end
  end

  describe 'longer string' do
    it 'returns the permutations' do
      string = '1234'
      permutations = string.split('').permutation.flat_map { |i| i.join }

      expect(string_perm(string)).to eq permutations
    end
  end

  describe 'longer string of chars' do
    it 'returns the permutations' do
      string = 'abcde'
      permutations = string.split('').permutation.flat_map { |i| i.join }

      expect(string_perm(string)).to eq permutations
    end
  end
end
