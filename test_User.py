# test_user.py

from revive import Item, User  # 假设你的类在 revive.py 中

def test_user_class():
    print("=== 测试 User 类 ===")

    # 1. 创建用户
    alice = User(1, "Alice", "alice@example.com")
    bob = User(2, "Bob", "bob@example.com")

    # 打印用户信息
    print("\n用户信息：")
    print(alice)
    print(bob)

    # 2. 创建物品
    book = Item(1, "书", "九成新教材", "alice@example.com")
    chair = Item(2, "椅子", "二手办公椅", "bob@example.com")

    # 3. 用户添加物品
    print("\n用户添加物品：")
    alice.add_item(book)
    bob.add_item(chair)

    # 4. 列出用户发布的物品
    print("\nAlice 的物品列表：")
    alice.list_items()
    print("\nBob 的物品列表：")
    bob.list_items()

    # 5. 测试 to_dict 和 from_dict
    print("\n用户对象 → 字典 → 用户对象：")
    alice_dict = alice.to_dict()
    print("Alice 字典：", alice_dict)

    new_alice = User.from_dict(alice_dict)
    print("从字典创建的新 Alice：", new_alice)

if __name__ == "__main__":
    test_user_class()
