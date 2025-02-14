<template>
  <div class="cmdb-container">
    <el-card>
      <template #header>
        <div class="header">
          <h2>CMDB 管理</h2>
          <el-button type="primary" @click="dialogVisible = true">添加项目</el-button>
        </div>
      </template>

      <el-table :data="items" v-loading="loading">
        <el-table-column prop="name" label="名称"></el-table-column>
        <el-table-column prop="type" label="类型"></el-table-column>
        <el-table-column prop="description" label="描述"></el-table-column>
        <el-table-column prop="status" label="状态"></el-table-column>
        <el-table-column label="操作">
          <template #default="scope">
            <el-button size="small" @click="handleEdit(scope.row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 添加/编辑对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="editingItem ? '编辑项目' : '添加项目'"
      width="50%"
    >
      <el-form :model="form" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="类型">
          <el-input v-model="form.type"></el-input>
        </el-form-item>
        <el-form-item label="描述">
          <el-input type="textarea" v-model="form.description"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleSave">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { cmdb } from '../api'

const items = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const editingItem = ref(null)
const form = ref({
  name: '',
  type: '',
  description: ''
})

const loadItems = async () => {
  loading.value = true
  try {
    const response = await cmdb.getItems()
    items.value = response.data
  } catch (error) {
    ElMessage.error('加载数据失败')
  } finally {
    loading.value = false
  }
}

const handleEdit = (item) => {
  editingItem.value = item
  form.value = { ...item }
  dialogVisible.value = true
}

const handleDelete = async (item) => {
  try {
    await ElMessageBox.confirm('确定要删除这个项目吗？', '警告', {
      type: 'warning'
    })
    await cmdb.deleteItem(item.id)
    ElMessage.success('删除成功')
    loadItems()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

const handleSave = async () => {
  try {
    if (editingItem.value) {
      await cmdb.updateItem(editingItem.value.id, form.value)
    } else {
      await cmdb.createItem(form.value)
    }
    ElMessage.success(editingItem.value ? '更新成功' : '添加成功')
    dialogVisible.value = false
    loadItems()
  } catch (error) {
    ElMessage.error(editingItem.value ? '更新失败' : '添加失败')
  }
}

onMounted(() => {
  loadItems()
})
</script>

<style scoped>
.cmdb-container {
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style> 