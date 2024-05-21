<template>
  <div class="news-outer">
    <h4 class="news-header">오늘의 금융 뉴스</h4>
    <div v-for="news in newsList" :key="news.id" class="news-item">
      <a :href="news.link" target="_blank" class="news-link">
        <p v-html="news.title" class="news-title"></p>
      </a>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, computed } from 'vue'
import { useApiStore } from '@/stores/news'

const apistore = useApiStore()
const intervalId = setInterval(() => {
  apistore.getNews()
}, 10000)

onMounted(() => {
  // Initial news load
  apistore.getNews()
})

onUnmounted(() => {
  // Stop the interval when the page is left
  if (intervalId) {
    clearInterval(intervalId)
  }
})

const newsList = computed(() => apistore.news)
</script>

<style scoped>
.news-outer {
  height: 100%;
  padding: 20px;
  box-sizing: border-box;
  overflow: hidden;
  background-color: rgb(219, 236, 241);

  border-radius: 10px;
}

.news-header {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  padding: 5px 0;
  border-radius: 10px;
}

.news-item {
  padding: 5px 0px;
  margin: 5px 0;
  background-color: white;
  border: 1px solid rgb(224, 224, 224);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  /* transition: box-shadow 0.3s; */
  text-align: center;
}

.news-item:hover {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}

.news-link {
  color: black;
  text-decoration: none;
}

.news-link:hover {
  color: rgb(134, 182, 246);
}

.news-title {
  font-size: 1.2rem;
}
</style>
