const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://106.14.91.113:8000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }, // 只保留一种重写方式
      },
    },
  },
});