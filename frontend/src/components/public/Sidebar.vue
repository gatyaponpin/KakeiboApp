<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { logout } from '@/api/login' // 共通化されたログアウト関数

const router = useRouter()

const isRail = ref(true)

const handleLogout = () => {
  logout(router)
  router.push('/login')
}
</script>

<template>
  <v-navigation-drawer :width="200" expand-on-hover v-model:rail="isRail">
    <v-list nav dense>
      <v-list-item prepend-icon="mdi-home" value="home" to="/home">
        <v-list-item-title>ホーム</v-list-item-title>
      </v-list-item>
      <v-list-item prepend-icon="mdi-cash-multiple" value="list" to="/list">
        <v-list-item-title>収支</v-list-item-title>
      </v-list-item>
      <!-- <v-list-item prepend-icon="mdi-sack" value="saving" to="/saving">
        <v-list-item-title>貯蓄</v-list-item-title>
      </v-list-item>
      <v-list-item prepend-icon="mdi-finance" value="graph" to="/graph">
        <v-list-item-title>グラフ</v-list-item-title>
      </v-list-item>
      <v-list-item prepend-icon="mdi-calendar-month" value="calendar" to="/calendar">
        <v-list-item-title>カレンダー</v-list-item-title>
      </v-list-item>
      <v-list-item prepend-icon="mdi-bitcoin" value="investment" to="/investment">
        <v-list-item-title>投資</v-list-item-title>
      </v-list-item>
      <v-list-item prepend-icon="mdi-cog" value="setting" to="/setting">
        <v-list-item-title>設定</v-list-item-title>
      </v-list-item> -->
    </v-list>

    <template #append>
      <div v-if="!isRail" class="pa-2">
        <v-btn block @click="handleLogout">
          <v-icon start>mdi-logout</v-icon>
          ログアウト
        </v-btn>
      </div>
    </template>
  </v-navigation-drawer>
</template>