<template>
	<div>
    <button @click="goBack" class="back-button">
      <img :src="`/assets/back.png`" alt="뒤로가기" style="width: 50px; height: 50px;">
    </button>
		<DepositList />
	</div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance';
import DepositList from '@/components/DepositList.vue'
import { onMounted } from 'vue';

const router = useRouter();
const store = useFinanceStore()

function goBack() {
    router.back();
}

onMounted(() => {
    store.getDepositList()
})

</script>

<style scoped>
.back-button {
    margin: 0px 10px;
    /* padding: 5px 10px; */
    font-size: 16px;
    color: black;
    background-color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.back-button:hover {
    background-color: rgb(165, 165, 165);
}
</style>