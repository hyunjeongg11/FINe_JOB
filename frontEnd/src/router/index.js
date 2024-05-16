import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchBankView from '@/views/SearchBankView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/searchbank', 
      name: 'searchbank', 
      component: SearchBankView
    }
  ]
})

export default router
