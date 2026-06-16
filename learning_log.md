# Learning Log

## 2026-06-12

Stage: Week 1 - Python basics.

Reality check:

- I am starting from almost zero Python.
- Today's goal is not to finish real monitoring scripts.
- Today's goal is to run one Python file, change it, and understand the output.

Today's target:

- [ ] Run `scripts/python_basics_day0.py`.
- [ ] Change `name` and `age`.
- [ ] Add one task to the `tasks` list.
- [ ] Explain what `if is_adult(age):` means in your own words.
- [ ] Make the first Git commit.

Notes:

- What I tried:我理解了 if is_adult(age): 的意思：把变量 age 作为实参传给 is_adult 函数，函数判断 age 是否大于等于 18。如果返回 True，就输出成年提示；如果返回 False，就输出未成年提示。
- What failed:暂时没有报错。
- What I understood after fixing it: list 里多一个元素，for 循环就会多打印一行。

## 2026-06-13

Stage: Week 1 - Python basics, Day 1.

Today's target:

- [x] Run `scripts/python_basics_day1.py`.
- [x] Change `learning_goal`.
- [x] Change `today_task`.
- [x] Change `study_days` and observe `rest_days`.
- [x] Explain what `age + 1` and `days_in_one_week - study_days` mean.

Notes:

- What I tried:我修改了 learning_goal、today_task 和 study_days，并重新运行 Day 1 脚本。
- What failed:暂时无报错
- What I understood after fixing it:变量可以保存文字和数字，数字变量可以做加减计算；study_days 改变后，rest_days 会跟着重新计算。
age + 1 表示用当前年龄加 1，得到明年的年龄。
days_in_one_week - study_days 表示一周 7 天减去学习天数，得到休息天数。

## 2026-06-14

Stage: Week 1 - Python basics, Day 2.

Today's target:

- [x] Run `scripts/python_basics_day2.py`.
- [x] Change `score`.
- [x] Observe both pass and fail outputs.
- [x] Explain what `>=` means.
- [x] Explain why the code entered `if` or `else`.

Notes:

- What I tried: 我修改了 score，并运行 Day 2 脚本观察 if 和 else 的输出。
- What failed: 暂时没有报错。
- What I understood after fixing it: 如果分数大于等于 60，`score >= pass_line` 返回 True，程序进入 if 分支；如果分数小于 60，则返回 False，程序进入 else 分支。

## 2026-06-15

Stage: Week 1 - Python basics, Day 3.

Today's target:

- [x] Run `scripts/python_basics_day3.py`.
- [x] Add one task to `tasks`.
- [x] Add one completed task to `completed_tasks`.
- [x] Observe task counts changing.
- [x] Explain what `for task in tasks:` means.

Notes:

- What I tried: 我给 `tasks` 增加了一个新任务，也给 `completed_tasks` 增加了一个已完成任务，然后重新运行 Day 3 脚本。
- What failed: `completed_tasks` 里的 `"add a new task"` 和 `tasks` 里的 `"add one new task"` 不完全一样，所以程序没有把它识别成已完成。
- What I understood after fixing it: `for task in tasks:` 的意思是从 `tasks` 列表里一个一个取出任务，放进变量 `task`，再执行下面缩进的代码。列表里的字符串要完全一样，`if task in completed_tasks:` 才会判断为已完成。修正后，4 个任务里完成了 3 个，还剩 1 个。

## 2026-06-15

Stage: Week 1 - Python basics, Day 4.

Today's target:

- [x] Run `scripts/python_basics_day4.py`.
- [x] Change one status code in `status_codes`.
- [x] Add one more status code.
- [x] Explain what `return` does.
- [x] Explain why each status code gets `ok`, `warn`, or `fail`.

Notes:

- What I tried: 我修改了 `status_codes` 列表，加入了 `333`、`444`、`555` 和 `111`，然后重新运行 Day 4 脚本，观察每个状态码对应的结果。
- What failed: 暂时没有报错。
- What I understood after fixing it: `return` 的作用是把函数算出来的结果返回给调用它的地方使用。这里 `label = get_status_label(code)` 就是在接住函数返回的值。200 到 399 返回 `ok`，400 到 499 返回 `warn`，其他情况返回 `fail`，所以 `111` 会得到 `fail`。

## 2026-06-15

Stage: Week 1 - Python basics, Day 5.

Today's target:

- [x] Run `scripts/hello_cli.py lenxuan`.
- [x] Try running the script without a name.
- [x] Explain what `sys.argv` is.
- [x] Explain what `sys.argv[1]` means.

Notes:

- What I tried: 我运行了 `python .\scripts\hello_cli.py lenxuan`，也运行了不带名字的命令，观察两种输出。
- What failed: 一开始不理解为什么 `len(sys.argv) != 2` 不能改成判断 0，也不理解 `name = sys.argv[1]` 是什么意思。
- What I understood after fixing it: `sys.argv` 是 Python 接收命令行参数的列表，里面至少包含脚本文件名。`sys.argv[0]` 是脚本名，`sys.argv[1]` 是命令后面输入的第一个真正有用的参数，比如 `lenxuan`。`len(sys.argv) != 2` 是为了保证输入刚好是“脚本名 + 一个名字”。

