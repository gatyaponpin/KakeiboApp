<template>
  <div>
    <h2>新規収支追加</h2>
    <form @submit.prevent="submit">
      <div>
        <label>日付</label>
        <input type="date" v-model="date" required />
      </div>
      <div>
        <label>カテゴリ</label>
        <input type="text" v-model="category" required />
      </div>
      <div>
        <label>金額</label>
        <input type="number" v-model.number="amount" required />
      </div>
      <button type="submit">追加</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useKakeiboStore } from '@/store/kakeibo'

const store = useKakeiboStore()
const router = useRouter()

const date = ref('')
const category = ref('')
const amount = ref(0)

const submit = () => {
  store.addRecord({
    date: date.value,
    category: category.value,
    amount: amount.value
  })
  router.push('/')
}
</script>