<template>
	<div>
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

</style>