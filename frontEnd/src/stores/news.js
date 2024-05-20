import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useApiStore = defineStore('news', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const recommenditem=ref('')

  const news = ref([])
  const getNews = function () {
      axios({
          method: 'GET',
          url: `${API_URL}/api/v1/naver_news/`
      })
          .then(res => {
              console.log(res.data)
              news.value = res.data.items
          })
          .catch(err => console.log(err))
  }

  // const recommend = function (user_id) {
  //     recommenditem.value=''
  //     console.log('id:',user_id)
  //     axios({
  //         method: 'GET',
  //         url: `${URL}/api/v1/recommend/${user_id}`,
  //     })
  //         .then(res => {
  //             console.log(res.data.data)
  //             recommenditem.value=res.data.data
  //             console.log(recommenditem.value)
  //         })
  //         .catch(err => console.log(err))
  // }
  return { API_URL, news, getNews }
}, { persist: true })