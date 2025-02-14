<template>
  <div class="profile-container">
    <el-card>
      <template #header>
        <h2>个人信息</h2>
      </template>

      <el-form :model="form" label-width="100px">
        <el-form-item label="邮箱">
          <el-input v-model="form.email" disabled></el-input>
        </el-form-item>
        <el-form-item label="新密码">
          <el-input v-model="form.password" type="password" placeholder="留空表示不修改"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleUpdate" :loading="loading">
            更新信息
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { users } from '../api'

const loading = ref(false)
const form = ref({
  email: '',
  password: ''
})

const loadProfile = async () => {
  try {
    const response = await users.getProfile()
    form.value.email = response.data.email
  } catch (error) {
    ElMessage.error('加载用户信息失败')
  }
}

const handleUpdate = async () => {
  loading.value = true
  try {
    const updateData = {}
    if (form.value.password) {
      updateData.password = form.value.password
    }
    await users.updateProfile(updateData)
    ElMessage.success('更新成功')
    form.value.password = ''
  } catch (error) {
    ElMessage.error('更新失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadProfile()
})
</script>

<style scoped>
.profile-container {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
}
</style> 