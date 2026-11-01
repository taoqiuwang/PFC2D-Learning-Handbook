# PFC2D-Learning-Handbook · 架构设计

> 技术栈：VitePress + Markdown + Vue 3 + MathJax 3（markdown-it-mathjax3）+ Git/GitHub + GitHub Actions
> 定位：专业技术类在线电子书，系统整理 PFC2D 官方帮助文档、理论知识、操作教程、代码示例、工程案例与常见问题。

## 一、总体架构设计原则

架构以「模块化、易维护、便于长期扩展」为核心目标，遵循以下原则：

- **配置与内容分离**：站点根目录 `docs/` 作为 VitePress 的 `srcDir`，配置集中在 `docs/.vitepress/`，内容集中在 `docs/<章节>/`，仓库根目录留白给未来的脚本、工具、数据。
- **配置模块化**：`config.mts` 只做汇总，导航 / 侧边栏 / Markdown 扩展 / 元信息各自独立成文件；新增章节只需改 `sidebar.ts`，互不干扰。
- **内容按七大板块组织**：绪论 / 操作教程 / 理论知识 / FISH 代码 / 工程案例 / FAQ / 官方文档速查，每块独立目录。
- **资源与代码集中管理**：图片统一进 `assets/`，FISH 脚本统一进 `code/`，Markdown 用 `<<< @/code/...` 引用脚本，保证代码单一来源、避免重复复制。
- **交互组件独立**：Vue 3 组件统一放 `.vitepress/theme/components/`，全局注册后可在任意 Markdown 中复用（用于未来的 DEM 参数交互演示）。

## 二、技术栈与版本约束

| 项 | 约定 |
|----|------|
| 运行时 | Node.js **22 或更高**的受支持版本 |
| 站点框架 | VitePress（最新稳定版） |
| 内容格式 | Markdown |
| 前端交互 | Vue 3 |
| 数学公式 | `markdown-it-mathjax3`（MathJax 3），通过 `markdown.config` 注册 |
| 包管理器 | pnpm，`pnpm-lock.yaml` 为**唯一**锁文件 |
| 模块规范 | ESM，`package.json` 中设置 `"type": "module"` |
| 版本管理 / 托管 | Git / GitHub |
| 部署 | GitHub Actions 构建并发布到 GitHub Pages |

## 三、项目目录结构

```
PFC2D-Learning-Handbook/
├── docs/                              # VitePress 站点根（srcDir）
│   ├── .vitepress/
│   │   ├── config.mts                 # 配置入口：defineConfig 汇总
│   │   ├── config/
│   │   │   ├── nav.ts                 # 顶部导航
│   │   │   ├── sidebar.ts             # 侧边栏（按七大章节分组）
│   │   │   ├── markdown.ts            # Markdown 扩展（MathJax3、代码引用）
│   │   │   └── head.ts                # <head> 元信息 / favicon
│   │   ├── theme/
│   │   │   ├── index.ts               # 主题入口，注册全局 Vue 组件
│   │   │   ├── style.css              # 自定义样式变量、配色
│   │   │   └── components/            # 全局交互组件
│   │   │       └── DemoTool.vue       # 示例：DEM 参数交互演示
│   │   └── cache/                     # 构建缓存（.gitignore）
│   ├── public/                        # 静态资源（原样拷贝）
│   │   ├── logo.svg
│   │   └── favicon.ico
│   ├── assets/                        # 图片 / GIF / 示意图
│   │   ├── images/
│   │   └── gifs/
│   ├── code/                          # FISH 示例脚本（供 Markdown 引用）
│   │   └── fish/
│   ├── index.md                       # 首页
│   ├── introduction/                  # ① 绪论
│   │   ├── index.md
│   │   ├── what-is-dem.md             #   离散元是什么
│   │   └── what-is-pfc2d.md           #   PFC2D 简介
│   ├── guide/                         # ② 操作教程
│   │   ├── index.md
│   │   ├── installation.md            #   安装与授权
│   │   ├── interface.md               #   界面与工作区
│   │   └── basic-workflow.md          #   基本建模流程
│   ├── theory/                        # ③ 理论知识
│   │   ├── index.md
│   │   ├── dem-basics.md              #   基本方程与时间步
│   │   ├── contact-models.md          #   接触模型
│   │   └── material-calibration.md    #   参数标定
│   ├── fish/                          # ④ FISH 脚本示例
│   │   ├── index.md
│   │   └── basics.md                  #   语法与常用命令
│   ├── examples/                      # ⑤ 工程案例
│   │   ├── index.md
│   │   ├── uniaxial-compression.md    #   单轴压缩
│   │   └── direct-shear.md            #   直剪试验
│   ├── faq/                           # ⑥ 常见问题
│   │   └── index.md
│   └── reference/                     # ⑦ 官方文档整理 / 速查
│       └── index.md
├── .github/
│   └── workflows/
│       └── deploy.yml                 # GitHub Actions：构建 + 部署 GitHub Pages
├── .gitignore
├── package.json                       # 含 "type": "module"
├── pnpm-lock.yaml                     # 唯一锁文件
├── LICENSE
└── README.md
```

