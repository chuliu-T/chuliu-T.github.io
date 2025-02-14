<template>
  <div class="register-container">
    <el-card class="register-card">
      <h2>注册</h2>
      <el-form :model="form" @submit.prevent="handleRegister">
        <el-form-item label="邮箱">
          <el-input v-model="form.email" type="email" placeholder="请输入邮箱"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item label="确认密码">
          <el-input v-model="form.confirmPassword" type="password" placeholder="请确认密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit" :loading="loading">注册</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { auth } from '../api'

const router = useRouter()
const loading = ref(false)
const form = ref({
  email: '',
  password: '',
  confirmPassword: ''
})

const handleRegister = async () => {
  if (form.value.password !== form.value.confirmPassword) {
    ElMessage.error('两次输入的密码不一致')
    return
  }

  try {
    loading.value = true
    await auth.register(form.value.email, form.value.password)
    ElMessage.success('注册成功，请登录')
    router.push('/login')
  } catch (error) {
    ElMessage.error(error.response?.data?.detail || '注册失败')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.register-card {
  width: 400px;
}
</style> 