import type { DefaultTheme } from 'vitepress'

// 侧边栏按七大章节分组；新增章节只需在此追加
export const sidebar: DefaultTheme.Sidebar = {
  '/introduction/': [
    {
      text: '绪论',
      items: [
        { text: '概述', link: '/introduction/' },
        { text: '离散元是什么', link: '/introduction/what-is-dem' },
        { text: 'PFC2D 简介', link: '/introduction/what-is-pfc2d' },
      ],
    },
  ],
  '/guide/': [
    {
      text: '操作教程',
      items: [
        { text: '概述', link: '/guide/' },
        { text: '安装与授权', link: '/guide/installation' },
        { text: '界面与工作区', link: '/guide/interface' },
        { text: '基本建模流程', link: '/guide/basic-workflow' },
      ],
    },
  ],
  '/theory/': [
    {
      text: '理论知识',
      items: [
        { text: '概述', link: '/theory/' },
        { text: '基本方程与时间步', link: '/theory/dem-basics' },
        { text: '接触模型', link: '/theory/contact-models' },
        { text: '参数标定', link: '/theory/material-calibration' },
      ],
    },
  ],
  '/fish/': [
    {
      text: 'FISH 脚本示例',
      items: [
        { text: '概述', link: '/fish/' },
        { text: '语法与常用命令', link: '/fish/basics' },
      ],
    },
  ],
  '/examples/': [
    {
      text: '工程案例',
      items: [
        { text: '概述', link: '/examples/' },
        { text: '单轴压缩', link: '/examples/uniaxial-compression' },
        { text: '直剪试验', link: '/examples/direct-shear' },
      ],
    },
  ],
  '/faq/': [
    {
      text: '常见问题',
      items: [{ text: '概述', link: '/faq/' }],
    },
  ],
  '/reference/': [
    {
      text: '官方文档速查',
      items: [{ text: '概述', link: '/reference/' }],
    },
  ],
}
