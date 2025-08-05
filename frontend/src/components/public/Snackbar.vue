<template>
  <v-snackbar
    v-model="isVisible"
    :timeout="util.snack.timeout"
    color="grey-lighten-2"
  >
    {{ util.snack.msg }}

    <template v-slot:actions>
      <v-btn
        :color="util.snack.color"
        variant="text"
        @click="util.resetSnack()"
      >
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useUtilStore } from '@/store/util'

const util = useUtilStore()

// snack.msg が存在するかで表示判定
const isVisible = computed({
  get: () => !!util.snack.msg,
  set: (val: boolean) => {
    if (!val) util.resetSnack()
  }
})
</script>