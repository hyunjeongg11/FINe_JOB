<template>
  <div class="outer-box">
    <h4 class="page-title">{{ store.userId }} 님을 위한 추천 공고</h4>
    <div class="job-container">
      <div v-if="store.token">
        <div v-if="loading">
          <!-- 로딩 스피너 표시 -->
          <div class="spinner-grow" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
        </div>
        <div v-else-if="store.recommendJobs && store.recommendJobs.length > 0">
          <table class="job-table">
            <thead>
              <tr>
                <th class="table-header th-title">모집공고</th>
                <th class="table-header th-company">회사명</th>
                <th class="table-header th-location">근무지</th>
                <th class="table-header th-deadline">마감일</th>
                <th class="table-header th-experience">경력사항</th>
                <th class="table-header th-requirement">요구사항</th>
                <th class="table-header th-jobtype">근무형태</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="job in store.recommendJobs" :key="job.id">
                <td class="truncate td-title"><a :href="job.url" target="_blank">{{ job.title }}</a></td>
                <td class="truncate">{{ job.company }}</td>
                <td class="truncate">{{ job.location }}</td>
                <td class="truncate">{{ job.deadline }}</td>
                <td class="truncate">{{ job.experience }}</td>
                <td class="truncate">{{ job.requirement }}</td>
                <td class="truncate">{{ job.jobtype }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else>
          <p>추천공고를 확인하시려면 관심산업을 등록하세요</p>
          <p></p>
        </div>
      </div>
      <div v-else>
        <p>추천공고를 확인하시려면 로그인하세요.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { userCheckStore } from '@/stores/usercheck'

const store = userCheckStore()
const loading = ref(false)

onMounted (() => {
  loading.value = true; // 버튼 클릭 시 로딩 상태를 true로 변경
  setTimeout(() => {
    store.getRecommendJobs()
    loading.value = false; // 추천공고를 가져온 후 로딩 상태를 false로 변경
  }, 500);
})
</script>

<style scoped>
/* 기존 스타일 */
.page-title {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  padding: 15px 0;
}

.outer-box {
  background-color: rgb(219, 236, 241);
  border-radius: 10px;
  padding: 5px;
  width: 80%;
  margin: 0 auto;
}

.job-container {
  background-color: rgb(219, 236, 241);
  border-radius: 10px;
  text-align: center;
  margin: 0 auto;
  /* box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); */
  overflow: auto;
  max-width: 100%; 
}

.job-table {
  width: 100%;
}

.table-header {
  background-color: #edf2f7;
  font-weight: bold;
  font-size: 16px;
  padding: 12px 6px;
}

.spinner-grow {
  width: 2rem;
  height: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
  background-color: rgb(59, 130, 153);
}

.truncate {
  font-size: 15px;
  max-width: 150px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap; 
  padding: 10px 0;
}

a {
  color: rgb(0, 0, 0);
}

a:hover {
  color: rgb(59, 130, 153);
}

.td-title {
  width: 30%;
}

.td-company {
  width: 15%;
}

.td-location {
  width: 15%;
}

.td-deadline {
  width: 15%;
}

.td-experience {
  width: 10%;
}

.td-requirement {
  width: 10%;
}

.td-jobtype {
  width: 5%;
}

tr:nth-child(even) {
  background-color: #f8fafc;
}
</style>
