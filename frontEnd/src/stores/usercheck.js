import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const userCheckStore = defineStore('usercheck', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userId = ref(null)
  const router = useRouter()
  const isSuperUser = ref(false)

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
        // console.log(res)
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
      .then((res) => {
        console.log('로그아웃 완료')
        token.value = null
        userId.value = null
        router.push({ name: 'home'})
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return { API_URL, token, userId, router, isSuperUser, logIn, logOut }
}, {persist: true})