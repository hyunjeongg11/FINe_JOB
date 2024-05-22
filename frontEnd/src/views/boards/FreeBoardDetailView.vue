<template>
  <div class="container">
    <nav>
      <RouterLink :to="{ name: 'freeboard' }" class="nav-item-here">자유게시판</RouterLink> | 
      <RouterLink :to="{ name: 'ageboard' }" class="nav-item">연령별게시판</RouterLink> | 
      <RouterLink :to="{ name: 'FAQ' }" class="nav-item">FAQ</RouterLink>
    </nav>
    <div v-if="isLogin">
      <div v-if="freeBoard">
        <div class="post-header">
          <h2>{{ freeBoard.title }}</h2>
          <div class="post-meta">
          <img :src="`/assets/profile.png`" alt="profile" style="height: 35px; width: 35px; border-radius: 20px;"> &nbsp;&nbsp;
             {{ freeBoard.user.username }} | {{ formattedCreatedAt }}
          </div>
          <hr>
        </div>
        <div class="post-content">
          <p>{{ freeBoard.content }}</p>
        </div>
        <div v-if="freeBoard.image" class="attachment">
          첨부파일: <a :href="freeBoard.image" download>{{ fileName }}</a>
        </div>
        <hr>
        <div class="comments-section">
          <!-- <h3>댓글</h3> -->
          <Comment />
        </div>
        <div class="actions-row">
          <button class="back" @click="goBack">목록으로</button>
          <div class="actions">
            <button class="fix" v-if="freeBoard.user.username === userStore.userId" @click="goToEditPage">게시글 수정</button>
            <button class="delete" v-if="freeBoard.user.username === userStore.userId" @click="deleteBoard">게시글 삭제</button>
          </div>
        </div>
      </div>
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
  return `${year}.${month}.${day} ${hours}:${minutes}`
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
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  /* border: 1px solid #ddd; */
  border-radius: 8px;
  /* background-color: #f9f9f9; */
}

h2 {
  margin-bottom: 25px;
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

.post-header {
  margin-bottom: 20px;
}

.post-header h1 {
  margin-bottom: 10px;
}

.post-meta {
  font-size: 14px;
  color: #555;
}

.post-content {
  margin-bottom: 20px;
  padding: 10px;
  /* border: 1px solid #ccc; */
  border-radius: 4px;
  background-color: #fff;
  height: 150px;
  /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); */
}

.attachment {
  margin-top: 20px;
}

.actions-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
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
  /* background-color: #def3f7; */
  color: black;
  cursor: pointer;
}

.fix:hover {
  background-color: rgb(126, 186, 205);
}

.delete {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  /* background-color: #f3b7bdb7; */
  color: black;
  cursor: pointer;
}

.delete:hover {
  background-color: #e7707c;
}

.back {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  color: black;
  cursor: pointer;
}

.back:hover {
  background-color: rgb(173, 216, 230);
}

.comments-section {
  margin-top: 20px;
}

.comments-section h3 {
  margin-bottom: 20px;
}
</style>
