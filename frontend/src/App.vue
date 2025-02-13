<template>
  <div class="app-container">
    <nav class="navbar">
      <div class="logo">CMDB System</div>
      <div class="nav-links" v-if="!isAuthenticated">
        <router-link to="/login">登录</router-link> |
        <router-link to="/register">注册</router-link>
      </div>
      <div class="nav-links" v-else>
        <router-link to="/dashboard">仪表盘</router-link> |
        <router-link to="/cmdb">CMDB</router-link> |
        <router-link to="/profile">个人信息</router-link> |
        <a href="#" @click.prevent="handleLogout">退出</a>
      </div>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'App',
  setup() {
    const router = useRouter()
    const isAuthenticated = ref(false)

    onMounted(() => {
      // 检查本地存储中是否有token
      const token = localStorage.getItem('token')
      isAuthenticated.value = !!token
    })

    const handleLogout = () => {
      localStorage.removeItem('token')
      isAuthenticated.value = false
      router.push('/login')
    }

    return {
      isAuthenticated,
      handleLogout
    }
  }
}
</script>

<style>
.app-container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.navbar {
  padding: 1rem;
  background-color: #f8f9fa;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #2c3e50;
}

.nav-links a {
  color: #2c3e50;
  text-decoration: none;
  margin: 0 0.5rem;
  padding: 0.5rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-links a:hover {
  background-color: #e9ecef;
}

.nav-links a.router-link-active {
  color: #42b983;
  font-weight: bold;
}
</style>
