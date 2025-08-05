<template>
  <v-container>
    <v-row class="align-center" dense>
      <v-col cols="2">
        <v-select
          v-model="typeFilter"
          :items="typeOptions"
          label="収支"
          clearable
        />
      </v-col>
      <v-col cols="3">
        <v-select
          v-model="categoryFilter"
          :items="categoryOptions"
          label="カテゴリ"
          clearable
        />
      </v-col>
      <v-col cols="3">
        <v-text-field
          v-model="startDate"
          label="開始日"
          type="date"
          clearable
        />
      </v-col>
      <v-col cols="3">
        <v-text-field
          v-model="endDate"
          label="終了日"
          type="date"
          clearable
        />
      </v-col>
    </v-row>

    <v-row dense class="mt-0 mb-3">
      <v-col cols="6" md="6" class="pa-0">
        <span class="font-weight-bold">収入：</span> ¥{{ totalIncome.toLocaleString() }}
      </v-col>
      <v-col cols="6" md="6" class="pa-0">
        <span class="font-weight-bold">支出：</span> ¥{{ totalExpense.toLocaleString() }}
      </v-col>
    </v-row>

    <v-data-table
      :headers="headers"
      :items="filteredRecords"
      class="elevation-1"
      :items-per-page="10"
    />
  </v-container>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { fetchKakeiboList, type KakeiboListItem } from '@/api/list'

const records = ref<KakeiboListItem[]>([])

const typeFilter = ref<number | null>(null)
const categoryFilter = ref<string | null>(null)
const startDate = ref<string | null>(null)
const endDate = ref<string | null>(null)

const typeOptions = [
  { title: '収入', value: 1 },
  { title: '支出', value: 2 },
]

const categoryOptions = ref<{ title: string; value: string }[]>([])

const headers = [
  { title: '日付', key: 'day' },
  { title: 'カテゴリ', key: 'category_name' },
  { title: '名前', key: 'name' },
  { title: '金額', key: 'amount' },
  { title: '種別', key: 'type_label' },
  { title: 'メモ', key: 'memo' },
]

const totalIncome = computed(() =>
  filteredRecords.value
    .filter(item => item.type === 1)
    .reduce((sum, item) => sum + item.amount, 0)
)

const totalExpense = computed(() =>
  filteredRecords.value
    .filter(item => item.type === 2)
    .reduce((sum, item) => sum + item.amount, 0)
)

onMounted(async () => {
  const result = await fetchKakeiboList()
  records.value = result

  // カテゴリ一覧を自動で抽出
  const categorySet = new Set(result.map(item => item.category_name).filter(Boolean))
  categoryOptions.value = Array.from(categorySet).map(name => ({ title: name as string, value: name as string }))
})

// フロント側で全フィルタを実行
const filteredRecords = computed(() => {
  return records.value.filter((item) => {
    const matchType = typeFilter.value ? item.type === typeFilter.value : true
    const matchCategory = categoryFilter.value ? item.category_name === categoryFilter.value : true
    const matchStart = startDate.value ? item.day >= startDate.value : true
    const matchEnd = endDate.value ? item.day <= endDate.value : true
    return matchType && matchCategory && matchStart && matchEnd
  })
})
</script>

