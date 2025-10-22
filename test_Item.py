from revive import Item


def test_item_class():
    print("=== 测试 Item 类 ===")

    # 1. 创建 Item 对象
    item1 = Item(1, "书", "九成新教材", "alice@example.com")
    item2 = Item(2, "椅子", "二手办公椅", "bob@example.com")

    # 2. 打印对象
    print("打印 Item 对象：")
    print(item1)
    print(item2)
    
    # 3. 转字典
    dict1 = item1.to_dict()
    print("\nItem 转字典：")
    print(dict1)

    # 4. 从字典创建 Item
    new_item = Item.from_dict(dict1)
    print("\n从字典创建 Item：")
    print(new_item)

if __name__ == "__main__":
    test_item_class()