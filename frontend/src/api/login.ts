import apiClient from './axios'
import type { Router } from 'vue-router'

interface LoginPayload {
  email: string
  password: string
}

/**
 * ログイン処理
 * @param payload ユーザー名とパスワード
 * @returns アクセストークン（成功時）
 */
export async function login(payload: LoginPayload): Promise<string> {
  try {
    const response = await apiClient.post('/api/token/', payload)
    
    const accessToken = response.data.access
    const refreshToken = response.data.refresh

    localStorage.setItem('access_token', accessToken)
    localStorage.setItem('refresh_token', refreshToken)
    
    return accessToken
  } catch (error: any) {
    throw new Error(error?.response?.data?.detail || 'ログインに失敗しました')
  }
}

/**
 * ログアウト処理
 * ローカルストレージのトークンを削除し、ログイン画面へリダイレクト
 */
export function logout(router: Router): void {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  router.push('/login')
}