## 2026-06-15

Stage: Week 1 - Day 6-7 review.

Today's target:

- [x] Run Day 0 to Day 5 scripts again.
- [x] Review what each script taught me.
- [x] Connect Week 1 basics to `site_probe.py`.
- [x] Decide not to start `cert_days_left.py` yet.

Notes:

- What I tried: 我重新运行了 Day 0 到 Day 5 的所有脚本，并检查了 `site_probe.py` 和 `cert_days_left.py` 的 TODO。
- What failed: 暂时没有报错，但 `site_probe.py` 和 `cert_days_left.py` 还没有实现。
- What I understood after fixing it: Week 1 学到的 `sys.argv`、函数、`return`、`if`、列表和循环，已经足够开始实现 `site_probe.py`。证书检测涉及 SSL 和日期，暂时先不碰。

## 2026-06-15

Stage: First real tool - `site_probe.py`.

Today's target:

- [x] Implement `probe_url(url)` by myself.
- [x] Read URL from `sys.argv[1]`.
- [x] Return HTTP status code from the function.
- [x] Print `OK` for 2xx/3xx status codes.
- [x] Print `WARN` for 4xx/5xx status codes.
- [x] Record what I tried before asking AI to review.

Notes:

- What I tried: 我先用 `print("收到的 url 是:", url)` 和 `return 200` 确认函数真的收到了参数。然后我一步一步加入 `urlopen`、`response.status`，最后再加入 `HTTPError` 处理。
- What failed: 一开始被缩进卡住，出现了 `IndentationError`。另外如果不处理 `HTTPError`，404 不会走到后面的 `WARN` 判断。
- What I understood after fixing it: `urlopen` 负责真正访问网站，`response.status` 是真实状态码，`return` 会把状态码交回给 `main()`。404 这种情况会变成 `HTTPError`，但错误对象里也有 `exc.code`，所以仍然可以返回给后面的 `if` 判断。

## 2026-06-15

Stage: First real TLS tool practice - `cert_days_left.py`.

Today's target:

- [x] Rebuild the tool step by step without copying the final file.
- [x] Read `hostname` from the command line.
- [x] Connect to port `443`.
- [x] Upgrade the socket to a TLS connection.
- [x] Read certificate expiry time and calculate remaining days.
- [x] Explain the full flow in plain words.

Notes:

- What I tried: 我新建了 `scripts/cert_days_left_rebuild.py`，没有直接照搬最终版，而是从 `sys.argv`、`socket.create_connection`、`wrap_socket`、`getpeercert(binary_form=True)` 一步一步往上搭。最后我把中间调试输出删掉，只保留 `OK ... certificate expires in ... days` 的结果。
- What failed: 中间我把 `_test_decode_cert` 手误写成了 `_text_decode_cert`，Python 报了 `AttributeError`。另外我一开始还是更像跟着敲，还不能完整手写。
- What I understood after fixing it: 这个工具的大流程是读取网址名称，连接 `443` 端口，把普通连接变成 TLS 连接，拿到证书内容，读出 `notAfter`，把时间字符串转成 `datetime`，再和当前时间相减得到剩余天数。现在我还不能完全默写，但已经能口头讲清楚主流程，也能在提示下自己把它重新搭出来。

## 2026-06-17

Stage: `site_probe.py` exception handling review.

Today's target:

- [x] Re-run `site_probe.py` with HTTP, 404, HTTPS, and timeout cases.
- [x] Explain `main() -> probe_url() -> urlopen()` in my own words.
- [x] Add timeout handling.
- [x] Add SSL certificate verification error handling.
- [x] Make failure output clean without traceback.

Notes:

- What I tried: 我重新运行了 `site_probe.py`，分别测试了 `http://example.com`、`http://example.com/does-not-exist`、`https://example.com` 和 `http://no-such-host.invalid`，然后根据输出补上了 timeout 和 SSL verify error 的异常处理。
- What failed: 一开始访问 `http://no-such-host.invalid` 会直接出现 traceback，因为 `TimeoutError` 没有被单独处理。访问 `https://example.com` 时也会因为证书校验失败报错。
- What I understood after fixing it: `main()` 先检查命令行参数个数是不是 2，也就是脚本名加 1 个 URL。如果不是，就输出正确用法并结束。参数正确时，把 `sys.argv[1]` 赋值给 `url`，然后调用 `probe_url(url)`。`probe_url(url)` 会用 `urlopen()` 真正访问网站；如果访问成功，就返回状态码；如果是 404 这种 `HTTPError`，也不会直接报错退出，而是把状态码返回给 `main()`。`main()` 拿到状态码后，再判断 200 到 399 输出 `OK`，其他状态码输出 `WARN`。如果请求过程中出现超时、SSL 证书校验失败或其他请求错误，就进入异常处理，输出对应的 `FAIL` 信息，并直接结束程序。
