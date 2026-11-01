import DefaultTheme from 'vitepress/theme'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // 预留：在此注册全局 Vue 3 组件
    // 示例：app.component('DemoTool', DemoTool)
  },
}
