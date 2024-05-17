<template>
    <div>
        <h1>적금 상품</h1>
        <RouterLink :to="{name: 'savingdetail'}">적금 상세 페이지</RouterLink>
        <SavingList />
    </div>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import SavingList from '@/components/SavingList.vue'
</script>

<style scoped>

</style>