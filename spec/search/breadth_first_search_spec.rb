require 'spec_helper'

describe 'Breadth First Search' do
  let(:tree) do
    #            50
    #        /        \
    #       15         70
    #     /   \       /   \
    #    20    18    90    80
    #   /  \  /  \  /  \  /  \
    #  5  30 6  40 60  2 25 100
    root = Node.new(50)
    root.left = Node.new(15); root.right = Node.new(70)
    root.left.left = Node.new(20); root.left.right = Node.new(18)
    root.right.left = Node.new(90); root.right.right = Node.new(80)
    root.left.left.left = Node.new(5); root.left.left.right = Node.new(30)
    root.left.right.left = Node.new(6); root.left.right.right = Node.new(40)
    root.right.left.left = Node.new(60); root.right.left.right = Node.new(2)
    root.right.right.left = Node.new(25); root.right.right.right = Node.new(100)
    root
  end

  context 'when node is in tree' do
    it 'finds the correct node' do
      node = breadth_first_search(tree, 18)
      expect(node.data).to eq 18
    end
  end

  context 'when node is NOT in tree' do
    it 'returns nil' do
      node = breadth_first_search(tree, 19)
      expect(node).to be_nil
    end
  end
end
