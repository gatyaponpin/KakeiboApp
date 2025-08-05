import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  withCredentials: false,
  timeout: 10000,
})

const getAccessToken = () => localStorage.getItem('access_token')
const getRefreshToken = () => localStorage.getItem('refresh_token')

// リクエストに自動で認証ヘッダーを付与
apiClient.interceptors.request.use((config) => {
  const token = getAccessToken()
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// 401 エラーの時にリフレッシュ試行
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    // アクセス拒否 かつ リトライ前ならリフレッシュ実行
    if (
      error.response?.status === 401 &&
      !originalRequest._retry &&
      getRefreshToken()
    ) {
      originalRequest._retry = true
      try {
        const res = await axios.post(`${apiClient.defaults.baseURL}/api/token/refresh/`, {
          refresh: getRefreshToken(),
        })

        const newAccessToken = res.data.access
        localStorage.setItem('access_token', newAccessToken)

        // 更新されたトークンで再リクエスト
        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`
        return apiClient(originalRequest)
      } catch (refreshError) {
        console.error('リフレッシュ失敗:', refreshError)
        // ログアウト等の処理
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        window.location.href = '/login' // または router.push('/login')
      }
    }

    return Promise.reject(error)
  }
)

export default apiClient