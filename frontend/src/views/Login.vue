<template>
  <v-container>
     <v-card max-width="500" class="mx-auto">
      <v-card-actions>
        <v-col>
          <v-form @submit.prevent="handleLogin" class="mt-8" ref="form">
            <v-text-field v-model="email" label="メールアドレス" required />
            <v-text-field v-model="password" label="パスワード" type="password" required />
            <v-btn type="submit" color="primary" :loading="loading">ログイン</v-btn>
            <v-alert v-if="errorMessage" type="error" class="mt-4">{{ errorMessage }}</v-alert>
          </v-form>
        </v-col>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '@/api/login'

const router = useRouter()

const email = ref('')
const password = ref('')
const loading = ref(false)
const errorMessage = ref('')

const handleLogin = async () => {
  errorMessage.value = ''
  loading.value = true
  try {
    const token = await login({ email: email.value, password: password.value })
    localStorage.setItem('access_token', token)
    router.push('/')
  } catch (error: any) {
    errorMessage.value = error.message
  } finally {
    loading.value = false
  }
}
</script>