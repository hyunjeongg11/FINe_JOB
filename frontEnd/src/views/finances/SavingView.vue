<template>
	<div>
    <button @click="goBack" class="back-button">
      <img :src="`/assets/back.png`" alt="뒤로가기" style="width: 50px; height: 50px;">
    </button>
		<SavingList />
	</div>
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