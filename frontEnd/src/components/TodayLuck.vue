<template>
  <div class="outer-box">
    <h4 class="luck-header">오늘의 운세</h4>
    <div class="luck-container" v-if="userStore.token">
      <div v-if="todayLuckTitle">
        <p class="luck-title">오늘의 총운은 <span class="highlight">{{ todayLuckTitle }}</span>입니다.</p>
        <p class="luck-content">{{ todayLuckContent }}</p>
      </div>
      <div v-else class="luck-info">
        <p>오늘의 운세를 확인하세요.</p>
        <button class="btn-luck" @click="getTodayLuck">운세 보기</button>
      </div>
    </div>
    <div class="luck-container" v-else>
      <p class="luck-info">오늘의 운세를 보려면 로그인하세요.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useBoardStore } from '@/stores/board'
import { userCheckStore } from '@/stores/usercheck'
const store = useBoardStore()
const userStore = userCheckStore()
const todayLuckTitle = computed(() => {
  if (store.todayLuck && store.todayLuck.title) {
    const fullTitle = store.todayLuck.title
    const startIndex = fullTitle.indexOf('오늘의 총운은') + 8 // Length of "오늘의 총운은"
    const endIndex = fullTitle.indexOf('입니다')
    return fullTitle.substring(startIndex, endIndex).trim()
  }
  else {
    return ''
  }
})
const todayLuckContent = computed(() => store.todayLuck.content)

const getTodayLuck = function() {
  store.getTodayLuck()
}
</script>

<style scoped>
.luck-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%; /* 높이를 100%로 설정합니다. */
}

.luck-info {
  font-size: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%; /* 높이를 100%로 설정합니다. */
}

.luck-header {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  /* background-color: rgb(224, 224, 224); */
  padding: 15px 0;
  border-radius: 10px;
}

.luck-title {
  font-size: 1.2rem;
  font-weight: bold;
  text-align: center;
}

.luck-content {
  font-size: 1rem;
  padding: 2%;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.btn-luck {
  width: 100px;
  margin: 10px auto;
  background-color: rgb(180, 212, 255);
  color: white; /* Optional: Makes the button text white for better contrast */
  border: none; /* Optional: Removes the border */
  padding: 10px;
  border-radius: 5px; /* Optional: Adds rounded corners */
  cursor: pointer; /* Optional: Changes the cursor to a pointer when hovering */
}

.highlight {
  color: blue;
  font-size: 1.4rem;
}
</style>
