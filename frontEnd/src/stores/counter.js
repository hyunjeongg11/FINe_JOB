import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  // const freeArticles = ref([])
  // const FREE_BOARD_API_URL = 'http://127.0.0.1:8000'
  // const getFreeBoards = function() {
  //   axios({
  //     method: 'get',
  //     url: `${API_URL}/api/v1/boards/free/`,
  //   })
  //     .then(res => {
  //       console.log(res)
  //       console.log(res.data)
  //     })
  //     .catch(err => console.log(err))
  // }
  // return { freeArticles, FREE_BOARD_API_URL, getFreeBoards }
}, {persist: true})
