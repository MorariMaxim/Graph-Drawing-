from __future__ import annotations

class Node:
    
    class Edge:
        def __init__(self, value, node:Node ) -> None:        
            self.value = value
            self.node = node
        
    
    def __init__(self, value = None, children = None) -> None:        
        self.value = value
        self.children: list[Node.Edge] = children if children else []
