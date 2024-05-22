<template>
	<div>

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

</style>