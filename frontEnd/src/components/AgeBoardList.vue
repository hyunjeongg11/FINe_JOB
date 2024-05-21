<template>
  <div class="container">
    <h2>연령별게시판 목록</h2>
    <div class="filter-container">
      <label for="ageFilter">연령대 선택:</label>
      <select id="ageFilter" v-model="selectedAgeGroup" @change="filterByAgeGroup">
        <option value="">전체</option>
        <option value="20">20대 이하</option> 
        <option value="30">30대</option>
        <option value="40">40대</option>
        <option value="50">50대</option>
        <option value="60">60대</option>
        <option value="70">70대 이상</option>
      </select>
    </div>
    <table class="board-table" v-if="filteredBoards.length">
      <thead>
        <tr>
          <th class="title-col">제목</th>
          <th class="author-col">작성자</th>
          <th class="age-col">나이</th> 
          <th class="date-col">작성일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ageBoard in paginatedBoards" :key="ageBoard.id">
          <td>
            <RouterLink :to="{ name: 'ageboarddetail', params: { id: ageBoard.id } }">
              {{ ageBoard.title }}
            </RouterLink>
          </td>
          <td>{{ ageBoard.user.username }}</td>
          <td>{{ getAgeGroup(ageBoard.user.birthday, ageBoard.created_at) }}</td> 
          <td>{{ formatDateTime(ageBoard.created_at) }}</td>
        </tr>
      </tbody>
    </table>
    <div v-else>
      게시글이 없습니다!
    </div>
    <div class="actions" v-if="isLogin">
      <RouterLink :to="{ name: 'ageboardcreate' }" class="create-button">게시글 생성</RouterLink>
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
const userStore = userCheckStore()
const router = useRouter()
const currentPage = ref(1)
const itemsPerPage = 10
const selectedAgeGroup = ref('')

const calculateAgeOnDate = (birthday, date) => {
  const birthDate = new Date(birthday)
  const targetDate = new Date(date)
  let age = targetDate.getFullYear() - birthDate.getFullYear()
  const monthDifference = targetDate.getMonth() - birthDate.getMonth()

  // 생일이 아직 지나지 않은 경우 나이 - 1
  if (monthDifference < 0 || (monthDifference === 0 && targetDate.getDate() < birthDate.getDate())) {
    age--
  }
  return age
}


const getAgeGroup = (birthday, date) => {
  if (!birthday) {
    return '알 수 없음'
  }
  const age = calculateAgeOnDate(birthday, date)
  if (isNaN(age)) {
    return '알 수 없음'
  }
  if (age <= 20) {
    return '20대 이하'
  } else if (age >= 70) {
    return '70대 이상'
  } else {
    return `${Math.floor(age / 10) * 10}대`
  }
}

const filteredBoards = computed(() => {
  if (selectedAgeGroup.value) {
    const ageGroup = parseInt(selectedAgeGroup.value)
    return store.ageBoards.filter(board => {
      const age = calculateAgeOnDate(board.user.birthday, board.created_at)
      if (isNaN(age)) {
        return false
      }
      if (ageGroup === 20) {
        return age <= 20 
      } else if (ageGroup === 70) {
        return age >= 70
      } else {
        return age >= ageGroup && age < ageGroup + 10
      }
    })
  }
  return store.ageBoards
})

const paginatedBoards = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return filteredBoards.value.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(filteredBoards.value.length / itemsPerPage)
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

const filterByAgeGroup = () => {
  currentPage.value = 1
}

const formatDateTime = (datetime) => {
  const date = new Date(datetime)
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  return `${year}-${month}-${day}`
}

const isLogin = computed(() => userStore.isLogin)
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

.filter-container {
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

.title-col {
  width: 50%;
}

.author-col {
  width: 15%;
}

.age-col {
  width: 15%;
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
