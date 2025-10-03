%cd ~/GitHub/obsidian_canvas_python/src

from obsidian_canvas_python.canvas import Canvas
from obsidian_canvas_python.enums import NodeType, Color, Side

# 创建一个新的画布
canvas = Canvas()

# 添加一个文本节点
node1 = canvas.add_node(
    node_type=NodeType.TEXT,
    x=0, y=0, width=200, height=100,
    text="这是一个文本节点",
    color=Color.RED
)

# 添加一个文件节点
node2 = canvas.add_node(
    node_type=NodeType.FILE,
    x=300, y=0, width=200, height=100,
    file="My Important Document.md"
)

# 添加一个链接节点
node3 = canvas.add_node(
    node_type=NodeType.LINK,
    x=600, y=0, width=200, height=100,
    url="https://www.example.com",
    text="Example Website"
)

# 添加一个边
edge1 = canvas.add_edge(
    from_node_id=node1.id,
    to_node_id=node2.id,
    label="连接到文件",
    color=Color.BLUE,
    from_side=Side.RIGHT,
    to_side=Side.LEFT
)

# 保存画布到文件
canvas.save("my_new_canvas.canvas")
print("画布已保存到 my_new_canvas.canvas")

!pwd

from obsidian_canvas_python.canvas import Canvas

# 从文件加载画布
canvas = Canvas("my_new_canvas.canvas")
print(f"加载了 {len(canvas.nodes)} 个节点和 {len(canvas.edges)} 条边。")

# 访问节点和边
for node in canvas.nodes:
    print(f"节点 ID: {node.id}, 类型: {node.node_type.value}, 文本: {node.text}")

for edge in canvas.edges:
    print(f"边 ID: {edge.id}, 从: {edge.from_node}, 到: {edge.to_node}, 标签: {edge.label}")


### 删除节点和边


from obsidian_canvas_python.canvas import Canvas
from obsidian_canvas_python.enums import Range

canvas = Canvas("my_new_canvas.canvas")

# 假设我们想删除之前创建的 node1
if canvas.nodes:
    node_to_delete_id = canvas.nodes[0].id
    if canvas.delete_object(node_to_delete_id, obj_type=Range.NODE):
        print(f"节点 {node_to_delete_id} 及其关联的边已删除。")
    else:
        print(f"未找到节点 {node_to_delete_id}。")

# 假设我们想删除之前创建的 edge1
if canvas.edges:
    edge_to_delete_id = canvas.edges[0].id
    if canvas.delete_object(edge_to_delete_id, obj_type=Range.EDGE):
        print(f"边 {edge_to_delete_id} 已删除。")
    else:
        print(f"未找到边 {edge_to_delete_id}。")

canvas.save("my_updated_canvas.canvas")

from obsidian_canvas_python.canvas import Canvas
from obsidian_canvas_python.enums import NodeType, Color

canvas = Canvas("my_new_canvas.canvas")

# 查找所有文本节点
text_nodes = canvas.find_nodes(node_type=NodeType.TEXT)
print(f"找到 {len(text_nodes)} 个文本节点。")

# 查找包含特定文本的节点
search_nodes = canvas.find_nodes(text_contains="文本")
print(f"找到 {len(search_nodes)} 个包含 '文本' 的节点。")

# 查找特定颜色的边
red_edges = canvas.find_edges(color=Color.RED)
print(f"找到 {len(red_edges)} 条红色边。")

# 查找从特定节点发出的边
edges_from_node1 = canvas.find_edges(from_node_id="node-id-here") # 替换为实际的节点ID
print(f"找到 {len(edges_from_node1)} 条从指定节点发出的边。")

from obsidian_canvas_python.canvas import Canvas

canvas = Canvas("my_new_canvas.canvas")

mermaid_syntax = canvas.to_mermaid()
print("\nMermaid 语法:")
print(mermaid_syntax)

from obsidian_canvas_python.canvas import Canvas
from obsidian_canvas_python.exceptions import CanvasFileNotFoundError, NodeNotFoundError

try:
    canvas = Canvas("non_existent_file.canvas")
except CanvasFileNotFoundError as e:
    print(f"错误: {e}")

try:
    canvas = Canvas("my_new_canvas.canvas")
    canvas.delete_object("non_existent_node_id")
except NodeNotFoundError as e:
    print(f"错误: {e}")