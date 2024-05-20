import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import SearchBankView from '@/views/SearchBankView.vue'
import FreeBoardView from '@/views/boards/FreeBoardView.vue'
import FreeBoardCreateView from '@/views/boards/FreeBoardCreateView.vue'
import FreeBoardDetailView from '@/views/boards/FreeBoardDetailView.vue'
import FreeEditBoardView from '@/views/boards/FreeEditBoardView.vue'
import AgeBoardView from '@/views/boards/AgeBoardView.vue'
import AgeBoardCreateView from '@/views/boards/AgeBoardCreateView.vue'
import AgeBoardDetailView from '@/views/boards/AgeBoardDetailView.vue'
import AgeEditBoardView from '@/views/boards/AgeEditBoardView.vue'
import FAQView from '@/views/boards/FAQView.vue'
import DepositView from '@/views/finances/DepositView.vue'
import DepositDetailView from '@/views/finances/DepositDetailView.vue'
import SavingView from '@/views/finances/SavingView.vue'
import SavingDetailView from '@/views/finances/SavingDetailView.vue'
import JobView from '@/views/JobView.vue'
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
      path: '/freeboarddetail/:id',
      name: 'freeboarddetail',
      component: FreeBoardDetailView
    },
    {
      path: '/freeboarddetail/:id/update',
      name: 'freeditboard',
      component: FreeEditBoardView
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
      path: '/ageboarddetail/:id',
      name: 'ageboarddetail',
      component: AgeBoardDetailView
    },
    {
      path: '/ageboarddetail/:id/update',
      name: 'ageeditboard',
      component: AgeEditBoardView
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
      path: '/deposit/:fin_prdt_cd/:id/', 
      name: 'depositdetail', 
      component: DepositDetailView
    },
    {
      path: '/saving', 
      name: 'saving', 
      component: SavingView
    },
    {
      path: '/saving/:fin_prdt_cd/:id/', 
      name:'savingdetail', 
      component: SavingDetailView
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
    ,
    {
      path: '/changepassword', 
      name: 'changepassword', 
      component: ChangePasswordView
    }
  ]
})

export default router