<template>
    <div>
        <h2>연령별게시판 목록</h2>
        <AgeBoardListItem
            v-for="ageBoard in store.ageBoards"
            :key="ageBoard.id"
            :ageBoard="ageBoard"
        />
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import AgeBoardListItem from '@/components/AgeBoardListItem.vue'

const store = useCounterStore()
</script>

<style scoped>

</style>