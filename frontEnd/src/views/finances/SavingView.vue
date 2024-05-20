<template>
	<div>
    <button @click="goBack" class="back-button">뒤로 가기</button>
		<!-- <h1>적금 상품</h1> -->
		<!-- <RouterLink :to="{name: 'savingdetail'}">적금 상세 페이지</RouterLink> -->
		<SavingList />
	</div>
	<!-- <RouterView /> -->
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance';
import { onMounted } from 'vue'
import SavingList from '@/components/SavingList.vue'

const store = useFinanceStore()
const router = useRouter();

function goBack() {
    router.back();
}
onMounted(() => {
    store.getSavingList()
})
</script>

<style scoped>
.back-button {
    margin: 10px 10px;
    padding: 5px 10px;
    font-size: 16px;
    color: black;
    /* background-color: #555; */
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.back-button:hover {
    background-color: rgb(165, 165, 165);
}
</style>