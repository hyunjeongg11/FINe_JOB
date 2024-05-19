import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck.js'

export const useBoardStore = defineStore('board', () => {
  const freeBoards = ref([])
  const ageBoards = ref([])
  const store = userCheckStore()
  const todayLuck = ref('')
  // const token = ref('f9ed05e26bf2a18c2c8a3793ad057fc9e5027499')
  const token = store.token
  const API_URL = 'http://127.0.0.1:8000'
  
  const getFreeBoards = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/boards/free/`,
    })
      .then(res => {
        freeBoards.value = res.data
      })
      .catch(err => console.log(err))
  }

  const getAgeBoards = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/boards/age/`,
    })
      .then(res => {
        ageBoards.value = res.data
      })
      .catch(err => console.log(err))
  }

  const getTodayLuck = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/side_events/get_today_luck/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(res => {
        todayLuck.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  } 

  return { freeBoards, ageBoards, API_URL, token, todayLuck, getFreeBoards, getAgeBoards, getTodayLuck }
}, {persist: true})
