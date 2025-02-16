const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://106.14.91.113:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
})
