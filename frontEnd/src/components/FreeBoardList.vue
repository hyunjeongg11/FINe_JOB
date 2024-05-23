<template>
  <div class="container">
    <div class="header">
      <h2>자유게시판 목록</h2>
      <div v-if="isLogin">
        <RouterLink :to="{ name: 'freeboardcreate' }" class="create-button">게시글 작성</RouterLink>
      </div>
    </div>
    <hr>
    <div class="board-list" v-if="filteredBoards.length">
      <div class="board-item" v-for="freeBoard in filteredBoards" :key="freeBoard.id">
        <div class="board-header">
          <RouterLink :to="{ name: 'freeboarddetail', params: { id: freeBoard.id } }">
            {{ freeBoard.title }}
          </RouterLink>
        </div>
        <div class="board-meta">
          <img :src="`/assets/profile/profile${freeBoard.user.profile_img_index}.png`" alt="profile" style="height: 35px; width: 35px; border-radius: 20px;"> &nbsp;&nbsp;
          {{ freeBoard.user.username }} | {{ formatDateTime(freeBoard.created_at) }}
        </div>
        <hr />
      </div>
    </div>
    <div v-else>
      게시글이 없습니다!
    </div>
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">&lt;</button>
      <button v-for="page in totalPages" :key="page" @click="goToPage(page)" :class="{ active: currentPage === page }">
        {{ page }}
      </button>
      <button @click="nextPage" :disabled="currentPage === totalPages">&gt;</button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useBoardStore } from '@/stores/board'
import { userCheckStore } from '@/stores/usercheck'
import { useRouter, RouterLink } from 'vue-router'

const store = useBoardStore()
const userStore = userCheckStore() // 사용자 스토어 사용
const router = useRouter()
const currentPage = ref(1)
const itemsPerPage = 10

const filteredBoards = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return store.freeBoards.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(store.freeBoards.length / itemsPerPage)
})

const goToPage = (page) => {
  currentPage.value = page
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const formatDateTime = (datetime) => {
  const date = new Date(datetime)
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  return `${year}-${month}-${day}`
}

const isLogin = computed(() => userStore.isLogin) // 로그인 상태 계산

</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

h2 {
  text-align: left;
  margin-bottom: 20px;
}

.board-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.board-item {
  padding: 10px 0;
}

.board-header {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 20px;
}

.board-header a {
  color: #000; /* Black color for title */
  text-decoration: none;
}

.board-header a:hover {
  text-decoration: underline;
}

.board-meta {
  font-size: 14px;
  color: #555;
  margin-top: 5px;
}

hr {
  border: none;
  border-top: 1px solid #181616;
  margin: 10px 0;
}

.create-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: rgb(59, 130, 153)
;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.create-button:hover {
  background-color: rgb(59, 130, 153);
}

.pagination {
  text-align: center;
  margin-top: 20px;
}

.pagination button {
  padding: 5px 10px;
  margin: 0 2px;
  border: 1px solid #ddd;
  background-color: #fff;
  cursor: pointer;
  color: rgb(59, 130, 153);
}

.pagination button.active {
  background-color: rgb(59, 130, 153);
  color: white;
}

.pagination button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>
