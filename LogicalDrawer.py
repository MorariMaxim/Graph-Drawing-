from Node import Node
from PhysicalDrawer import PhyisicalDrawer
from collections import defaultdict
class LogicalDrawer:
    
    class NodeInfo:
        
        def __init__(self) -> None:
            self.rightmost_drawned = 0
            self.x = 0
            self.y = 0
            
        def __iter__(self):
            return iter((self.rightmost_drawned, self.x, self.y))
        
        def set(self, r,x,y):
            self.rightmost_drawned = r
            self.x = x
            self.y = y

    
    def __init__(self,physical_drawer: PhyisicalDrawer, node:Node,children_distance:int,root_child_d:int, node_inner_pad:int) -> None:
        self.root = node
        self.node_infos: defaultdict[Node, LogicalDrawer.NodeInfo] = defaultdict(LogicalDrawer.NodeInfo)

        self.children_distance = children_distance
        self.root_child_d = root_child_d
        self.node_inner_pad = node_inner_pad
        self.physical_drawer = physical_drawer

    def draw_graph(self, node:Node, left_offset = 0, top_offset = 0, root_call=True):
        
        size = self.get_drawned_node_size(node)
        
        lo = left_offset
        for child in node.children:

            self.draw_graph(child,lo,top_offset+size + self.root_child_d,False)
            lo = self.node_infos[child].rightmost_drawned + self.children_distance
                            
        if node.children:
            lo-=self.children_distance
                
        y = top_offset + size/2
        off =(lo - left_offset)/2
        x = left_offset +  (off if off > size/2 else size/2)
        self.node_infos[node].set(max(lo, x + size/2 ) ,x,y)
                                
        for child in node.children:
            
            self.draw_edge(node,child)
            self.draw_node(child, self.node_infos[child].x,self.node_infos[child].y)
            
        if root_call:
            self.draw_node(node,x,y)
            
    def draw_node(self, node:Node, x, y):
        self.physical_drawer.draw_circle(x,y,self.get_drawned_node_size(node)/2)        
        self.physical_drawer.draw_text(node.value,x,y)        
    
    def draw_edge(self, node1:Node, node2:Node):
        
        _,x1,y1 = self.node_infos[node1]
        _,x2,y2 = self.node_infos[node2]
        
        self.physical_drawer.draw_line(x1,y1,x2,y2)

    def get_drawned_node_size(self, node):
        text_size = max(self.physical_drawer.get_size(node.value))
        return text_size + 2 * self.node_inner_pad # + circumeference
    


        
root = Node(value="A")
node_b = Node(value="B")
node_c = Node(value="C")
node_d = Node(value="D")
node_e = Node(value="E")
node_f = Node(value="F")
node_g = Node(value="G")
node_h = Node(value="H")
node_i = Node(value="I")
node_j = Node(value="J")
node_k = Node(value="K")

# Build the tree structure
root.children.append(node_b)
root.children.append(node_k)
root.children.append(node_c)

node_b.children.append(node_d)
node_b.children.append(node_e)

node_c.children.append(node_f)
node_c.children.append(node_g)

node_f.children.append(node_h)
node_f.children.append(node_i)

node_g.children.append(node_j)



physical_drawer = PhyisicalDrawer()
logical_drawer = LogicalDrawer(physical_drawer,root,50,50,20)

logical_drawer.draw_graph(root)

val = input("waiting for input")