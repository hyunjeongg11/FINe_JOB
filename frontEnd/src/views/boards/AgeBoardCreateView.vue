<template>
	<div class="container">
		<nav>
      <RouterLink :to="{ name: 'freeboard' }" class="nav-item">자유게시판</RouterLink> | 
      <RouterLink :to="{ name: 'ageboard' }" class="nav-item-here">연령별게시판</RouterLink> | 
      <RouterLink :to="{ name: 'FAQ' }" class="nav-item">FAQ</RouterLink>
    </nav>
		<h1>연령별 게시글 작성</h1>
		<form @submit.prevent="createBoard" class="form-container">
			<div class="form-group">
				<label for="title">제목 :</label>
				<input type="text" id="title" v-model.trim="title" placeholder="제목을 입력해주세요" />
			</div>
			<div class="form-group">
				<label for="content">내용 :</label>
				<textarea id="content" v-model.trim="content" placeholder="내용을 입력해주세요"></textarea>
			</div>
			<div class="form-group">
				<label for="image">파일 첨부 :</label>
				<input type="file" id="image" @change="handleFileUpload" />
				<div v-if="fileName">{{ fileName }}</div>
				<button type="button" @click="clearFile">전체 삭제</button>
			</div>
			<div class="form-actions">
				<button type="button" @click="cancel">취소</button>
				<input class="btn-submit" type="submit" value="등록" />
			</div>
		</form>
	</div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'
import { useBoardStore } from '@/stores/board'
import { userCheckStore } from '@/stores/usercheck'

const router = useRouter()
const store = useBoardStore()
const userStore = userCheckStore()

const title = ref('')
const content = ref('')
const image = ref(null)
const fileName = ref('')

const handleFileUpload = (event) => {
	image.value = event.target.files[0]
	fileName.value = image.value ? image.value.name : ''
}

const clearFile = () => {
	image.value = null
	fileName.value = ''
	document.getElementById('image').value = null
}

const createBoard = () => {
	const formData = new FormData()
	formData.append('title', title.value)
	formData.append('content', content.value)
	if (image.value) {
		formData.append('image', image.value)
	}

	axios({
		method: 'post',
		url: `${store.API_URL}/api/v1/boards/age/`, // Ensure this is the correct endpoint
		data: formData,
		headers: {
			Authorization: `Token ${userStore.token}`,
			// 'Content-Type': 'multipart/form-data',
		},
	})
		.then((response) => {
			router.push({ name: 'ageboard' })
		})
		.catch((error) => {
			console.log('Error:', error.response ? error.response.data : error.message)
		})
}

const cancel = () => {
	router.push({ name: 'ageboard' })
}
</script>

<style scoped>
.container {
	max-width: 1000px;
	margin: 0 auto;
	padding: 20px;
	border: 1px solid #ddd;
	border-radius: 8px;
	background-color: #f9f9f9;
}

nav {
	margin-bottom: 20px;
}

.nav-item {
  color: black;
  text-decoration: none;
}

.nav-item-here {
  color: black;
}


h1 {
	margin-bottom: 20px;
}

.form-container {
	display: flex;
	flex-direction: column;
}

.form-group {
	display: flex;
	align-items: center;
	margin-bottom: 10px;
}

.form-group label {
	width: 80px;
	margin-right: 10px;
}

.form-group input[type="text"],
.form-group textarea {
	flex: 1;
	padding: 8px;
	border: 1px solid #ccc;
	border-radius: 4px;
}

.form-group textarea {
	height: 100px;
	resize: vertical;
}

.form-actions {
	display: flex;
	justify-content: flex-end;
	margin-top: 20px;
}

.form-actions button,
.form-actions input[type="submit"] {
	padding: 10px 20px;
	margin-left: 10px;
	border: none;
	border-radius: 4px;
	cursor: pointer;
}

.form-actions button {
	background-color: #ccc;
}

.btn-submit {
	background-color: rgb(59, 130, 153);
	color: white;
}

.btn-submit:hover {
  background-color: rgb(45, 101, 119);
}
</style>
