import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '../views/MainPageView.vue'
import SearchBankView from '@/views/SearchBankView.vue'
import BoardView from '@/views/Board/BoardView.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import JobView from '@/views/JobView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import UserProfileView from '@/views/UserProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    {
      path: '/searchbank', 
      name: 'searchbank', 
      component: SearchBankView
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView
    },
    {
      path: '/deposit', 
      name: 'deposit', 
      component: DepositView
    },
    {
      path: '/saving', 
      name: 'saving', 
      component: SavingView
    },
    {
      path: '/job', 
      name: 'job', 
      component: JobView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup', 
      name: 'signup', 
      component: SignUpView
    },
    {
      path: '/userprofile', 
      name: 'userprofile', 
      component: UserProfileView
    }
  ]
})

export default router
