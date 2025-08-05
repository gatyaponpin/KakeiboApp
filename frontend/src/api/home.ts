import apiClient from './axios'

export interface BudgetSummaryItem {
  category_name: string
  amount: number
  total: number
}

export interface KakeiboSummaryItem {
  income: number
  expense: number
  balance : number
}

export const fetchBudgetSummary = async (): Promise<BudgetSummaryItem[]> => {
  const res = await apiClient.get('/api/budget-summary/')
  return res.data
}

export const fetchKakeiboSummary = async (): Promise<KakeiboSummaryItem> => {
  const res = await apiClient.get('/api/kakeibo-summary/')
  return res.data
}