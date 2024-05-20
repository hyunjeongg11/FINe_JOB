<template>
  <div>
    <h4 class="luck">오늘의 운세</h4>
    <div v-if="userStore.token">
      <div v-if="todayLuckTitle">
        <p class="luck-title">{{ todayLuckTitle }}</p>
        <p class="luck-content">{{ todayLuckContent }}</p>
      </div>
      <div v-else>
        <p>오늘의 운세를 확인하세요.</p>
        <button @click="getTodayLuck">운세 보기</button>
      </div>
    </div>
    <div v-else>
      <p>오늘의 운세를 보려면 로그인하세요.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useBoardStore } from '@/stores/board'
import { userCheckStore } from '@/stores/usercheck'
const store = useBoardStore()
const userStore = userCheckStore()
const todayLuckTitle = computed(() => store.todayLuck.title)
const todayLuckContent = computed(() => store.todayLuck.content)

const getTodayLuck = function() {
  store.getTodayLuck()
}
</script>

<style scoped>
.luck {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
}

.luck-title {
  font-size: 1.2rem;
  font-weight: bold;
  text-align: center;
}

.luck-content {
  font-size: 1rem;
  padding: 3%;
}

</style>