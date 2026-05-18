# 用法：修改完 数据结构 里的文件后，运行此脚本一键推送
# 在终端执行：.\push.ps1 "你的提交信息"

param(
    [Parameter(Mandatory=$true)]
    [string]$msg
)

$dsa = "数据结构"

Write-Host ">>> 推送 dsa 仓库..." -ForegroundColor Cyan
Set-Location $dsa
git add -A
git commit -m $msg
if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 1) { throw "dsa commit 失败" }
git push origin main
if ($LASTEXITCODE -ne 0) { throw "dsa push 失败" }

Set-Location ..

Write-Host ">>> 推送 learning_plan 仓库..." -ForegroundColor Cyan
git add $dsa
git commit -m "chore: 更新 数据结构 子模块（$msg）"
if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 1) { throw "learning_plan commit 失败" }
git push origin main
if ($LASTEXITCODE -ne 0) { throw "learning_plan push 失败" }

Write-Host ">>> 完成！" -ForegroundColor Green
