import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import IntroView from '@/views/IntroView.vue'
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
import RecommendJobListView from '@/views/RecommendJobListView.vue'
import CurrencyConverterView from '@/views/CurrencyConverterView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import UserProfileView from '@/views/accounts/UserProfileView.vue'
import ChangePasswordView from '@/views/accounts/ChangePasswordView.vue'
import UserProfileEditView from '@/views/accounts/UserProfileEditView.vue'
import SubscribeProductView from '@/views/accounts/SubscribeProductView.vue'
import BoardRecordView from '@/views/accounts/BoardRecordView.vue'
import UserProfileDetailView from '@/views/accounts/UserProfileDetailView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'intro',
      component: IntroView
    },
    {
      path: '/main',
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
      path: '/recommendjoblist',
      name: 'recommendjoblist',
      component: RecommendJobListView
    },
    {
      path: '/currencyconverter',
      name: 'currencyconverter',
      component: CurrencyConverterView
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
    },
    {
      path: '/userprofileedit',
      name: 'userprofileedit',
      component: UserProfileEditView
    },
    {
      path: '/subscribeproduct',
      name: 'subscribeproduct',
      component: SubscribeProductView
    },
    {
      path: '/boardrecord',
      name: 'boardrecord',
      component: BoardRecordView
    },
    {
      path: '/userprofiledetail',
      name: 'userprofiledetail',
      component: UserProfileDetailView
    },
  ]
})

import { userCheckStore } from '@/stores/usercheck'

router.beforeEach((to, from) => {
  const store = userCheckStore()
  if ((to.name === 'login' || to.name === 'signup') && (store.isLogin)){
    window.alert('이미 로그인 하셨습니다.')
    return { name: 'main' }
  }
})

export default router