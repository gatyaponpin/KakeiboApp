<script setup lang="ts">
import { ref, onMounted } from 'vue'
import OverviewCard from './Molecules/OverviewCard.vue'
import { KakeiboSummaryItem, fetchKakeiboSummary } from '@/api/home'

interface Overview {
  name: string
  money: number
}

const overviews = ref<Overview[]>([])

onMounted(async () => {
  try {
    const summary: KakeiboSummaryItem = await fetchKakeiboSummary()

    overviews.value = [
      { name: '収入', money: summary.income },
      { name: '支出', money: summary.expense },
      { name: '残金', money: summary.balance }
    ]
  } catch (error) {
    console.error('収支サマリの取得に失敗しました', error)
  }
})
</script>

<template>
  <v-row>
    <div v-for="(overview, index) of overviews" :key="index">
      <OverviewCard :name="overview.name" :money="overview.money"/>
    </div>
  </v-row>
</template>