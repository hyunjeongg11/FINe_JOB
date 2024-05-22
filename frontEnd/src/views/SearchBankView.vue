<template>
	<div>
		
		<h1>주변 은행 찾기</h1>
		<Map />
	</div>
</template>

<script setup>
import Map from '@/components/Map.vue';
import SearchBar from '@/components/SearchBar.vue';
import PlaceList from '@/components/PlaceList.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

function goBack() {
    router.back();
}

</script>

<style scoped>
h1 {
    text-align: center;
    margin-bottom: 20px;
}

</style>
