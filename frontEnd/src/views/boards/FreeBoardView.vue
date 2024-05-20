<template>
	<div>
		<button @click="goBack" class="back-button">뒤로 가기</button>
		<nav>
			<RouterLink :to="{name: 'freeboard'}">자유게시판</RouterLink> | 
			<RouterLink :to="{name: 'ageboard'}">연령별 게시판</RouterLink> | 
			<RouterLink :to="{name: 'FAQ'}">FAQ</RouterLink>
		</nav>
		<div class="container">
			<h1>자유게시판</h1>
			<FreeBoardList />
		</div>
	</div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import FreeBoardList from '@/components/FreeBoardList.vue'
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()
const router = useRouter();

onMounted(() => {
	store.getFreeBoards()
})

function goBack() {
    router.back();
}
</script>

<style scoped>
h1 {
	text-align: center;
	margin-bottom: 20px;
}
.container {
	max-width: 1500px;
	margin: 0 auto;
	padding: 20px;
	border: 1px solid #ddd;
	border-radius: 8px;
	background-color: #f9f9f9;
}

nav {
	text-align: center;
	margin-bottom: 20px;
}

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