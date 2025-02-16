const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://106.14.91.113:8000',
        changeOrigin: true,
        // 只保留一种路径重写方式
        pathRewrite: { '^/api': '' }
      }
    }
  }
})
// vue.config.js
