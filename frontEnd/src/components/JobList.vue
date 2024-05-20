<template>
  <div>
    <h2>일자리 목록</h2>
    <select v-model="keyword">
      <option v-for="keyword in keywords" :key="keyword.id" :value="keyword">{{ keyword }}</option>
    </select>
    <JobListItem 
      v-for="jobBoard in store.jobBoards"
      :key="jobBoard.id"
      :jobBoard="jobBoard"
    />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import JobListItem from '@/components/JobListItem.vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()
const keyword = ref('')

const keywords = ref(['IT', '서비스', '금융', '보험', '인사', '노무', '회계', '세무', '재무', '디자인', '생산', '영업', '상품기획', '교육', 'R&D', '의료', '건축', '전기', '기계', '고객상담', '운송', '미디어', '스포츠', '복지'])

watch(keyword, () => {
  store.getJobBoards(keyword.value)
})

// const currentPage = ref(1)
// const itemsPerPage = 10

// const filteredBoards = computed(() => {
//   const start = (currentPage.value - 1) * itemsPerPage
//   const end = start + itemsPerPage
//   return store.jobBoards.slice(start, end)
// })

// const totalPages = computed(() => {
//   return Math.ceil(store.jobBoards.length / itemsPerPage)
// })

// const goToPage = (page) => {
//   currentPage.value = page
// }

// const prevPage = () => {
//   if (currentPage.value > 1) {
//     currentPage.value--
//   }
// }

// const nextPage = () => {
//   if (currentPage.value < totalPages.value) {
//     currentPage.value++
//   }
// }


</script>

<style scoped>

</style>