<template>
  <div class="container">
    <nav>
      <RouterLink :to="{ name: 'freeboard' }" class="nav-item-here">자유게시판</RouterLink> | 
      <RouterLink :to="{ name: 'ageboard' }" class="nav-item">연령별게시판</RouterLink> | 
      <RouterLink :to="{ name: 'FAQ' }" class="nav-item">FAQ</RouterLink>
    </nav>
    <h1>자유 게시글 수정</h1>
    <form @submit.prevent="submitEdit" class="form-container">
      <div class="form-group">
        <label for="title">제목 :</label>
        <input type="text" id="title" v-model.trim="title" placeholder="제목을 입력해주세요" />
      </div>
      <div class="form-group">
        <label for="content">내용 :</label>
        <textarea id="content" v-model.trim="content" placeholder="내용을 입력해주세요"></textarea>
      </div>
      <div class="form-group">
        <label for="file">파일 첨부 :</label>
        <input type="file" id="file" @change="handleFileUpload" />
        <div v-if="fileName">{{ fileName }}</div>
        <button type="button" @click="clearFile">전체 삭제</button>
      </div>
      <div class="form-actions">
        <button type="button" @click="cancel">취소</button>
        <input class="submit-btn" type="submit" value="저장" />
      </div>
    </form>
  </div>
</template>

<script setup>
import { RouterLink, useRouter, useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'

const router = useRouter()
const route = useRoute()
const userStore = userCheckStore()
const store = useBoardStore()

const title = ref('')
const content = ref('')
const file = ref(null)
const fileName = ref('')

const handleFileUpload = (event) => {
  file.value = event.target.files[0]
  fileName.value = file.value ? file.value.name : ''
}

const clearFile = () => {
  file.value = null
  fileName.value = ''
  document.getElementById('file').value = null
}

const fetchBoardData = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/boards/free/${route.params.id}`,
    headers: {
      Authorization: `Token ${userStore.token}` // 인증 토큰을 헤더에 추가
    }
  })
    .then((res) => {
      title.value = res.data.title
      content.value = res.data.content
    })
    .catch((err) => {
      console.log(err)
    })
}

onMounted(() => {
  fetchBoardData()
})

const submitEdit = () => {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('content', content.value)
  if (file.value) {
    formData.append('file', file.value)
  }

  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/boards/free/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`, // 인증 토큰을 헤더에 추가
      'Content-Type': 'multipart/form-data',
    },
    data: formData,
  })
    .then(() => {
      router.push({ name: 'freeboarddetail', params: { id: route.params.id } })
    })
    .catch((err) => {
      console.log(err)
    })
}

const cancel = () => {
  router.push({ name: 'freeboarddetail', params: { id: route.params.id } })
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

.form-actions input[type="submit"] {
  /* background-color: #007bff; */
  color: white;
}

.submit-btn {
  background-color: rgb(59, 130, 153);
  color: white;
}
</style>
