<template>
	<div>
		    <button @click="goBack" class="back-button">
      <img :src="`/assets/back.png`" alt="뒤로가기" style="width: 50px; height: 50px;">
    </button>
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
