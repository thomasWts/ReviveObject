import gradio as gr
from revive import Item, User  # 假设 Item 和 User 在 revive.py

# 全局存储：用户和物品
users = {}
all_items = []

# 创建一个默认用户
current_user = User(1, "Alice", "alice@example.com")
users[current_user.user_id] = current_user

# 添加物品
def add_item(name, description, contact_info):
    item_id = len(all_items) + 1
    item = Item(item_id, name, description, contact_info)
    current_user.add_item(item)
    all_items.append(item)
    return f"✅ 添加成功: {item}"

# 显示用户物品列表
def show_my_items():
    if not current_user.items:
        return "你没有发布任何物品。"
    return "\n".join([str(item) for item in current_user.items])

# 显示所有物品
def show_all_items():
    if not all_items:
        return "当前没有任何物品。"
    return "\n".join([str(item) for item in all_items])

# 删除物品（通过 ID）
def delete_item(item_id):
    try:
        item_id = int(item_id)
        item_to_remove = next((i for i in current_user.items if i.item_id == item_id), None)
        if item_to_remove:
            current_user.items.remove(item_to_remove)
            all_items.remove(item_to_remove)
            return f"✅ 删除成功: {item_to_remove}"
        else:
            return "❌ 未找到该物品"
    except ValueError:
        return "❌ 请输入有效的物品 ID"

# Gradio UI 布局
with gr.Blocks() as demo:
    gr.Markdown("## 物品复活平台（Revive Items）")
    
    with gr.Tab("添加物品"):
        name = gr.Textbox(label="物品名称")
        desc = gr.Textbox(label="物品描述")
        contact = gr.Textbox(label="联系人信息")
        add_btn = gr.Button("添加物品")
        add_output = gr.Textbox(label="输出")
        add_btn.click(add_item, inputs=[name, desc, contact], outputs=add_output)
    
    with gr.Tab("查看我的物品"):
        my_items_btn = gr.Button("显示我的物品")
        my_items_output = gr.Textbox(label="我的物品列表")
        my_items_btn.click(show_my_items, inputs=[], outputs=my_items_output)
    
    with gr.Tab("查看所有物品"):
        all_items_btn = gr.Button("显示所有物品")
        all_items_output = gr.Textbox(label="所有物品列表")
        all_items_btn.click(show_all_items, inputs=[], outputs=all_items_output)
    
    with gr.Tab("删除物品"):
        del_id = gr.Textbox(label="物品 ID")
        del_btn = gr.Button("删除物品")
        del_output = gr.Textbox(label="输出")
        del_btn.click(delete_item, inputs=del_id, outputs=del_output)

# 启动界面
demo.launch()
