<template>
	<div>
		<button @click="goBack" class="back-button">뒤로 가기</button>
		<h1>근처 은행 찾기</h1>
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
.back-button {
    margin: 10px 0;
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
