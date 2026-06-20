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

## 2026-06-17

Stage: First FastAPI API practice.

Today's target:

- [x] Create the first FastAPI app entry.
- [x] Add `/` and `/health` routes.
- [x] Install FastAPI and Uvicorn in a local `.venv`.
- [x] Reuse `probe_url(url)` inside a `/probe` route.
- [x] Return JSON for both `200` and `404` cases.

Notes:

- What I tried: 我先创建了 `app.py` 和 `requirements.txt`，再在本地 `.venv` 里安装 FastAPI、Pydantic 和 Uvicorn。然后我把 `site_probe.py` 里的 `probe_url(url)` 逻辑搬到 `app.py`，写了 `/probe` 路由，并测试了 `http://example.com` 和 `http://example.com/does-not-exist`。
- What failed: 一开始我把命令行脚本的 `sys.argv` 写法直接放进了 `app.py` 顶层，导致 FastAPI 导入文件时就报错。后面我还把返回字段名写错过，也遇到过旧进程没有重启、浏览器结果和文件内容对不上的情况。
- What I understood after fixing it: 命令行脚本是启动后立刻往下执行，所以会用 `sys.argv` 和 `print()`；FastAPI 则是在收到请求后才进入路由函数，所以要用函数参数接收 `url`，再用 `return` 返回字典，让 FastAPI 自动变成 JSON。现在 `/probe` 已经能返回 `url`、`status_code` 和 `result`，并正确区分 `200` 的 `ok` 和 `404` 的 `warn`。

## 2026-06-18

Stage: `/probe` exception handling in FastAPI.

Today's target:

- [x] Re-test `/probe` with `200`, `404`, HTTPS SSL error, and timeout cases.
- [x] Add timeout handling in the FastAPI route.
- [x] Add SSL certificate verification error handling in the FastAPI route.
- [x] Return JSON errors instead of `500 Internal Server Error`.
- [x] Explain the difference between CLI `print()` output and API `return` JSON.

Notes:

- What I tried: 我继续修改了 `app.py` 里的 `/probe` 路由，测试了 `http://example.com`、`http://example.com/does-not-exist`、`https://example.com` 和 `http://no-such-host.invalid`。我把 `site_probe.py` 里学过的超时和 SSL 错误处理思路迁到了 FastAPI 路由里。
- What failed: 一开始 `/probe` 遇到 HTTPS 证书错误和无效主机时会直接变成 `500`。中间我还漏过 `urllib.error` 的导入，也试过把 `exc.reason` 直接原样返回，结果不够稳定、不够清楚。
- What I understood after fixing it: CLI 脚本里异常可以用 `print()` 告诉终端发生了什么，但 FastAPI 路由里不能让异常直接冒出去，否则浏览器只会看到 `500`。现在 `/probe` 会自己接住异常，再 `return` 一个 JSON 结果：正常请求返回 `ok` 或 `warn`，HTTPS 证书校验失败返回 `ssl certificate verification error`，超时返回 `timeout`。这样 API 调用方就能稳定拿到结构化结果，而不是只看到报错页面。

## 2026-06-18

Stage: First `/cert` route in FastAPI.

Today's target:

- [x] Reuse `get_cert_expiry()` and `days_until()` inside `app.py`.
- [x] Add a `/cert` route that accepts `hostname`.
- [x] Return certificate expiry information as JSON.
- [x] Return a JSON error instead of crashing when TLS lookup fails.
- [x] Verify both a real hostname and an invalid hostname.

Notes:

- What I tried: 我在 `app.py` 顶部导入了 `get_cert_expiry` 和 `days_until`，然后新增了 `/cert` 路由，测试了 `example.com` 和 `no-such-host.invalid`。成功时我返回 `hostname`、`expires_at`、`days_left` 和 `result`，失败时返回 `tls_error` 和错误信息。
- What failed: 一开始我把 `ssl` 手误写成了 `sll`，还把字段名写成过 `expiry_at` 和 `adays_left`，所以错误分支没有正确接住，返回字段名也不统一。
- What I understood after fixing it: 这次我不需要重新手写证书计算逻辑，只要把 CLI 脚本里已经写好的函数复用到 FastAPI 路由里就行。API 路由的重点是把函数结果整理成 JSON 返回；如果查询失败，也要返回结构化错误，而不是让异常直接冒出去。

## 2026-06-18

Stage: FastAPI `response_model` and `BaseModel`.

Today's target:

- [x] Add clear response models for `/`, `/health`, `/probe`, and `/cert`.
- [x] Make Swagger show fixed fields instead of a generic dictionary shape.
- [x] Understand what `BaseModel` does.
- [x] Understand what `response_model` does.

