<script setup>
  import { ref } from 'vue'
  import { useUtilStore } from '@/store/util'

  const drawer = ref(false)
  const store = useUtilStore()

  const email = store.email

</script>

<template>
  <v-app-bar color="primary" :height="50">
    <template v-slot:prepend>
      <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
    </template>
    <v-spacer></v-spacer>
    <v-app-bar-title class="mx-auto">Accounting Manager</v-app-bar-title>
    <template v-slot:append>
      <p class="text-subtitle-1 mx-5">{{ email }}</p>
    </template>
  </v-app-bar>
</template>

