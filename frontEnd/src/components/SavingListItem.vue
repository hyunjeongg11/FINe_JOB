<template>
  <div @click="goDetail(saving.fin_prdt_cd, saving.id)">
    <table class="styled-table">
      <thead>
        <tr>
          <th rowspan="2">공시제출월</th>
          <th rowspan="2">은행이름</th>
          <th rowspan="2">상품명</th>
          <th colspan="2" v-for="option in saving.saving_options" :key="option.id">
            금리 및 기간
          </th>
        </tr>
        <tr>
          <!-- Correctly pair headers for rates and terms -->
          <template v-for="option in saving.saving_options" :key="option.id">
            <th>우대금리</th>
            <th>가입기간</th>
          </template>
        </tr>
      </thead>
      <tbody>
        <tr v-if="saving">
          <td>{{ saving.dcls_month }}</td>
          <td>{{ saving.kor_co_nm }}</td>
          <td>{{ saving.fin_prdt_nm }}</td>
          <!-- Display rate and term pairs in data rows -->
          <template v-for="option in saving.saving_options">
            <td>{{ option.intr_rate }}</td>
            <td>{{ option.save_trm }}</td>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

defineProps({
  saving: Object
})

const goDetail = function (bank, id) {
  router.push({name: 'savingdetail', params: {fin_prdt_cd: bank, id: id}})
}
</script>

<style scoped>
.styled-table {
  border-collapse: collapse;
  margin: 20px 0;
  width: 100%;
  font-size: 15px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
.styled-table thead tr {
  background-color: rgb(238 245 255);
  color: rgba(0, 0, 0, 0.747);
  text-align: left;
}
.styled-table th,
.styled-table td {
  padding: 12px 15px;
  border: 1px solid #dddddd;
}

.styled-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
  border-bottom: 2px solid rgb(238 245 255);
}
/* .styled-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
} */
</style>