> 说明：
> - 章节内部目录（如 `theory/`、`examples/`）未来按内容量可继续下钻成子目录，无需改动整体框架。
> - **仅维护 `pnpm-lock.yaml`**，不生成 / 提交 `package-lock.json` 或 `yarn.lock`。

## 四、模块化配置设计

| 文件 | 职责 |
|------|------|
| `config.mts` | 配置入口，用 `defineConfig` 汇总各子模块，只负责组装 |
| `config/nav.ts` | 顶部导航栏定义 |
| `config/sidebar.ts` | 侧边栏定义，按七大章节分组；新增章节只改此处 |
| `config/markdown.ts` | Markdown 扩展：注册 `markdown-it-mathjax3`、代码块/引用相关配置 |
| `config/head.ts` | `<head>` 元信息、favicon、SEO、社交标签 |
| `theme/index.ts` | 主题入口，`enhanceApp` 中注册全局 Vue 组件 |
| `theme/style.css` | 自定义 CSS 变量、配色、暗色模式微调 |
| `theme/components/` | 全局可复用的 Vue 3 交互组件 |

## 五、关键配置要点

| 项 | 方案 |
|----|------|
| 站点基路径 | `base: '/PFC2D-Learning-Handbook/'`，**必须与实际仓库名一致**；若仓库改名则同步修改 |
| 语言与标题 | `lang: 'zh-CN'`，`title: 'PFC2D 学习与研究手册'` |
| 数学公式 | 使用 `markdown-it-mathjax3`（MathJax 3），通过 `markdown.config` 注册；**不使用** `markdown.math: true`（它并非 VitePress 内建 KaTeX） |
| 代码引用 | `<<< @/code/fish/xxx.fis` 引用外部脚本，保证代码单一来源 |
| FISH 展示 | 初期以**普通文本（`text`）**方式展示 FISH 文件；后续再通过自定义 Shiki 语言定义补充语法高亮 |
| 模块规范 | `package.json` 设置 `"type": "module"`，配置采用 ESM（`.mts` / `.ts`） |
| 锁文件 | `pnpm-lock.yaml` 为唯一锁文件，全程使用 pnpm，避免混用 npm/yarn 生成额外锁文件 |
| 部署触发 | push 到 `main` → 自动构建 → 发布 Pages |

### 数学公式配置示例

```ts
// docs/.vitepress/config.mts（示意）
import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'

export default defineConfig({
  lang: 'zh-CN',
  title: 'PFC2D 学习与研究手册',
  base: '/PFC2D-Learning-Handbook/',
  markdown: {
    config: (md) => {
      md.use(mathjax3) // 由 MathJax 3 渲染 TeX 公式
    },
  },
})
```

### package.json 约定（示意）

```json
{
  "name": "pfc2d-learning-handbook",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vitepress dev docs",
    "build": "vitepress build docs",
    "preview": "vitepress preview docs"
  },
  "devDependencies": {
    "vitepress": "^1.x",
    "markdown-it-mathjax3": "^4.x"
  }
}
```

## 六、实施计划

### 阶段 1 — 项目初始化
1. 确认 Node.js（**≥ 22**）与 pnpm 已安装
2. 创建 `package.json`（含 `"type": "module"`），安装 `vitepress` 与 `markdown-it-mathjax3`
3. 建立最小 `config.mts`：`base` / `title` / `lang` / MathJax3 注册
4. 建首页 `docs/index.md` 与目录骨架
5. 本地 `pnpm vitepress dev docs` 跑通预览

### 阶段 2 — 配置模块化
1. 拆出 `nav.ts` / `sidebar.ts` / `markdown.ts` / `head.ts`
2. 通过 `markdown-it-mathjax3` 启用数学公式
3. 配置暗色模式、logo、favicon、中文样式
4. 建 `.vitepress/theme/index.ts`，预留全局组件注册

### 阶段 3 — 目录与导航骨架
1. 建立七大章节的 `index.md` 占位页
2. 配置侧边栏分组与顶部导航
3. 打通首页 → 各章节 → 子页的完整导航

### 阶段 4 — 内容生产（长期，按优先级）
1. 优先：`reference/`（官方文档整理）与 `guide/`（操作教程）——最快形成实用价值
2. 其次：`theory/`（理论 + 公式）、`fish/`（代码示例，初期纯文本展示）
3. 再次：`examples/`（工程案例）、`faq/`（常见问题）
4. 建立内容规范：文件命名、frontmatter、公式/代码/图片引用约定

### 阶段 5 — 自动部署 CI/CD
1. 编写 `.github/workflows/deploy.yml`（checkout → pnpm 安装 → `vitepress build docs` → 上传 Pages artifact）
2. 在 GitHub 仓库 Settings → Pages 开启 `GitHub Actions` 来源
3. 验证 `base` 路径与仓库名一致，确认 `https://taoqiuwang.github.io/PFC2D-Learning-Handbook/` 正常访问

### 阶段 6 — 持续扩展
1. 交互式 DEM 参数演示组件（Vue 3 + MathJax）
2. 自定义 Shiki 语言定义，为 FISH 补充语法高亮
3. 本地/全文搜索优化
4. 随 PFC2D 版本迭代补充内容
