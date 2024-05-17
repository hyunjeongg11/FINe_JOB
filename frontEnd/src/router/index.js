import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import SearchBankView from '@/views/SearchBankView.vue'
import FreeBoardView from '@/views/Board/FreeBoardView.vue'
import FreeBoardCreateView from '@/views/Board/FreeBoardCreateView.vue'
import FreeBoardDetailView from '@/views/Board/FreeBoardDetailView.vue'
import AgeBoardView from '@/views/Board/AgeBoardView.vue'
import AgeBoardCreateView from '@/views/Board/AgeBoardCreateView.vue'
import AgeBoardDetailView from '@/views/Board/AgeBoardDetailView.vue'
import FAQView from '@/views/Board/FAQView.vue'
import DepositView from '@/views/DepositView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingView from '@/views/SavingView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'
import JobView from '@/views/JobView.vue'
import JobDetailView from '@/views/JobDetailView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import UserProfileView from '@/views/accounts/UserProfileView.vue'
import ChangePasswordView from '@/views/accounts/ChangePasswordView.vue'

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
      path: '/freeboard',
      name: 'freeboard',
      component: FreeBoardView
    },
    {
      path: '/freeboardcreate',
      name: 'freeboardcreate',
      component: FreeBoardCreateView
    },
    {
      path: '/freeboarddetail',
      name: 'freeboarddetail',
      component: FreeBoardDetailView
    },
    {
      path: '/ageboard',
      name: 'ageboard',
      component: AgeBoardView
    },
    {
      path: '/ageboardcreate',
      name: 'ageboardcreate',
      component: AgeBoardCreateView
    },
    {
      path: '/ageboarddetail',
      name: 'ageboarddetail',
      component: AgeBoardDetailView
    },
    {
      path: '/faq',
      name: 'FAQ',
      component: FAQView
    },
    {
      path: '/deposit', 
      name: 'deposit', 
      component: DepositView
    },
    {
      path: '/depositdetail', 
      name: 'depositdetail', 
      component: DepositDetailView
    },
    {
      path: '/saving', 
      name: 'saving', 
      component: SavingView
    },
    {
      path: '/savingdetail', 
      name:'savingdetail', 
      component: SavingDetailView
    },
    {
      path: '/job', 
      name: 'job', 
      component: JobView
    },
    {
      path: '/jobdetail', 
      name: 'jobdetail', 
      component: JobDetailView
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
    ,
    {
      path: '/changepassword', 
      name: 'changepassword', 
      component: ChangePasswordView
    }
  ]
})

export default router
