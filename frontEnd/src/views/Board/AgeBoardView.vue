<template>
	<div>
		<nav>
			<RouterLink :to="{name: 'freeboard'}">자유게시판</RouterLink> | 
			<RouterLink :to="{name: 'ageboard'}">연령별 게시판</RouterLink> | 
			<RouterLink :to="{name: 'FAQ'}">FAQ</RouterLink>
		</nav>
		<div class="container">
			<h1>연령별 게시판</h1>
			<AgeBoardList />
		</div>
	</div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AgeBoardList from '@/components/AgeBoardList.vue'
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()

onMounted(() => {
	store.getAgeBoards()
})
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

</style>