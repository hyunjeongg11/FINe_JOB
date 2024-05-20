<template>
  <div>
    <button @click="goBack" class="back-button">뒤로 가기</button>
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
    margin: 10px 10px;
    padding: 5px 10px;
    font-size: 16px;
    color: black;
    /* background-color: #555; */
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.back-button:hover {
    background-color: rgb(165, 165, 165);
}
</style>