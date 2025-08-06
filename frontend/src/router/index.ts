import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import MainView from '@/views/MainView.vue'
import Login from '@/views/Login.vue'
import Home from '@/views/Home/HomePage.vue'
import List from '@/views/List/ListPage.vue'
import UserRegister from '@/views/UserRegister.vue'
// import Saving from '@/pages/SavingPage.vue'
// import Graph from '@/pages/GraphPage.vue'
// import Calendar from '@/pages/CalendarPage.vue'
// import Setting from '@/pages/SettingPage.vue'
// import Investment from '@/pages/InvestmentPage.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
   {
    path: '/register',
    name: 'Register',
    component: UserRegister,
  },
  {
    path: '/',
    component: MainView,
    children: [
      { path: '', redirect: '/home' }, // ルートアクセス時に /home にリダイレクト
      { path: 'home', name: 'Home', component: Home },
      { path: 'list', name: 'List', component: List },
      // { path: 'saving', name: 'Saving', component: Saving },
      // { path: 'graph', name: 'Graph', component: Graph },
      // { path: 'calendar', name: 'Calendar', component: Calendar },
      // { path: 'setting', name: 'Setting', component: Setting },
      // { path: 'investment', name: 'Investment', component: Investment },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem('access_token')

  // ログインページと新規登録ページは常に許可
  if (to.name === 'Login' || to.name === 'Register') {
    return next()
  }

  // トークンがない場合はログインページへリダイレクト
  if (!isLoggedIn) {
    return next({ name: 'Login' })
  }

  next()
})

export default router