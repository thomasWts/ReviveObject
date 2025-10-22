
import os
import sys


class Item:
    """
    物品类：包含物品编号、物品名称、物品描述、联系人信息
    """
    def __init__(self, item_id: int, name: str, 
                 description: str, contact_info: str):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.contact_info = contact_info

    def to_dict(self) -> dict:
        """
        将物品对象转换为字典
        """
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "contact_info": self.contact_info
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Item':
        """
        从字典创建物品对象
        """
        return Item(
            item_id=data["item_id"],
            name=data["name"],
            description=data["description"],
            contact_info=data["contact_info"]
        )
    
    def __str__(self) -> str:
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Contact: {self.contact_info}"
    
class User:
    """
    用户类：包含用户编号、用户名、邮箱
    """
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.items = []  # 用户发布的物品列表

    def add_item(self, item: Item):
        """
        添加物品到用户的物品列表
        """
        self.items.append(item)
        print(f"{self.username} 添加了物品: {item.name}")

    def list_items(self):
        """
        列出用户发布的所有物品
        """
        if not self.items:
            print(f"{self.username} 没有发布任何物品。")
            return

        for item in self.items:
            print(item)

    def to_dict(self) -> dict:
        """
        将用户对象转换为字典
        """
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'User':
        """
        从字典创建用户对象
        """
        return User(
            user_id=data["user_id"],
            username=data["username"],
            email=data["email"]
        )
    
    def __str__(self) -> str:
        return f"ID: {self.user_id}, Username: {self.username}, Email: {self.email}"