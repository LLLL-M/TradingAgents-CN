#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建初始管理员账户
"""
from pymongo import MongoClient
from datetime import datetime
import bcrypt
import sys

# MongoDB 配置
MONGO_URI = "mongodb://admin:tradingagents123@localhost:27017/tradingagents?authSource=admin"
DB_NAME = "tradingagents"
COLLECTION_NAME = "users"

# 管理员账户配置
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
ADMIN_EMAIL = "admin@example.com"

def create_admin_user():
    """创建管理员账户"""
    print("=" * 60)
    print("创建初始管理员账户")
    print("=" * 60)
    
    try:
        # 连接 MongoDB
        print(f"\n📡 连接 MongoDB: {MONGO_URI.split('@')[1].split('?')[0]}...")
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        
        # 检查是否已存在管理员账户
        existing_admin = collection.find_one({"username": ADMIN_USERNAME})
        if existing_admin:
            print(f"\n⚠️  管理员账户已存在：{ADMIN_USERNAME}")
            print(f"   邮箱：{existing_admin.get('email')}")
            print(f"   创建时间：{existing_admin.get('created_at')}")
            
            # 询问是否重置密码
            print(f"\n💡 是否重置密码为 '{ADMIN_PASSWORD}'? (y/n): ", end="")
            # 自动确认（非交互模式）
            print("y (自动确认)")
            
            # 更新密码
            hashed_password = bcrypt.hashpw(ADMIN_PASSWORD.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            collection.update_one(
                {"username": ADMIN_USERNAME},
                {
                    "$set": {
                        "hashed_password": hashed_password,
                        "updated_at": datetime.utcnow()
                    }
                }
            )
            print(f"✅ 密码已重置为：{ADMIN_PASSWORD}")
            return True
        
        # 创建新管理员账户
        print(f"\n🔐 创建管理员账户：{ADMIN_USERNAME}")
        
        # 哈希密码
        hashed_password = bcrypt.hashpw(ADMIN_PASSWORD.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        print(f"   密码已哈希")
        
        # 构建用户文档
        user_doc = {
            "username": ADMIN_USERNAME,
            "email": ADMIN_EMAIL,
            "hashed_password": hashed_password,
            "is_active": True,
            "is_admin": True,
            "is_verified": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "preferences": {
                "language": "zh-CN",
                "theme": "light",
                "timezone": "Asia/Shanghai"
            }
        }
        
        # 插入数据库
        result = collection.insert_one(user_doc)
        print(f"✅ 管理员账户创建成功！")
        print(f"   用户 ID: {result.inserted_id}")
        print(f"   用户名：{ADMIN_USERNAME}")
        print(f"   密码：{ADMIN_PASSWORD}")
        print(f"   邮箱：{ADMIN_EMAIL}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ 创建失败：{e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        client.close()
        print("\n📡 MongoDB 连接已关闭")


if __name__ == "__main__":
    success = create_admin_user()
    sys.exit(0 if success else 1)
