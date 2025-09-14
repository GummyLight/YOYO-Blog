#!/usr/bin/env python3
import re, shutil, pathlib, os

# ==========  只改这里就够了  ==========
GITHUB_USER   = "GummyLight"
GITHUB_REPO   = "YOYO-Blog"
GITHUB_BRANCH = "main"
# ======================================

VAULT_ROOT = pathlib.Path.cwd()                # Vault 根目录
DEPLOY_DIR = VAULT_ROOT / "deploy"             # 临时发布副本
RAW_URL    = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}"

# 1. 清掉旧 deploy
if DEPLOY_DIR.exists():
    shutil.rmtree(DEPLOY_DIR)
DEPLOY_DIR.mkdir()

# 2. 遍历所有 md，跳过符号链接
for root, dirs, files in os.walk(VAULT_ROOT, followlinks=False):
    root = pathlib.Path(root)
    # 跳过隐藏目录 & deploy 自身
    if any(p.startswith('.') for p in root.relative_to(VAULT_ROOT).parts):
        dirs[:] = []
        continue
    if root == DEPLOY_DIR:
        dirs[:] = []
        continue
    for f in files:
        if f.lower().endswith('.md'):
            md = root / f
            out = DEPLOY_DIR / md.relative_to(VAULT_ROOT)
            out.parent.mkdir(parents=True, exist_ok=True)

            text = md.read_text(encoding='utf-8')
            text = re.sub(
                r'!\[\[(public/assets/([^|\]]+?)(?:\|.*?)?)\]\]',
                rf'![\2]({RAW_URL}/\1)',
                text, flags=re.I)
            out.write_text(text, encoding='utf-8')

# 3. 把整个 public/assets 拷过去，保证 CDN 有图
assets_src = VAULT_ROOT / "public" / "assets"
assets_dst = DEPLOY_DIR / "public" / "assets"
if assets_src.exists():
    shutil.copytree(assets_src, assets_dst, dirs_exist_ok=True)

print("✅ 副本已生成在 ./deploy ，可直接 push 到博客仓库。")