import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck.js'

export const useBoardStore = defineStore('board', () => {
  const freeBoards = ref([])
  const ageBoards = ref([])
  const ageComments = ref([])
  const store = userCheckStore()
  const token = ref('f9ed05e26bf2a18c2c8a3793ad057fc9e5027499')
  // const token = store.token

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


  return { freeBoards, ageBoards, ageComments, API_URL, token, getFreeBoards, getAgeBoards }
}, { persist: true })
