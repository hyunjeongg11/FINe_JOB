<template>
    <div>
        <h1>예금 상품</h1>
        <!-- <RouterLink :to="{name: 'depositdetail'}">예금 상품 상세 페이지</RouterLink> -->
        <DepositList />
    </div>
    <!-- <RouterView /> -->
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useFinanceStore } from '@/stores/finance';
import DepositList from '@/components/DepositList.vue'
import { onMounted } from 'vue';

const store = useFinanceStore()

onMounted(() => {
    store.getDepositList()
})

</script>

<style scoped>

</style>