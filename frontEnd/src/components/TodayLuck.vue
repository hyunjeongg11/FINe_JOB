<template>
  <div class="outer-box">
    <h4 class="luck-header">오늘의 운세</h4>
    <div class="luck-border">
      <div class="luck-container" v-if="userStore.token">
        <div v-if="loading">
          <!-- 로딩 스피너 표시 -->
          <div class="spinner-grow" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
        </div>
        <div v-else-if="todayLuckTitle">
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
        <p class="luck-info">오늘의 운세를 보시려면 로그인하세요.</p>
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
const loading = ref(false)

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
  loading.value = true; // 버튼 클릭 시 로딩 상태를 true로 변경
  setTimeout(() => {
    store.getTodayLuck()
    loading.value = false; // 운세를 가져온 후 로딩 상태를 false로 변경
  }, 500)
}
</script>

<style scoped>
.outer-box {
  background-color: rgb(236, 245, 248);
  padding-bottom: 3%;
  border-radius: 10px;
}

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
  margin-left: 5%;
  width: 90%;
}

.luck-header {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  padding-top: 5px;
  border-radius: 10px;
  width: 90%;
}

.luck-title {
  font-size: 1.2rem;
  margin-top: 5px;
  font-weight: bold;
  text-align: center;
}

.luck-content {
  font-size: 14px;
  padding-top: 3px;
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

.btn-luck:hover {
  background-color: rgb(104, 142, 206);
}

.highlight {
  color: rgb(134, 182, 246);
  font-size: 1.4rem;
}

.spinner-grow {
  width: 2rem;
  height: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
}
</style>
