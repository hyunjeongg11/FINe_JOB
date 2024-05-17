<template>
    <div>
        <h1>예금 상품</h1>
        <RouterLink :to="{name: 'depositdetail'}">예금 상품 상세 페이지</RouterLink>
        <DepositList />
    </div>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import DepositList from '@/components/DepositList.vue'
</script>

<style scoped>

</style>