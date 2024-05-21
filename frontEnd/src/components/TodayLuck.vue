<template>
  <div class="outer-box">
    <h4 class="luck-header">오늘의 운세</h4>
    <div class="luck-border">
      <div class="luck-container" v-if="userStore.token">
        <div v-if="todayLuckTitle">
          <p class="luck-title">오늘의 총운은 <span class="highlight">{{ todayLuckTitle }}</span>입니다.</p>
          <hr>
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
  height: 90%;
}

.luck-info {
  font-size: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%; /* 높이를 100%로 설정합니다. */
}

.luck-border {
  border: 1px solid rgb(224, 224, 224);
  border-radius: 10px;
  padding: 0px 10px;
  background-color: white;
}

.luck-header {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  padding-top: 5px;
  border-radius: 10px;
}

.luck-title {
  font-size: 1.2rem;
  margin-top: 5px;
  font-weight: bold;
  text-align: center;
}

.luck-content {
  font-size: 1rem;
  padding: 5px 0px;
  background-color: white;
  border-radius: 10px;
}

.btn-luck {
  width: 100px;
  margin: 10px auto;
  background-color: rgb(180, 212, 255);
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}

.highlight {
  color: rgb(134, 182, 246);
  font-size: 1.4rem;
}
</style>
