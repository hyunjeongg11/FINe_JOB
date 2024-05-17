<template>
    <div>
        <h1>연령별 게시판</h1>
        <RouterLink :to="{name: 'ageboardcreate'}">게시글 생성</RouterLink> | 
        <RouterLink :to="{name: 'ageboarddetail'}">게시글 상세페이지</RouterLink>
        <AgeBoardList />
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AgeBoardList from '@/components/AgeBoardList.vue'
</script>

<style scoped>

</style>