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
