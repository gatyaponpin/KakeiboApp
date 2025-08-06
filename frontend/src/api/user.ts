import apiClient from './axios'

export interface RegisterPayload {
  email: string
  username: string
  password: string
}

export async function registerUser(payload: RegisterPayload): Promise<string> {
  try {
    const res = await apiClient.post('/api/register/', payload)
    return res.data.message || '登録に成功しました'
  } catch (err: any) {
    // エラーメッセージの抽出と加工
    const data = err.response?.data
    const message =
      data?.email?.[0] ||
      data?.username?.[0] ||
      data?.password?.[0] ||
      data?.detail ||
      '登録に失敗しました'
    throw new Error(message)
  }
}