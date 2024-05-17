<template>
    <div>
        <h2>자유게시판 목록</h2>
        <FreeBoardListItem
            v-for="freeBoard in store.freeBoards"
            :key="freeBoard.id"
            :freeBoard="freeBoard"
        />
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import FreeBoardListItem from '@/components/FreeBoardListItem.vue'

const store = useCounterStore()
</script>

<style scoped>

</style>