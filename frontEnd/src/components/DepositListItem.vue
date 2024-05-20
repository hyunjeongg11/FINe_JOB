<template>
  <div @click="goDetail(deposit.fin_prdt_cd, deposit.id)">
    <table class="styled-table">
      <thead>
        <tr class="align-middle">
          <th rowspan="2">공시제출월</th>
          <th rowspan="2">은행이름</th>
          <th rowspan="2">상품명</th>
          <th colspan="2" v-for="option in deposit.deposit_options" :key="option.id">
            금리 및 기간
          </th>
        </tr>
        <tr>
          <!-- Modify the loop to interleave rate and term pairs -->
          <template v-for="option in deposit.deposit_options" :key="option.id">
            <th>우대금리</th>
            <th>가입기간</th>
          </template>
        </tr>
      </thead>
      <tbody>
        <tr v-if="deposit">
          <td>{{ deposit.dcls_month }}</td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <!-- Ensure that rate and term are presented as pairs in the data rows as well -->
          <template v-for="option in deposit.deposit_options">
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
  deposit: Object
})

const goDetail = function (bank, id) {
  router.push({ name: 'depositdetail', params: { fin_prdt_cd: bank, id: id } })
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
  background-color:  rgb(238 245 255);
  color: rgba(0, 0, 0, 0.747);
  text-align: left;
}
.styled-table th,
.styled-table td {
  padding: 12px 15px;
  border: 1px solid #dddddd; /* Improved visibility with consistent borders */
}
.styled-table th:last-child,
.styled-table td:last-child {
  border-right: none; /* Avoid double border on the last column */
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
