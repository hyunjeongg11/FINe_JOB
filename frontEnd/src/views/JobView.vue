<template>
    <div>
        <h1>일자리</h1>
        <RouterLink :to="{name: 'jobdetail'}">일자리 상세 페이지</RouterLink>
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