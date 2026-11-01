# PFC2D-Learning-Handbook · 实施计划

> 本文档为实施计划索引。**技术架构、目录结构、配置要点以 [ARCHITECTURE.md](./ARCHITECTURE.md) 为准**，此处不再重复维护，避免两份文档内容漂移。

## 实施计划（分阶段）

### 阶段 1 — 项目初始化
1. 确认 Node.js（≥ 22）与 pnpm 已安装
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
