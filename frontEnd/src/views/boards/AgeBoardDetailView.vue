<template>
	<div class="container">
		<nav>
			<RouterLink :to="{ name: 'freeboard' }">자유게시판</RouterLink> | 
			<RouterLink :to="{ name: 'ageboard' }">연령별게시판</RouterLink> | 
			<RouterLink :to="{ name: 'FAQ' }">FAQ</RouterLink>
		</nav>
		<div v-if="ageBoard">
			<h3>연령별게시판</h3>
			<div class="post-header">
				<h1>{{ ageBoard.title }}</h1>
				<div class="post-meta">
					<p>작성자: {{ ageBoard.author }}</p>
					<p>작성시간: {{ formattedCreatedAt }}</p>
					<p>수정시간: {{ formattedUpdatedAt }}</p>
				</div>
			</div>
			<div class="post-content">
				<div class="content-box">
					<p>{{ ageBoard.content }}</p>
				</div>
			</div>
			<div v-if="ageBoard.image" class="attachment">
				<p>첨부파일: <a :href="ageBoard.image" download>{{ fileName }}</a></p>
			</div>
			<button @click="goToEditPage">수정</button>
		</div>
		<Comment />
		<CreateComment />
	</div>
</template>

<script setup>
import { RouterLink, useRoute, useRouter } from 'vue-router'
import CreateComment from '@/components/CreateComment.vue'
import Comment from '@/components/Comment.vue'
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()
const route = useRoute()
const router = useRouter()
const ageBoard = ref(null)

onMounted(() => {
	axios({
		method: 'get',
		url: `${store.API_URL}/api/v1/boards/age/${route.params.id}`,
		headers: {
			Authorization: `Token ${store.token}` // 인증 토큰을 헤더에 추가
		}
	})
		.then((res) => {
			console.log(res.data)
			ageBoard.value = res.data
		})
		.catch((err) => {
			console.log(err)
		})
})

const formatDateTime = (datetime) => {
	const date = new Date(datetime)
	const year = date.getFullYear()
	const month = String(date.getMonth() + 1).padStart(2, '0')
	const day = String(date.getDate()).padStart(2, '0')
	const hours = date.getHours()
	const minutes = String(date.getMinutes()).padStart(2, '0')
	const isPM = hours >= 12
	const formattedHours = isPM ? hours - 12 : hours
	const period = isPM ? '오후' : '오전'
	return `${year}.${month}.${day} ${period} ${formattedHours}`
}

const formattedCreatedAt = computed(() => {
	return ageBoard.value ? formatDateTime(ageBoard.value.created_at) : ''
})

const formattedUpdatedAt = computed(() => {
	return ageBoard.value ? formatDateTime(ageBoard.value.updated_at) : ''
})

const goToEditPage = () => {
	router.push(`/ageboarddetail/${route.params.id}/update`)
}

const fileName = computed(() => {
	if (ageBoard.value && ageBoard.value.image) {
		const parts = ageBoard.value.image.split('/')
		return parts[parts.length - 1]
	}
	return ''
})
</script>

<style scoped>
.container {
	max-width: 1500px;
	margin: 0 auto;
	padding: 20px;
	border: 1px solid #ddd;
	border-radius: 8px;
	background-color: #f9f9f9;
}

nav {
	margin-bottom: 20px;
}

.post-header {
	margin-bottom: 20px;
}

.post-header h1 {
	margin-bottom: 10px;
}

.post-meta {
	display: flex;
	justify-content: space-between;
	margin-bottom: 20px;
}

.post-content {
	margin-bottom: 20px;
}

.content-box {
	padding: 10px;
	border: 1px solid #ccc;
	border-radius: 4px;
	background-color: #fff;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.attachment {
	margin-top: 20px;
}

button {
	padding: 5px 10px;
	border: none;
	border-radius: 4px;
	background-color: #007bff;
	color: white;
	cursor: pointer;
}

button:hover {
	background-color: #0056b3;
}
</style>
