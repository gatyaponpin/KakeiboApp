<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import CategoryCard from './Molecules/CategoryCard.vue';
  import { fetchBudgetSummary, BudgetSummaryItem } from '@/api/home'
  
  interface BalanceCategory {
    category: string
    budget: number
    used: number
  }

  const balances = ref<BalanceCategory[]>([])

  const loadBalances = async () => {
    try {
      const data: BudgetSummaryItem[] = await fetchBudgetSummary()
      balances.value = data.map(item => ({
        category: item.category_name,
        budget: Number(item.amount),
        used: Number(item.total)
      }))
    } catch (error) {
      console.error('予算サマリの取得に失敗しました', error)
    }
  }

  onMounted(loadBalances)
</script>

<template>
  <v-row>
    <v-col cols="3" v-for="(balance, index) in balances" :key="index">
      <CategoryCard :category="balance.category" :budget="balance.budget" :used="balance.used"/> 
    </v-col>
  </v-row>
</template>