<template>
    <div>
      <h2>오늘의 운세</h2>
      <div v-if="todayLuck">
        <p>{{ todayLuck }}</p>
      </div>
      <div v-else>
        <p >오늘의 운세를 확인하세요.</p>
        <button @click="getTodayLuck">운세 보기</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { useBoardStore } from '@/stores/board'
  const store = useBoardStore()
  const todayLuck = computed(() => store.todayLuck.content)
  
  const getTodayLuck = function() {
    store.getTodayLuck()
  }
  </script>
  
  <style scoped>
  
  </style>