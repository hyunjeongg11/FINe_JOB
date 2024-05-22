<template>
  <div class="container">
    <div class="header">
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
      <div v-if="isLogin">
        <RouterLink :to="{ name: 'ageboardcreate' }" class="create-button">게시글 작성</RouterLink>
      </div>
    </div>
    <hr>
    <div class="board-list" v-if="filteredBoards.length">
      <div class="board-item" v-for="ageBoard in paginatedBoards" :key="ageBoard.id">
        <div class="board-header">
          <RouterLink :to="{ name: 'ageboarddetail', params: { id: ageBoard.id } }">
            {{ ageBoard.title }}
          </RouterLink>
        </div>
        <div class="board-meta">
          <img :src="`/assets/profile.png`" alt="profile" style="height: 35px; width: 35px; border-radius: 20px;"> &nbsp;&nbsp;
          {{ ageBoard.user.username }} | {{ getAgeGroup(ageBoard.user.birthday, ageBoard.created_at) }} | {{ formatDateTime(ageBoard.created_at) }}
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

select {
  padding: 5px;
  border-radius: 4px;
  border: 1px solid #ddd;
  margin-left: 10px;

}
.filter-container {
  margin-right: 20px;
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
  background-color: rgb(59, 130, 153);
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
