<script setup>
  import BalanceOverview from './Organisms/BalanceOverview.vue';
  import BalanceCategory from './Organisms/BalanceCategory.vue';

</script>

<template>
  <v-container class="d-flex flex-column justify-center align-center border">
    <BalanceOverview />
    <BalanceCategory />
    <v-btn color="primary" width="100">入力へ</v-btn>
  </v-container>
</template>