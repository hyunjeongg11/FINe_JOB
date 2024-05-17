import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const freeBoards = ref([])
  const ageBoards = ref([])

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
  return { freeBoards, ageBoards, API_URL, getFreeBoards, getAgeBoards }
}, {persist: true})
