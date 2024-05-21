<template>
  <button @click="goBack" class="back-button">뒤로 가기</button>
  <div class="container">
    <nav>
      <RouterLink :to="{ name: 'freeboard' }">자유게시판</RouterLink> |
      <RouterLink :to="{ name: 'ageboard' }">연령별 게시판</RouterLink> |
      <RouterLink :to="{ name: 'FAQ' }">FAQ</RouterLink>
    </nav>
    <div v-if="isLogin">
      <div v-if="freeBoard">
        <h3>자유게시판</h3>
        <div class="post-header">
          <h1>{{ freeBoard.title }}</h1>
          <div class="post-meta">
            <p>작성자 : {{ freeBoard.user.username }}</p>
            <p>작성시간 : {{ formattedCreatedAt }}</p>
            <p>수정시간 : {{ formattedUpdatedAt }}</p>
          </div>
        </div>
        <div class="post-content">
          <div class="content-box">
            <p>{{ freeBoard.content }}</p>
          </div>
        </div>
        <div v-if="freeBoard.image" class="attachment">
          <p>첨부파일: <a :href="freeBoard.image" download>{{ fileName }}</a></p>
        </div>
        <div class="actions">
          <button class="fix" v-if="freeBoard.user.username === userStore.userId" @click="goToEditPage">수정</button>
          <button class="fix" v-if="freeBoard.user.username === userStore.userId" @click="deleteBoard">삭제</button>
        </div>
      </div>
      <Comment />
    </div>
  </div>
</template>

<script setup>
import { RouterLink, useRoute, useRouter } from 'vue-router'
import Comment from '@/components/FreeBoardComment.vue'
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useBoardStore } from '@/stores/board'
import { userCheckStore } from '@/stores/usercheck'

const store = useBoardStore()
const userStore = userCheckStore()
const route = useRoute()
const router = useRouter()
const freeBoard = ref(null)
const isLogin = computed(() => userStore.isLogin)

function goBack() {
    router.back()
}

onMounted(() => {
  if (!isLogin.value) {
    alert('로그인 해주세요')
    router.push({ name: 'login' })
  } else {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/boards/free/${route.params.id}`,
      headers: {
        Authorization: `Token ${userStore.token}` // 인증 토큰을 헤더에 추가
      }
    })
      .then((res) => {
        console.log(res.data)
        freeBoard.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
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
  return `${year}.${month}.${day} ${period} ${formattedHours}:${minutes}`
}

const formattedCreatedAt = computed(() => {
  return freeBoard.value ? formatDateTime(freeBoard.value.created_at) : ''
})

const formattedUpdatedAt = computed(() => {
  return freeBoard.value ? formatDateTime(freeBoard.value.updated_at) : ''
})

const goToEditPage = () => {
  router.push(`/freeboarddetail/${route.params.id}/update`)
}

const deleteBoard = () => {
  if (confirm('정말로 이 게시글을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/boards/free/${route.params.id}`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(() => {
        alert('게시글이 삭제되었습니다.')
        router.push({ name: 'freeboard' })
      })
      .catch((err) => {
        console.log(err)
        alert('게시글 삭제에 실패했습니다.')
      })
  }
}

const fileName = computed(() => {
  if (freeBoard.value && freeBoard.value.image) {
    const parts = freeBoard.value.image.split('/')
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

.post-meta p {
  margin: 0;
  line-height: 1.5;
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

.actions {
  display: flex;
  gap: 10px;
}

.fix {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.fix:hover {
  background-color: #0056b3;
}

.fix + .fix {
  background-color: #dc3545;
}

.fix + .fix:hover {
  background-color: #c82333;
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
