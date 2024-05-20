<template>
    <div>
        <h1>적금 상품</h1>
        <!-- <RouterLink :to="{name: 'savingdetail'}">적금 상세 페이지</RouterLink> -->
        <SavingList />
    </div>
    <!-- <RouterView /> -->
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useFinanceStore } from '@/stores/finance';
import { onMounted } from 'vue'
import SavingList from '@/components/SavingList.vue'

const store = useFinanceStore()

onMounted(() => {
    store.getSavingList()
})
</script>

<style scoped>

</style>