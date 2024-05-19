<template>
    <div>
      <h2>오늘의 운세</h2>
      <div v-if="userStore.token">
        <div v-if="todayLuck">
          <p>{{ todayLuck }}</p>
        </div>
        <div v-else>
          <p >오늘의 운세를 확인하세요.</p>
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
  const todayLuck = computed(() => store.todayLuck.content)
  
  const getTodayLuck = function() {
    store.getTodayLuck()
  }
  </script>
  
  <style scoped>
  
  </style>