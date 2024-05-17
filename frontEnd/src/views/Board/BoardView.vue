<template>
    <div>
        <RouterLink :to="{name: 'freeboard'}">자유게시판</RouterLink> | 
        <RouterLink :to="{name: 'ageboard'}">연령별 게시판</RouterLink> | 
        <RouterLink :to="{name: 'FAQ'}">FAQ</RouterLink>
    </div>
    <FreeBoardList />
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import FreeBoardList from '@/components/FreeBoardList.vue'
</script>

<style scoped>

</style>