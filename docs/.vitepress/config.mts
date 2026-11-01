import { defineConfig } from 'vitepress'
import { base, lang, title, description } from './config/site'
import { nav } from './config/nav'
import { sidebar } from './config/sidebar'
import { markdown } from './config/markdown'
import { head } from './config/head'

export default defineConfig({
  lang,
  title,
  description,
  base,
  head,
  markdown,

  themeConfig: {
    logo: '/logo.svg',
    nav,
    sidebar,
  },
})
