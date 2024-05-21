<template>
  <div class="container">
    <table class="board-table">
      <thead>
        <tr>
          <th class="title-col">주제</th>
          <th class="date-col">등록일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="board in filteredBoards" :key="board.id">
          <td><a :href="board.url" target="_blank">{{ board.subject }}</a></td>
          <td>{{ board.registerDate }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useBoardStore } from '@/stores/board'
import FAQBoardList from '@/components/FAQBoardList.vue'
import { useRouter, RouterLink } from 'vue-router'

const store = useBoardStore()
const router = useRouter()
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

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.board-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.board-table th,
.board-table td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: center;
}

.board-table th {
  background-color: #f1f1f1;
}

.board-table td a {
  color: #007bff;
  text-decoration: none;
}

.board-table td a:hover {
  text-decoration: underline;
}

/* Add width percentages for columns */
.title-col {
  width: 60%;
}

.author-col {
  width: 20%;
}

.date-col {
  width: 20%;
}

.actions {
  text-align: right;
  margin-bottom: 20px;
}

.create-button {
  display: inline-block;
  padding: 10px 20px;
  margin-top: 10px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.create-button:hover {
  background-color: #0056b3;
}

.pagination {
  text-align: center;
}

.pagination button {
  padding: 5px 10px;
  margin: 0 2px;
  border: 1px solid #ddd;
  background-color: #fff;
  cursor: pointer;
}

.pagination button.active {
  background-color: #007bff;
  color: white;
}

.pagination button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>
