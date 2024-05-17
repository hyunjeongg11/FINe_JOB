<template>
    <div>
        <nav>
            <RouterLink :to="{name: 'freeboard'}">자유게시판</RouterLink> | 
            <RouterLink :to="{name: 'ageboard'}">연령별 게시판</RouterLink> | 
            <RouterLink :to="{name: 'FAQ'}">FAQ</RouterLink>
        </nav>
        <h1>연령별 게시판</h1>
        <RouterLink :to="{name: 'ageboardcreate'}">게시글 생성</RouterLink> | 
        <RouterLink :to="{name: 'ageboarddetail'}">게시글 상세페이지</RouterLink>
        <AgeBoardList />
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AgeBoardList from '@/components/AgeBoardList.vue'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
    store.getAgeBoards()
})
</script>

<style scoped>

</style>