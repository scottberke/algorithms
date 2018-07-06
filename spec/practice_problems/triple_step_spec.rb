require 'spec_helper'

describe 'Triple Step' do
  describe '1 step' do
    it 'returns the number of steps required' do
      stairs = 1

      expect(triple_step(stairs)).to eq 1
    end
  end

  describe '2 step' do
    it 'returns the number of steps required' do
      stairs = 2

      expect(triple_step(stairs)).to eq 2
    end
  end

  describe '3 step' do
    it 'returns the number of steps required' do
      stairs = 3

      expect(triple_step(stairs)).to eq 4
    end
  end

  describe '4 step' do
    it 'returns the number of steps required' do
      stairs = 4

      expect(triple_step(stairs)).to eq 7
    end
  end

  describe '5 step' do
    it 'returns the number of steps required' do
      stairs = 5

      expect(triple_step(stairs)).to eq 13
    end
  end

  describe '6 step' do
    it 'returns the number of steps required' do
      stairs = 6

      expect(triple_step(stairs)).to eq 24
    end
  end

  describe '15 step' do
    it 'returns the number of steps required' do
      stairs = 15

      expect(triple_step(stairs)).to eq 5768
    end
  end
end
