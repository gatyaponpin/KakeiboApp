<script setup lang="ts">
  import SnackBar from './components/public/Snackbar.vue'
</script>

<template>
  <v-app>
    <router-view />
    <SnackBar />
  </v-app>
</template>
