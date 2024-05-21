<template>
  <div>
    <button @click="goBack" class="back-button">
      <img :src="`/assets/back.png`" alt="뒤로가기" style="width: 50px; height: 50px;">
    </button>
    <h1>일자리</h1>
    <JobList />
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import JobList from '@/components/JobList.vue'
const router = useRouter();

function goBack() {
    router.back();
}
</script>

<style scoped>
.back-button {
  margin: 0px 10px;
  /* padding: 5px 10px; */
  font-size: 16px;
  color: black;
  background-color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.back-button:hover {
    background-color: rgb(165, 165, 165);
}
</style>