import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import { useBoardStore } from '@/stores/board'
import axios from 'axios'

export const userCheckStore = defineStore('usercheck', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userId = ref(null)
  const store = useBoardStore() 
  const router = useRouter()
  const isSuperUser = ref(false)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        console.log('로그인 완료')
        token.value = res.data.key
        userId.value = username
        // checkSuperUser()
        router.push({name: 'main'})
      })
      .catch(err => {
        console.log(err)
        window.alert('아이디 또는 비밀번호가 틀렸습니다.')
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`
    })
      .then(res => {
        console.log('로그아웃 완료')
        token.value = null
        userId.value = null
        store.todayLuck = ''
        router.push({ name: 'main'})
      })
      .catch(err => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2, email, nickname, birthday, gender, address, asset, salary, interest_industry } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email, nickname, birthday, gender, address, asset, salary, interest_industry
      }
    })
      .then(res => {
        console.log('회원가입 완료')
        const password = password1
        logIn({ username, password })
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { API_URL, token, userId, router, isSuperUser, isLogin, logIn, logOut, signUp }
}, {persist: true})