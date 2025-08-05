import apiClient from './axios'

export interface KakeiboListItem {
  id: number
  name: string
  amount: number
  type: number
  type_label: string
  day: string
  memo: string | null
  category_id: number | null
  category_name: string | null
  created_at: string
}

export const fetchKakeiboList = async (): Promise<KakeiboListItem[]> => {
  const res = await apiClient.get('/api/kakeibo-list/')
  return res.data
}