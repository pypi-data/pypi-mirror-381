# 变更日志

所有重要的项目变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且此项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

## [未发布]

### 新增
- 📝 添加中文快速开始指南 (`QUICKSTART_CN.md`)
- 📖 增强 README 文档，添加详细的 CLI 使用示例
- 📋 添加命令速查表和翻译前后对比示例
- ❓ 添加常见问题解答部分
- ⚡ **[性能提升]** 实现并发文件翻译，使用 asyncio.gather 同时处理最多 5 个文件
- 🚦 添加 Semaphore 限流机制，避免 API 速率限制

### 修复
- 🐛 **[关键修复]** 修复 Python parser 在翻译时丢失 docstring 引号的问题
- 🐛 修复多行 docstring 处理导致的行号错位问题
- 🐛 修复 `langlint fix` 命令参数传递错误
- 🔧 改进 token 替换逻辑，采用倒序处理避免行号冲突
- 🎯 完善字符串 token 重建，正确保留原始引号样式（`"""`, `'''`, `"`, `'`）

### 变更
- ⚡ 优化多行 token 处理性能
- 📚 更新 README 文档结构，添加路线图和项目状态
- 🎨 改进 CLI 输出格式和用户体验

## [1.0.0] - 2024-01-01

### 新增
- 🎉 首次发布 LangLint v1.0.0
- 🔌 可插拔的解析引擎架构
  - Python 解析器 (`.py`, `.pyi`, `.pyw`)
  - Markdown 解析器 (`.md`, `.markdown`, `.mdown`, `.mkd`, `.mkdn`)
  - Jupyter Notebook 解析器 (`.ipynb`)
  - 通用代码解析器 (`.js`, `.ts`, `.go`, `.rs`, `.java`, `.cpp`, `.c`, `.cs`, `.php`, `.rb`, `.sh`, `.sql`, `.r`, `.m`, `.scala`, `.kt`, `.swift`, `.dart`, `.lua`, `.vim`)
  - 配置文件解析器 (`.yaml`, `.yml`, `.toml`, `.json`, `.ini`, `.cfg`, `.conf`, `.properties`)
- 🌐 多翻译服务支持
  - OpenAI GPT 模型翻译
  - DeepL 高质量翻译
  - Google Translate 翻译
  - Azure Translator 翻译
  - Mock 测试翻译器
- ⚡ 高性能特性
  - 异步 I/O 支持
  - SQLite 持久化缓存
  - 批量翻译处理
  - 内存优化和流式处理
- 🛠️ 强大的配置系统
  - 路径匹配配置
  - 自动语言检测
  - 灵活的文件排除规则
  - 环境变量支持
- 📊 完整的可复现性支持
  - 三个端到端场景示例
  - 可复现的基准测试脚本
  - 性能指标和报告生成
- 🧪 军事级测试套件
  - 单元测试覆盖率 ≥ 85%
  - 核心模块覆盖率 ≥ 95%
  - 集成测试和端到端测试
  - 跨平台测试支持
- 📚 完整的文档
  - 面向初学者的快速开始指南
  - 详细的 API 参考文档
  - 教程和示例
  - 开发者指南
- 🔒 透明的合规与伦理设计
  - 数据最小化原则
  - 用户控制原则
  - 零遥测设计
  - 隐私保护政策
- 🚀 命令行界面
  - `langlint scan` - 扫描可翻译文本
  - `langlint translate` - 翻译文件
  - `langlint fix` - 修复文件（原地翻译）
  - `langlint status` - 检查翻译服务状态
  - `langlint info` - 显示项目信息
- 🎯 三个端到端场景
  - 场景 A: 软件国际化 - Python 科学计算库
  - 场景 B: 文档全球化 - Markdown 文档
  - 场景 C: 可复现研究的无障碍化 - Jupyter Notebook
- 🔧 开发工具支持
  - 代码质量检查 (Black, Ruff, MyPy, Bandit)
  - 预提交钩子
  - 持续集成/持续部署
  - 安全审计和依赖扫描
- 📦 开放软件资产包
  - MIT 许可证
  - PyPI 发布
  - Zenodo DOI 归档
  - 引用规范 (CITATION.cff)

### 技术细节
- Python 3.8+ 支持
- 异步编程支持
- 类型注解完整覆盖
- 错误处理机制完善
- 性能优化和内存管理
- 跨平台兼容性

### 文档
- README.md - 项目介绍和快速开始
- PRIVACY.md - 隐私政策
- CITATION.cff - 引用信息
- 完整的 API 文档
- 教程和示例

### 测试
- 单元测试覆盖所有核心功能
- 集成测试验证组件协作
- 端到端测试确保完整工作流程
- 性能测试和基准测试
- 跨平台兼容性测试

### 构建和部署
- GitHub Actions CI/CD
- 自动化测试和代码质量检查
- 自动化发布到 PyPI
- 文档自动构建和部署
- 安全审计和依赖扫描

---

## 版本说明

### 版本号格式
我们使用 [语义化版本](https://semver.org/spec/v2.0.0.html) 格式：
- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

### 版本类型
- **主版本** (1.0.0)：重大更新，可能包含破坏性变更
- **次版本** (1.1.0)：新功能，向下兼容
- **修订版本** (1.0.1)：错误修复，向下兼容
- **预发布版本** (1.0.0-alpha.1)：预发布版本，可能不稳定

### 支持策略
- **当前版本**：完全支持，包括新功能和错误修复
- **前一个主版本**：仅支持错误修复
- **更早版本**：不再支持

### 升级指南
- **主版本升级**：请查看升级指南和破坏性变更说明
- **次版本升级**：通常可以直接升级
- **修订版本升级**：建议立即升级以获得错误修复

---

## 贡献者

感谢所有为 LangLint 做出贡献的开发者和用户！

### 核心团队
- LangLint Team - 项目维护者

### 贡献者
- 感谢所有提交代码、报告问题、提出建议的贡献者

---

## 许可证

本项目采用 MIT 许可证。详情请查看 [LICENSE](LICENSE) 文件。

---

## 链接

- [项目主页](https://github.com/HzaCode/Langlint)
- [文档](https://github.com/HzaCode/Langlint)
- [问题反馈](https://github.com/HzaCode/Langlint/issues)
- [讨论区](https://github.com/HzaCode/Langlint/discussions)
- [PyPI 包](https://pypi.org/project/langlint/)
- [Zenodo 归档](https://zenodo.org/record/1234567)










