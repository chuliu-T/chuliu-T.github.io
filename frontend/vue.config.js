const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://106.14.91.113:8900',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''  // 移除前缀 /api
        }
      }
    }
  }
})