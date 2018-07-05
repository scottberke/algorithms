
class NodeContainer
  attr_accessor :node, :path

  def initialize(node:, path: [])
    @node = node
    @path = path
  end
end



def breadth_first_search_w_path(root, target)
  node_queue = [ NodeContainer.new(node: root) ]

  while !node_queue.empty?
    current_node_container = node_queue.pop
    current_node = current_node_container.node

    if current_node.data == target
      current_node_container.path << current_node.data

      return current_node_container
    end

    if current_node.left
      new_node_container = NodeContainer.new(node: current_node.left,
        path: current_node_container.path + [current_node.data])

      node_queue.unshift(new_node_container)
    end

    if current_node_container.node.right
      new_node_container = NodeContainer.new(node: current_node.right,
        path: current_node_container.path + [current_node.data])

      node_queue.unshift(new_node_container)
    end
  end
end
