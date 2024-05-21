<template>
  <div class="container-fluid">
    <div class="cards-container">
      <div class="card-container" v-for="deposit in [props.deposit]" :key="deposit.id">
        <div class="card" @click="goDetail(deposit.fin_prdt_cd, deposit.id)">
          <img :src="`/assets/banks/${deposit.kor_co_nm}.png`" class="card-img-top" alt="Bank Logo">
          <div class="card-body">
            <p class="card-text">{{ deposit.join_way }}</p>
            <h3 class="card-text">{{ deposit.fin_prdt_nm }}</h3>
            <h5 class="card-text">최대 우대금리: <strong>{{ calculateMaxRate(deposit.deposit_options).maxRate }}</strong>%</h5>
            <p class="card-text">기간: {{ calculateMaxRate(deposit.deposit_options).maxTerm }}개월</p>
            <button class="btn btn-primary">상세보기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useRouter } from 'vue-router'
import { defineProps } from 'vue'

const router = useRouter()
const props = defineProps({
  deposit: Object
})

const goDetail = function (bank, id) {
  router.push({ name: 'depositdetail', params: { fin_prdt_cd: bank, id: id } })
}

const calculateMaxRate = (depositOptions) => {
  let maxRate = 0
  let maxTerm = 0

  for (const option of depositOptions) {
    if (option.intr_rate > maxRate) {
      maxRate = option.intr_rate
      maxTerm = option.save_trm
    }
  }
  return { maxRate, maxTerm }
}
</script>

<style scoped>
.cards-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px; /* Add space between the cards */
  justify-content: center; /* Center the cards horizontally */
}
.card-container {
  flex: 0 0 calc(33.33% - 20px); /* Ensure three cards per row */
  box-sizing: border-box;
}
.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px 0;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  width: 100%; /* Make sure the card takes full width of its container */
}
.card-img-top {
  width: 80%;
  margin: 0 auto;
  padding: 20px;
  height: auto;
  object-fit: cover;
}
.card-body {
  border: 2px solid rgba(173, 170, 170, 0.555);
  padding: 15px;
  width: 100%;
  text-align: center; /* Center text inside the card */
}
.btn-primary {
  margin-top: 10px;
  background-color: rgba(113, 166, 201, 0.856);
  border: none;
  color: white;
}
h3 {
  margin-bottom: 20px;
}
</style>
