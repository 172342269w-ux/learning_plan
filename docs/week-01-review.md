# 第 1 周复盘

日期：2026-06-15

## 已完成

- Day 0：运行 Python 文件，修改列表，并观察输出变化。
- Day 1：练习变量、字符串、数字和简单计算。
- Day 2：练习 `if`、`else` 和比较表达式。
- Day 3：使用列表和 `for` 循环打印任务清单。
- Day 4：写出一个函数，根据状态码返回 `ok`、`warn` 或 `fail`。
- Day 5：使用 `sys.argv` 读取命令行参数。

## 现在能解释的内容

- `print(...)`：把内容输出到终端。
- 变量：保存一个值，后面可以继续使用。
- `if`：当条件为真时执行一段代码。
- 列表：保存多个值。
- `for` 循环：从列表里一个一个取出值并执行代码。
- 函数：把一段逻辑用名字封装起来。
- `return`：把函数的结果返回给调用它的地方。
- `sys.argv[1]`：命令行里脚本名后面的第一个真正有用的参数。

## 重要踩坑

- Day 3 里，`"add a new task"` 和 `"add one new task"` 不匹配，因为字符串必须完全一致。
- Day 5 里，不额外输入参数时，`len(sys.argv)` 也不是 0，因为脚本名本身也在参数列表里。

## 下一步

开始实现 `scripts/site_probe.py`。

这是路线图里的第一个真实小工具，会把第 1 周学到的基础串起来：

- `sys.argv`：从命令行接收 URL。
- 函数：实现 `probe_url(url)`。
- `return`：返回 HTTP 状态码。
- `if`：判断网站状态是 `OK` 还是 `WARN`。

## 下一步进展

`scripts/site_probe.py` 已经完成第一版：

- `http://example.com` 返回 `OK` 和状态码 `200`。
- `http://example.com/not-found` 返回 `WARN` 和状态码 `404`。
- 不传 URL 时会提示正确用法。
- 当前 Windows/Python 环境访问部分 HTTPS 网站会遇到本机证书校验问题，这属于环境问题，先记录，不阻塞 HTTP 状态码练习。

暂时不要开始 `cert_days_left.py`。证书检测会涉及 SSL 和日期处理，等 `site_probe.py` 真正理解并跑通后再做。