Notes:

- What I tried: 我在 `app.py` 里新增了 `RootResponse`、`HealthResponse`、`ProbeResponse` 和 `CertResponse`，然后把它们分别挂到对应路由的 `response_model` 上。
- What failed: 之前没有响应模型时，Swagger 只能把返回值显示成很模糊的通用字典，看起来像 `additionalProp1` 这种结构，不方便我看清接口到底应该返回什么字段。
- What I understood after fixing it: `BaseModel` 就像先把“返回数据的字段表”写出来，比如 `/probe` 必须有 `url`、`status_code` 和 `result`。`response_model` 则是把这张字段表绑定到具体路由上，告诉 FastAPI 这个接口应该按这个结构返回，也让 Swagger 文档显示得更清楚。这样我不只是“接口能跑”，而是连接口长什么样也固定下来了。

## 2026-06-18

Stage: Reuse existing probe logic in FastAPI.

Today's target:

- [x] Import `probe_url()` from `scripts/site_probe.py` instead of keeping a copied version in `app.py`.
- [x] Keep `/probe` behavior consistent after switching to the shared function.
- [x] Clean up `app.py` formatting and spacing.

Notes:

- What I tried: 我先尝试把 `probe_url()` 复用到 `app.py` 里，后来发现一开始导错了来源文件，随后改成从 `scripts/site_probe.py` 正确导入。最后我顺手把 `app.py` 的空行、缩进和空格也整理了一遍。
- What failed: 最开始我把 `probe_url` 误从 `cert_days_left.py` 里导入，导致 `app.py` 直接 `ImportError`，接口都起不来。
- What I understood after fixing it: 已经写好的核心逻辑，优先应该复用，而不是在另一个文件里再抄一遍。这样后面如果我要改 `probe_url()` 的行为，只改一处就能同时影响 CLI 和 FastAPI，两边不会越来越不一致。整理格式虽然不改变功能，但会让我以后更容易读懂和维护自己的代码。

## 2026-06-19

Stage: Swagger documentation polish.

Today's target:

- [x] Add API-level description and version information.
- [x] Add route summaries and descriptions.
- [x] Add query parameter descriptions and examples.
- [x] Add field descriptions to response models.
- [x] Make the `/docs` page look closer to a real API document.

Notes:

- What I tried: 我在 `app.py` 的 `FastAPI(...)` 里补了 `description` 和 `version`，又给 `/`、`/health`、`/probe`、`/cert` 加了 `summary` 和 `description`。同时我把 `url`、`hostname` 参数改成了 `Query(...)`，也给响应模型字段补了 `Field(description=...)`。
- What failed: 之前虽然接口能跑，但 Swagger 页面只显示默认标题和很基础的信息，参数和字段的含义不够清楚，看起来还不像一个认真整理过的 API。
- What I understood after fixing it: Swagger 文档不是“自动就够用了”，而是可以通过 `FastAPI(...)`、`summary`、`description`、`Query(...)` 和 `Field(...)` 主动把接口说明写清楚。这样别人打开 `/docs`，不只知道能不能调用，还能更快明白每个接口和字段是什么意思。

## 2026-06-20

Stage: In-memory target management and batch check.

Today's target:

- [x] Keep the in-memory `targets_db` structure as the current storage layer.
- [x] Confirm `GET /targets` and `POST /targets` are part of the current API.
- [x] Add `GET /targets/check` to loop through all stored targets.
- [x] Reuse the existing `/probe` logic for each target instead of writing a second probe flow.
- [x] Update `README.md` so the repo description matches the current real progress.

Notes:

- What I tried: 我先在 `README.md` 里补了当前 FastAPI 进度和运行方式，然后在 `app.py` 里新增了 `TargetCheckResult`、`TargetCheckListResponse` 和 `GET /targets/check`。这个新接口会遍历 `targets_db`，再复用现有的 `/probe` 逻辑给每个目标生成结果。
- What failed: 一开始浏览器里看到 `404`，主要是因为本地运行的服务还是旧代码，没有重新加载到新增的 `/targets` 路由，不是路由设计本身有问题。
- What I understood after fixing it: 真实项目里不能只会检查一个网址，还要先管理“有哪些目标需要检查”。这次的重点不是数据库，而是先把“目标列表 -> 逐个检查 -> 返回批量结果”这条最小主线接起来。这样下一步再换成 SQLite 时，我只是在替换存储层，而不是重新想一遍接口流程。
