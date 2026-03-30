#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试登录 API
"""
import requests
import json

# API 地址
BASE_URL = "http://localhost:8000"

# 测试登录
def test_login():
    """测试登录接口"""
    url = f"{BASE_URL}/api/auth/login"
    
    # 测试数据
    payload = {
        "username": "admin",
        "password": "admin123"
    }
    
    print(f"🔐 测试登录 API: {url}")
    print(f"📝 请求数据：{json.dumps(payload, ensure_ascii=False)}")
    
    try:
        # 发送 POST 请求，设置正确的 Content-Type
        response = requests.post(
            url,
            json=payload,  # 使用 json 参数会自动设置 Content-Type: application/json
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            timeout=10
        )
        
        print(f"\n📊 响应状态码：{response.status_code}")
        print(f"📊 响应头 Content-Type: {response.headers.get('Content-Type')}")
        print(f"📊 响应内容：{response.text}")
        
        if response.status_code == 200:
            print("\n✅ 登录成功！")
            data = response.json()
            if data.get("success"):
                print(f"🎫 Token: {data['data']['access_token'][:50]}...")
                return data["data"]["access_token"]
        elif response.status_code == 405:
            print("\n❌ 405 错误 - 方法不允许")
            print("💡 可能原因：")
            print("   1. 请求方法错误（应该使用 POST）")
            print("   2. Content-Type 设置错误（应该是 application/json）")
            print("   3. 路由未正确注册")
        elif response.status_code == 401:
            print("\n❌ 401 错误 - 认证失败")
            print("💡 用户名或密码错误")
        else:
            print(f"\n❌ 请求失败，状态码：{response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("\n❌ 连接错误 - 无法连接到 API 服务器")
        print("💡 请确保后端服务正在运行：docker compose ps")
    except requests.exceptions.Timeout:
        print("\n❌ 请求超时")
    except Exception as e:
        print(f"\n❌ 错误：{e}")
    
    return None


def test_health():
    """测试健康检查接口"""
    url = f"{BASE_URL}/api/health"
    
    print(f"\n🏥 测试健康检查 API: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        print(f"📊 响应状态码：{response.status_code}")
        print(f"📊 响应内容：{response.text}")
        
        if response.status_code == 200:
            print("✅ 后端服务运行正常")
            return True
        else:
            print(f"❌ 健康检查失败，状态码：{response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ 健康检查失败：{e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("TradingAgents-CN API 测试脚本")
    print("=" * 60)
    
    # 先测试健康检查
    if test_health():
        print("\n" + "=" * 60)
        # 测试登录
        test_login()
    else:
        print("\n❌ 后端服务不可用，无法进行登录测试")
