<template>
  <div>
    <h1 class="job-search-title mb-4">일자리 검색</h1>
    <h2 class="job-search-title mb-3">관심 산업을 선택하세요</h2>
    <select class="job-search-title form-select" v-model="keyword">
      <option value="" disabled selected>산업군</option>
      <option v-for="kw in keywords" :key="kw" :value="kw">{{ kw }}</option>
    </select>
    <br>
    <div class="outer-box">
      <div v-if="!keyword" class="keyword-title">모든 산업 공고</div>
      <div v-else class="keyword-title">{{ keyword }} 산업 공고</div>
      <div v-if="loading" class="spinner-container">
        <div class="spinner-grow" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      <div v-else class="job-container">
        <table class="job-table">
          <thead>
            <tr>
              <th class="table-header">모집공고</th>
              <th class="table-header">회사</th>
              <th class="table-header">마감일</th>
              <th class="table-header">근무지</th>
              <th class="table-header">경력사항</th>
              <th class="table-header">요구사항</th>
              <th class="table-header">근무형태</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="jobBoard in paginatedJobBoards" :key="jobBoard.id">
              <td><a :href="jobBoard.url" target="_blank">{{ jobBoard.title }}</a></td>
              <td class="truncate">{{ jobBoard.company }}</td>
              <td class="truncate">{{ jobBoard.deadline }}</td>
              <td class="truncate">{{ jobBoard.location }}</td>
              <td class="truncate">{{ jobBoard.experience }}</td>
              <td class="truncate">{{ jobBoard.requirement }}</td>
              <td class="truncate">{{ jobBoard.jobtype }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">&lt;</button>
        <button v-for="page in totalPages" :key="page" @click="goToPage(page)" :class="{ active: currentPage === page }">
          {{ page }}
        </button>
        <button @click="nextPage" :disabled="currentPage === totalPages">&gt;</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()
const keyword = ref('')
const loading = ref(false)

const keywords = ref(['IT', '서비스', '금융', '보험', '인사', '노무', '회계', '세무', '재무', '디자인', '생산', '영업', '상품기획', '교육', 'R&D', '의료', '건축', '전기', '기계', '고객상담', '운송', '미디어', '스포츠', '복지'])

watch(keyword, async () => {
  loading.value = true
  setTimeout(async () => {
    await store.getJobBoards(keyword.value)
    loading.value = false
  }, 200)
})

const currentPage = ref(1)
const itemsPerPage = 10

const paginatedJobBoards = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return store.jobBoards.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(store.jobBoards.length / itemsPerPage)
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
.job-search-title {
  margin-left: 10%;
}

.job-table {
  width: 100%;
  border-collapse: collapse;
}

.job-container {
  border-radius: 10px;
  text-align: center;
  margin: 0 auto;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  overflow: auto;
  max-width: 100%;
}

.table-header {
  background-color: #edf2f7;
  padding: 10px 10px;
}

.job-table td {
  padding: 10px;
  border: 1px solid #ddd;
}

a {
  color: rgb(0, 0, 0);
}

a:hover {
  color: rgb(59, 130, 153);
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

.outer-box {
  background-color: rgb(219, 236, 241);
  border-radius: 10px;
  padding: 5px;
  width: 80%;
  margin: 0 auto;
}

tr:nth-child(even) {
  background-color: #f8fafc;
}

tr:nth-child(odd) {
  background-color: white;
}

.job-table td {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.form-select {
  width: 20%;
}

.keyword-title {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  padding-top: 5px;
  border-radius: 10px;
  width: 90%;
  margin: 10px auto;
}

.spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
}

.spinner-grow {
  width: 5rem;
  height: 5rem;
  background-color: rgb(59, 130, 153);
}

.spinner-grow .visually-hidden {
  display: none;
}

.spinner-container {
  background-color: rgb(219, 236, 241);
  border-radius: 10px;
  margin: 10px 10px;
}
</style>
