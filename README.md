# learning_plan

这是 lenxuan 的 2026-2027 编程成长计划仓库。

当前路线已经从原来的“24 周硬核全栈大计划”收敛为更适合当前阶段的主线：

> 先做出能运行、能部署、能展示的项目，再逐步补底层和复杂技术。

## 总目标

到 2027 年 6 月：

- 能独立搭建、部署、交付小型项目。
- 至少有 2 个公网可访问的在线作品。
- 至少 1 个项目有完整 README、截图、部署说明和技术栈说明。
- 至少尝试 3 次接单渠道，并完成 1 次真实交付或半真实委托。

## 当前阶段

当前阶段：第 1 周，Python 入门和 Git 习惯。

现实情况：

- Python 几乎从 0 开始。
- 暂时不急着写完整后端。
- 今天先完成“改代码 -> 运行 -> 看到输出变化”的闭环。

今日入口：

```powershell
python .\scripts\python_basics_day0.py
```

然后修改：

- `name`
- `age`
- `tasks` 列表

再运行一次，确认输出发生变化。

## 仓库结构

- `docs/roadmap-2026-2027.md`：新版 2026-2027 总路线。
- `docs/week-01-python-basics.md`：第 1 周 Python 零基础执行表。
- `docs/ai-rules.md`：AI 使用规则。
- `learning_log.md`：每日学习记录。
- `scripts/python_basics_day0.py`：今天的 Python 第 0 天练习。
- `scripts/site_probe.py`：后续 HTTP 检测练习。
- `scripts/cert_days_left.py`：后续证书到期检测练习。
- `数据结构`：旧计划中的数据结构子模块，保留为 C++ 副线资料。
- `docs/github-upload.md`：以后上传 GitHub 的固定流程。

## 主线

2026 暑假主线：

- Python
- FastAPI
- SQLite
- Git
- Linux
- Nginx
- HTTPS
- 部署

2026 暑假的第一个真实项目：

> `lenxuan-monitor`：服务器监控 + HTTPS 证书到期提醒面板。

## 副线

副线保留 C++ 数据结构训练，但只做少量、持续练习：

- 指针
- 结构体
- 类
- 链表
- 栈和队列
- BST
- 快排或哈希表

副线不能抢走主线时间。

## 已清理的旧计划内容

这些内容已经从当前执行仓库中移除：

- `TS学习` 子模块：TypeScript 迁移不再是 2026 暑假主线。
- `每周审计/W1_TS_Migration`：旧 TS 迁移审计记录，和当前 Python 主线不再匹配。

旧内容没有丢失，仍然可以从 Git 历史里找回。

## 暂时不做

2026 暑假暂时不要把这些放进主线：

- Rust
- Web3
- RAG
- Raft
- Kubernetes
- 微服务
- 高并发架构

这些不是不好，而是现在会稀释最重要的目标：交付第一个可上线项目。

## 学习规则

- 先闭环，再扩展。
- 所有代码都走 Git。
- 每周必须有可运行结果。
- AI 当陪练，不当替身。
- 数据库模型、核心检测逻辑、认证逻辑要先自己写一版。
- 每周复盘：本周写了什么、卡在哪里、下周只推进哪 1-2 件关键事。
