<template>
  <div>
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

</style>