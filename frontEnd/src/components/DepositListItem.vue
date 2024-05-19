
<template>
    <div @click="goDetail(deposit.fin_prdt_cd, deposit.id)">
    <table class="styled-table">
      <thead>
        <tr class="align-middle">
          <th rowspan="2">공시제출월</th>
          <th rowspan="2">은행이름</th>
          <th rowspan="2">상품명</th>
          <th colspan="2" v-for="(option, index) in deposit.deposit_options" :key="index">
            우대금리 / 가입기간
          </th>
        </tr>
        <tr>
          <th v-for="(option, index) in deposit.deposit_options" :key="index">
            우대금리
          </th>
          <th v-for="(option, index) in deposit.deposit_options" :key="index">
            가입기간
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="deposit">
          <td>{{ deposit.dcls_month }}</td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <td v-for="option in deposit.deposit_options" :key="option.intr_rate">
            <p>{{ option.intr_rate }}</p>
          </td>
          <td v-for="option in deposit.deposit_options" :key="option.save_trm">
            <p>{{ option.save_trm }}</p>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { watch } from 'vue'
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
  width: 100%;
  font-size: 18px;
  text-align: left;
  margin-bottom: 20px;
}

.styled-table th,
.styled-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

.styled-table th {
  background-color: #f2f2f2;
}

.styled-table tr:hover {
  background-color: #f5f5f5;
}
</style>