# 新增模型配置说明

本文档说明如何配置和使用新增的 AI 模型。

## 🆕 新增模型列表

本次更新添加了以下 4 个新模型的支持：

| 模型名称 | 厂商 | 能力等级 | 适用场景 |
|---------|------|---------|---------|
| **qwen3.5-plus** | 阿里百炼 | 4（专业级） | 深度分析、全面分析 |
| **glm-5** | 智谱 AI | 5（旗舰级） | 最强推理、全面分析 |
| **kimi-k2.5** | 月之暗面 | 4（专业级） | 长上下文处理、深度分析 |
| **MiniMax-M2.5** | MiniMax | 4（专业级） | 高性能通用分析 |

## 📋 配置步骤

### 1. 获取 API 密钥

根据您的需要，访问相应厂商的控制台获取 API 密钥：

- **阿里百炼 (Qwen3.5 Plus)**: https://dashscope.console.aliyun.com/
- **智谱 AI (GLM-5)**: https://open.bigmodel.cn/
- **月之暗面 (Kimi K2.5)**: https://platform.moonshot.cn/
- **MiniMax (M2.5)**: https://platform.minimaxi.com/

### 2. 配置环境变量

#### Docker 环境 (.env.docker)

```bash
# 新增模型 API 密钥配置
QWEN35_PLUS_API_KEY=your_qwen35_plus_api_key_here
ZHIPU_API_KEY=your_zhipu_api_key_here
GLM5_API_KEY=your_glm5_api_key_here
MOONSHOT_API_KEY=your_moonshot_api_key_here
KIMI_K25_API_KEY=your_kimi_k25_api_key_here
MINIMAX_API_KEY=your_minimax_api_key_here
```

#### 本地环境 (.env.example)

```bash
# 新增模型 API 密钥配置
QWEN35_PLUS_API_KEY=your_qwen35_plus_api_key_here
ZHIPU_API_KEY=your_zhipu_api_key_here
GLM5_API_KEY=your_glm5_api_key_here
MOONSHOT_API_KEY=your_moonshot_api_key_here
KIMI_K25_API_KEY=your_kimi_k25_api_key_here
MINIMAX_API_KEY=your_minimax_api_key_here
```

### 3. 在系统中配置模型

1. 登录系统管理界面
2. 进入"配置管理" -> "LLM 模型配置"
3. 添加新模型，填写以下信息：
   - **模型名称**: 如 `qwen3.5-plus`
   - **供应商**: 如 `dashscope`
   - **API Base URL**: 如 `https://dashscope.aliyuncs.com/compatible-mode/v1`
   - **能力等级**: 根据模型选择 (4 或 5)
   - **适用角色**: 建议选择"both"（通用）

### 4. 验证配置

使用以下命令验证模型配置是否正确：

```bash
# 检查配置状态
python -m cli.main config

# 测试模型连接
python -m cli.main test
```

## 🔧 Tushare 数据源配置

用户指定使用 Tushare 数据源，每分钟 200 次调用限制。

### 配置说明

在 `.env.docker` 和 `.env.example` 中已配置：

```bash
# Tushare API Token
TUSHARE_TOKEN=your_tushare_token_here
TUSHARE_ENABLED=true

# Tushare 权限等级配置（用于速率限制）
# 可选值：free(100 次/分), basic(200), standard(400), premium(600), vip(800)
# 用户指定每分钟 200 次限制，使用 basic 等级
TUSHARE_TIER=basic
TUSHARE_RATE_LIMIT_SAFETY_MARGIN=0.8
```

### 获取 Tushare Token

1. 访问 https://tushare.pro/register?reg=tacn
2. 注册账号并完成邮箱验证
3. 在个人中心获取 Token
4. 建议升级积分到 2000 积分以上以获得更多权限

## 🐳 Docker 部署

### 启动服务

```bash
# 复制并编辑配置文件
cp .env.docker .env
# 编辑 .env 文件，填入您的 API 密钥

# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

### 访问地址

- **Web 应用**: http://localhost:3000
- **API 服务**: http://localhost:8000
- **Redis 管理**: http://localhost:8081
- **MongoDB 管理**: http://localhost:8082

## 📊 模型能力对比

| 模型 | 能力等级 | 推理能力 | 长上下文 | 工具调用 | 性价比 |
|------|---------|---------|---------|---------|-------|
| qwen3.5-plus | 4 | ✅ | ✅ | ✅ | ⭐⭐⭐⭐ |
| glm-5 | 5 | ✅✅ | ✅ | ✅ | ⭐⭐⭐ |
| kimi-k2.5 | 4 | ✅ | ✅✅ | ✅ | ⭐⭐⭐⭐ |
| MiniMax-M2.5 | 4 | ✅ | ✅ | ✅ | ⭐⭐⭐⭐ |

## 🎯 推荐配置

### 快速分析 + 深度分析模型对

| 分析深度 | 快速模型推荐 | 深度模型推荐 |
|---------|------------|------------|
| 快速 | qwen-turbo | qwen-plus |
| 基础 | qwen-plus | qwen3.5-plus |
| 标准 | qwen3.5-plus | glm-5 |
| 深度 | qwen3.5-plus | glm-5 |
| 全面 | kimi-k2.5 | glm-5 |

## ⚠️ 注意事项

1. **API 密钥安全**: 请勿将 `.env` 文件提交到 Git 仓库
2. **速率限制**: Tushare basic 等级限制为每分钟 200 次调用
3. **成本控制**: 建议在系统中启用成本跟踪功能
4. **模型选择**: 系统会根据分析深度自动推荐合适的模型对

## 🔗 相关文档

- [配置指南](docs/configuration_guide.md)
- [Docker 部署指南](docs/docker_deployment.md)
- [模型能力说明](docs/model_capabilities.md)
