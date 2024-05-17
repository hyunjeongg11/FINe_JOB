<template>
    <div>
        <h1>자유게시판</h1>
        <RouterLink :to="{name: 'freeboardcreate'}">게시글 생성</RouterLink> | 
        <RouterLink :to="{name: 'freeboarddetail'}">게시글 상세페이지</RouterLink>
        <FreeBoardList />
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import FreeBoardList from '@/components/FreeBoardList.vue'
</script>

<style scoped>

</style>