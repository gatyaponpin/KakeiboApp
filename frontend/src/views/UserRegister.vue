<template>
  <v-container class="d-flex justify-center">
    <v-card width="400" class="pa-4">
      <v-card-title class="text-h6">ユーザー登録</v-card-title>

      <v-form @submit.prevent="submit" ref="formRef" v-model="isValid">
        <v-text-field
          v-model="form.email"
          label="メールアドレス"
          :rules="emailRules"
          required
        />
        <v-text-field
          v-model="form.username"
          label="ユーザー名"
          :rules="usernameRules"
          required
        />
        <v-text-field
          v-model="form.password"
          label="パスワード"
          type="password"
          :rules="passwordRules"
          required
        />

        <v-btn type="submit" color="primary" class="mt-4" :disabled="!isValid || loading">
          登録
        </v-btn>
      </v-form>

      <v-alert v-if="errorMessage" type="error" class="mt-4">
        {{ errorMessage }}
      </v-alert>
      <v-alert v-if="successMessage" type="success" class="mt-4">
        {{ successMessage }}
      </v-alert>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { registerUser } from '@/api/user'

const form = reactive({
  email: '',
  username: '',
  password: '',
})

const isValid = ref(false)
const formRef = ref()

const errorMessage = ref('')
const successMessage = ref('')
const loading = ref(false)

const emailRules = [(v: string) => !!v || 'メールアドレスを入力してください']
const usernameRules = [(v: string) => !!v || 'ユーザー名を入力してください']
const passwordRules = [(v: string) => v.length >= 6 || '6文字以上で入力してください']

const submit = async () => {
  errorMessage.value = ''
  successMessage.value = ''
  loading.value = true

  try {
    await registerUser(form)
    successMessage.value = 'ユーザー登録に成功しました'
    form.email = ''
    form.username = ''
    form.password = ''
    formRef.value.resetValidation()
  } catch (err: any) {
    errorMessage.value = err.message || '登録に失敗しました'
  } finally {
    loading.value = false
  }
}
</script>
