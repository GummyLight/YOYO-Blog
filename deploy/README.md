# YOYO-Blog

> 一个由 **VitePress** + **Obsidian** 驱动的「懒人写作 & 一键部署」博客方案  
> 写作在 Obsidian，渲染靠 VitePress，推送用 GitHub Actions —— 全程 10 秒完成发布！

---

## 🧡 特点一览

| 维度 | 方案 |
|---|---|
| **框架** | [VitePress](https://vitepress.dev)（@sugarat/theme 简约风） |
| **写作端** | [Obsidian](https://obsidian.md) + Templater 插件 |
| **部署** | GitHub Pages（全自动构建，零服务器成本） |
| **归档** | 按「年-月-日」自动落入 `docs/posts/YYYY/` |
| **分类** | 单选下拉（A 技术向 / B 生活向 / C 学习向） |
| **标签** | 任意打 `#标签` 或 YAML 数组，自动聚合 |
| **草稿** | `status: draft` 一键隐藏，`published` 秒上线 |

---

## 🚀 10 秒写作→发布流程

1. **Obsidian 里按快捷键** `Ctrl+Alt+N`  
   → 弹窗输入标题 → 自动归档到 `docs/posts/2025/标题.md` + 套模板
2. 属性面板**点两下**（分类、tag）→ 写完 `Ctrl+Shift+G` 一键 commit & push
3. GitHub Actions 自动 `pnpm build` → 站点更新完成！

---

## 📦 快速上手（本地预览）

```bash
# ① 克隆
git clone https://github.com/YOUR_NAME/YOYO-Blog.git
cd YOYO-Blog

# ② 装依赖
npm i -g pnpm
pnpm install

# ③ 启动
pnpm dev
# 打开 http://localhost:5173
```

---

## ⚙️ 一键部署（GitHub Pages）

1. **仓库 Settings → Pages → Source 选 GitHub Actions**
2. **已含 `.github/workflows/deploy.yml`**，无需改动
3. **修改 `docs/.vitepress/config.mts` 的 `base`：**
   ```ts
   const base = '/YOYO-Blog/'   // 改成你的仓库名
   ```
4. **推送到 `main` 分支** → Actions 跑完即可访问 `https://YOUR_NAME.github.io/YOYO-Blog/`

---

## 🧩 目录结构

```
YOYO-Blog/                 ← Vault 根（Obsidian 打开这一层）
├─ .git/                   ← 自动版本控制
├─ docs/
│  ├─ posts/2025/          ← 文章按年归档
│  ├─ public/assets/       ← 图片跟随文章
│  ├─ .vitepress/config.mts← 主题 & 部署配置
│  └─ post/YearIndex.md    ← 手写归档/分类索引页
├─ Templates/              ← Obsidian 模板
│  └─ 博文.md              ← 一键新建 + 自动 YAML
├─ scripts/                ← 批量迁移旧文件夹（一次性）
└─ README.md               ← 本文件
```

---

## 📝 模板字段（实时自动生成）

```yaml
title:        <% tp.file.title %>
date:         <% tp.date.now("YYYY-MM-DD") %>
category:     A 技术向          # 下拉单选
tags:         []                # 多选或 #标签
status:       draft             # 下拉 draft / published
series:       ""                # 连载名（可选）
wordCount:    <% tp.file.content.split(/\s/).filter(s => s).length %>
updated:      <% tp.date.now("YYYY-MM-DD HH:mm") %>
```

> 字数 & 更新时刻可随写随刷，无需手填。

---

## 🎨 主题美化（可扩展）

- 颜色：已内置 `vp-green`，可在 `config.mts` → `themeColor` 切换
- 友链 / 公告 / 搜索框：都在 `blogTheme` 里配置，见文件内注释
- 数学公式：KaTeX + MathJax3 已开箱即用

---

## 🤝 贡献 & 反馈

欢迎提 Issue / PR，或直接在YOYO-BLOG 里添加作者联系方式交流！

---

> 写作愉快，发布轻松，愿你也能 10 秒把灵感推上网！
