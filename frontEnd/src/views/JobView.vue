<template>
  <div>
    <h1>일자리</h1>
    <JobList />
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import JobList from '@/components/JobList.vue'
</script>

<style scoped>

</style>