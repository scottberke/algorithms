require 'spec_helper'

describe 'Peaks and Valleys' do
  def check_peaks_and_valleys(array)
    even_peak = array[0] > array[1] ? true : false
    status = true

    (0..array.size - 2).each do |index|
      if even_peak
        status = status && array[index] >= array[index + 1]
      else
        status = status && array[index] <= array[index + 1]
      end
      even_peak = !even_peak
    end

    status
  end


  it 'outputs an array with peaks and valleys - example from book' do
    arr = [5, 3, 1, 2, 3]

    sorted_peaks_and_valleys = peaks_and_valleys(arr)

    expect(check_peaks_and_valleys(sorted_peaks_and_valleys)).to be true
  end

  it 'outputs an array with peaks and valleys - second example' do
    arr = [5 ,8, 6, 2, 3, 4, 6]

    sorted_peaks_and_valleys = peaks_and_valleys(arr)

    expect(check_peaks_and_valleys(sorted_peaks_and_valleys)).to be true
  end

  it 'outputs an array with peaks and valleys - random' do
    arr = Array.new(20) { rand(100) }

    sorted_peaks_and_valleys = peaks_and_valleys(arr)

    expect(check_peaks_and_valleys(sorted_peaks_and_valleys)).to be true
  end

end
