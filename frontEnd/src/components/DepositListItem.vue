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
.container-fluid {
  width: 30%;
  margin: 0 auto; /* Center the container */
}

.cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin: 20px 0;
}

.card-container {
  flex: 1 1 30%;
  margin: 10px;
}

.card {
  cursor: pointer;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 400px; /* Adjusted height to fit all content */
}

.card-img-top {
  width: 100%;
  height: 150px; /* Fixed height to maintain aspect ratio */
  object-fit: cover;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.card-body {
  padding: 15px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
}

.card-text {
  margin: 5px 0;
  flex-grow: 1; /* Allow text to grow and take available space */
}

.btn-primary {
  background-color: #007bff;
  border: none;
  padding: 10px 20px;
  margin-top: 10px;
  cursor: pointer;
  border-radius: 5px;
  color: white;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>
