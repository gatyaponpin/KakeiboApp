<script setup lang="ts">
import Header from '@/components/public/Header.vue'
import SideBar from '@/components/public/Sidebar.vue'
</script>

<template>
  <v-main>
    <Header />
    <SideBar />
    <v-container width="1500" height="820" class="mx-auto mt-5 border">
      <router-view />
    </v-container>
  </v-main>
</template>