<script setup>
  import { defineProps, computed } from 'vue';

  // eslint-disable-next-line no-unused-vars
  const props = defineProps({
    category: String,
    budget: Number,
    used: Number
  });

  const category = computed(() => props.category ?? '')

  const remainLabel = computed(() =>
    '￥' + ((props.budget ?? 0) - (props.used ?? 0)).toLocaleString('ja-JP')
  )

  const usedLabel = computed(() =>
    '￥' + (props.used ?? 0).toLocaleString('ja-JP')
  )

  const progress = computed(() =>
    props.budget ? (props.used ?? 0) / props.budget * 100 : 0
  )

  const isOver = computed(() =>
    (props.budget ?? 0) - (props.used ?? 0) < 0
  )

</script>

<template>
  <v-card class="mx-auto border" max-width="320" flat>
    <v-card-text class="text-medium-emphasis pa-6">

      <div class="d-flex">
        <div class="text-h6 mb-6">{{ category }}</div>
        <v-spacer></v-spacer>
        <v-chip
          v-if="isOver"
          class="ma-2"
          color="error"
          variant="outlined"
        >
          超過
        </v-chip>
      </div>

      <div class="text-h4 font-weight-black mb-4">
        {{ usedLabel }}
      </div>

      <v-progress-linear
        bg-color="surface-variant"
        class="mb-6"
        color="primary"
        height="10"
        :model-value="progress"
        rounded="pill"
      ></v-progress-linear>

      <div>残：{{ remainLabel }}</div>
    </v-card-text>
  </v-card>
</template>