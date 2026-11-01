import type { HeadConfig } from 'vitepress'
import { base, title, description } from './site'

export const head: HeadConfig[] = [
  ['link', { rel: 'icon', href: `${base}logo.svg`, type: 'image/svg+xml' }],
  ['meta', { name: 'theme-color', content: '#2563eb' }],
  ['meta', { property: 'og:type', content: 'website' }],
  ['meta', { property: 'og:title', content: title }],
  ['meta', { property: 'og:description', content: description }],
]
