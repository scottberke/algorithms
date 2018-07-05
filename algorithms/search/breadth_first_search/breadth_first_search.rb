
def breadth_first_search(root, target)
  node_queue = [root]

  while !node_queue.empty?
    current_node = node_queue.pop

    return current_node if current_node.data == target

    node_queue.unshift(current_node.left) if current_node.left
    node_queue.unshift(current_node.right) if current_node.right
  end
end
