import axios from 'axios'

const api = axios.create({
  baseURL: 'http://106.14.91.113:8000',  // 直接使用后端地址
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

export const auth = {
  login: (email, password) => 
    api.post('/auth/token', new URLSearchParams({
      username: email,
      password: password
    }).toString(), {
      headers: { 
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }),
  register: (email, password) => 
    api.post('/users', { email, password })
}

export const users = {
  getProfile: () => api.get('/users/me'),
  updateProfile: (data) => api.put('/users/me', data)
}

export const cmdb = {
  getItems: () => api.get('/cmdb'),
  createItem: (data) => api.post('/cmdb', data),
  updateItem: (id, data) => api.put(`/cmdb/${id}`, data),
  deleteItem: (id) => api.delete(`/cmdb/${id}`)
}

export default api