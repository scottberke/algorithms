

class DFS
  attr_accessor :root, :found_node

  def initialize(root:)
    @root = root
    @found_node = nil
  end

  def depth_first_search(root: self.root, target:)
    if root

      self.found_node = root if root.data == target

      depth_first_search(root: root.left, target: target)
      depth_first_search(root: root.right, target: target)
    end
  end

end
