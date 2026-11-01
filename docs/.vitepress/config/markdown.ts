import type { MarkdownOptions } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'

export const markdown: MarkdownOptions = {
  config: (md) => {
    // 数学公式：MathJax 3 渲染（行内 $…$，块级 $$…$$）
    md.use(mathjax3)
  },
}
