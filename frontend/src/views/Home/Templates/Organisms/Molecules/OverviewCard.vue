<script setup>
  import { defineProps } from 'vue';

  // eslint-disable-next-line no-unused-vars
  const props = defineProps({
    name: String,
    money: Number
  })

  const moneyLabel = "￥" + props.money.toLocaleString("ja-JP");

</script>

<template>
  <v-container class="d-flex flex-column justify-center text-medium-emphasis px-15">
    <p>{{ name }}</p>
    <div class="text-h4 font-weight-black mb-4">{{ moneyLabel }}</div>
  </v-container>
</template>