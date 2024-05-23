<template>
  <div class="container">
    <h2>FAQ 목록</h2>
    <hr>
    <div class="board-list" v-if="filteredBoards.length">
      <div class="board-item" v-for="board in filteredBoards" :key="board.id">
        <div class="board-header">
          <a :href="board.url" target="_blank">
            {{ board.subject }}
          </a>
        </div>
        <div class="board-meta">
          {{ formatDate(board.registerDate) }}
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

const store = useBoardStore()
const currentPage = ref(1)
const itemsPerPage = 10

const filteredBoards = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return store.faqBoards.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(store.faqBoards.length / itemsPerPage)
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

const formatDate = (dateString) => {
  const date = new Date(dateString)
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  return `${year}-${month}-${day}`
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
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
  color: #000;
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
  /* background-color: #007bff; */
  background-color: rgb(59, 130, 153);
  color: white;
}

.pagination button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>
