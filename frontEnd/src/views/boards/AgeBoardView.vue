<template>
	<div>
		<button @click="goBack" class="back-button">
      <img :src="`/assets/back.png`" alt="뒤로가기" style="width: 50px; height: 50px;">
    </button>
		<ul class="nav nav-underline justify-content-center">
			<li class="nav-item">
				<RouterLink :to="{name: 'freeboard'}" class="nav-link" :class="{ active: isActiveRoute('freeboard') }">자유게시판</RouterLink>
			</li>
			<li class="nav-item"> 
				<RouterLink :to="{name: 'ageboard'}" class="nav-link" :class="{ active: isActiveRoute('ageboard') }">연령별게시판</RouterLink>
			</li>
			<li class="nav-item">
				<RouterLink :to="{name: 'FAQ'}" class="nav-link" :class="{ active: isActiveRoute('FAQ') }">FAQ</RouterLink>
			</li>
		</ul>
		<div class="container">
			<!-- <h1>연령별 게시판</h1> -->
			<AgeBoardList />
		</div>
	</div>
</template>

<script setup>
import { RouterLink, useRouter, useRoute } from 'vue-router'
import AgeBoardList from '@/components/AgeBoardList.vue'
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()
const router = useRouter()
const route = useRoute()

onMounted(() => {
	store.getAgeBoards()
})

function goBack() {
    router.back()
}

function isActiveRoute(name) {
  return route.name === name
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
	/* border: 1px solid #ddd; */
	/* border-radius: 8px; */
	/* background-color: #f9f9f9; */
}

nav {
	text-align: center;
	margin-bottom: 20px;
}

.nav-link {
	color: black;
	font-size: 20px;
}

.nav-link.active {
	color: black;
	border-bottom: 2px solid black;
}

.nav-link:hover,
.nav-link.active {
    color: rgb(59, 130, 153);
}

.back-button {
    margin: 0px 10px;
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
