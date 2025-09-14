#!/usr/bin/env bash
# 一键生成发布副本并推到 GitHub
set -e                                    # 遇到错误立即退出
cd "$(dirname "$0")"                      # 切到 Vault 根目录
echo ">>> 正在生成 deploy 副本..."
python vault2blog.py

echo ">>> 正在推到博客仓库..."
cd deploy
# 第一次运行会自动初始化
if [ ! -d .git ]; then
  git init
  git remote add blog https://github.com/GummyLight/YOYO-Blog.git
fi
git add -A
git commit -m "publish $(date +%F-%H%M)"
git push -f blog main
echo ">>> 完成！GitHub Pages 稍等 30 秒左右即可刷新。"