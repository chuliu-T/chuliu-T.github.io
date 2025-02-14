<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card>
          <template #header>
            <div class="card-header">
              <span>CMDB 统计</span>
            </div>
          </template>
          <div class="item-count">
            <h3>{{ itemCount }}</h3>
            <p>总项目数</p>
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <template #header>
            <div class="card-header">
              <span>用户信息</span>
            </div>
          </template>
          <div class="user-info">
            <p>邮箱：{{ userInfo.email }}</p>
            <p>状态：{{ userInfo.is_active ? '活跃' : '禁用' }}</p>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { cmdb, users } from '../api'

const itemCount = ref(0)
const userInfo = ref({})

onMounted(async () => {
  try {
    const [itemsResponse, userResponse] = await Promise.all([
      cmdb.getItems(),
      users.getProfile()
    ])
    itemCount.value = itemsResponse.data.length
    userInfo.value = userResponse.data
  } catch (error) {
    console.error('Failed to load dashboard data:', error)
  }
})
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
}

.card-header {
  font-weight: bold;
}

.item-count {
  text-align: center;
}

.item-count h3 {
  font-size: 2em;
  margin: 0;
}
</style> 