import { defineStore } from 'pinia'

export const useUtilStore = defineStore('util', {
  state: () => ({
    snack: {
      msg: null as string | null,
      timeout: 3000,
      color: 'success'
    },
    email: 'user@example.com',
  }),
  actions: {
    setSnack(payload: { msg: string | null; timeout?: number; color?: string }) {
      this.snack.msg = payload.msg
      if (payload.timeout !== undefined) this.snack.timeout = payload.timeout
      if (payload.color !== undefined) this.snack.color = payload.color
    },
    resetSnack() {
      this.snack.msg = null
    },
     setEmail(email: string) {
      this.email = email
    },
  }
})