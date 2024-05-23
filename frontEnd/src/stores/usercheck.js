import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import { useBoardStore } from '@/stores/board'
import axios from 'axios'

export const userCheckStore = defineStore('usercheck', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userId = ref(null)
  const recommendJobs = ref([])
  const store = useBoardStore() 
  const router = useRouter()
  const isSuperUser = ref(false)
  const profile_img_index = ref(null) // profile_img_index를 여기서 정의

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
      // console.log(userId.value)
      getProfileIndex()
    })
    // .then(() => {
    // })
    .catch(err => {
      console.log(err)
      window.alert('아이디 또는 비밀번호가 틀렸습니다.')
    })
  }

  const getProfileIndex = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/accounts/user_detail/${userId.value}`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(res.data.user_data)
        const userData = res.data.user_data
        profile_img_index.value = userData.profile_img_index
      })
      .catch((err) => {
        console.log(err)
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
        recommendJobs.value = []
        profile_img_index.value = null
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

  const changePassword = function (payload) {
    const { new_password1, new_password2, old_password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      data: {
        new_password1, new_password2, old_password
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        window.alert('비밀번호가 변경되었습니다.')
        router.go(-1)
      })
      .catch((err) => {
        console.log(err)
        window.alert("비밀번호는 8글자 이상이며, 영문과 숫자가 섞여야 합니다.")
      })
    }
    const withdraw = function () {
      const answer = window.confirm("회원탈퇴 하시겠습니까?")
      if (answer) {
        const re_answer = window.confirm("정말 회원탈퇴 하시겠습니까?")
        if (re_answer) {
          const re_re_answer = window.confirm("정말 정말 떠나시겠습니까? 모든 정보는 지워집니다.")
          if (re_re_answer) {
            axios({
              method: 'delete',
              url: `${API_URL}/api/v1/accounts/delete_user/`,
              headers: {
                Authorization: `Token ${token.value}`
            }
          })
          .then((res) => {
            token.value = null
            userId.value = null
            window.alert("회원탈퇴 되었습니다. 안녕히 가십시요.")
            router.push({ name: 'main'})
          })
          .catch((err) => {
            console.log(err)
          })
        }
      }
    }
  }
  const getRecommendJobs = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/jobs/recommend_job/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      console.log(res.data)
      recommendJobs.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }
  
return { API_URL, token, userId, recommendJobs, router, isSuperUser, isLogin, profile_img_index, logIn, logOut, signUp, changePassword, withdraw, getRecommendJobs, getProfileIndex }
}, {persist: true})
