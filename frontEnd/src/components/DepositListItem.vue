<template>
  <div class="container-fluid"> 
      <div class="col-md-6 mb-4" style="height: 500px;">
        <div class="card" @click="goDetail(deposit.fin_prdt_cd, deposit.id)" >
          <img :src="`/assets/banks/${deposit.kor_co_nm}.png`" class="card-img-top" alt="Bank Logo">
          <div class="card-body">
            <p class="card-text">{{ deposit.join_way }}</p>
            <h3 class="card-text">{{ deposit.fin_prdt_nm }}</h3>
            <h5 class="card-text">최대 우대금리: <strong>{{ calculateMaxRate(deposit.deposit_options).maxRate }}</strong>%</h5>
            <p class="card-text">기간: {{ calculateMaxRate(deposit.deposit_options).maxTerm }}개월</p>
            <button @click="goDetail(deposit.fin_prdt_cd, deposit.id)" class="btn btn-primary">상세보기</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { defineProps, computed } from 'vue'

const router = useRouter()
const props = defineProps({
  deposit: Object
})

const goDetail = function (bank, id) {
  router.push({ name: 'depositdetail', params: { fin_prdt_cd: bank, id: id } })
}

const calculateMaxRate = (depositOptions) => {
  let maxRate = 0;
  let maxTerm = 0;

  for (const option of depositOptions) {
    if (option.intr_rate > maxRate) {
      maxRate = option.intr_rate;
      maxTerm = option.save_trm;
    }
  }
  return { maxRate, maxTerm };
}
</script>

<style scoped>
.card {
  margin: 20px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
  width: 500px; 
  cursor: pointer;
}
img {
  padding: 50px;
  border: rgba(173, 170, 170, 0.555) 2px solid;
}
.card-body {
  border: rgba(173, 170, 170, 0.555) 2px solid;
}
.card-img-top {
  width: 100%;
  height: 15%;
  object-fit: cover;
}
.card-body {
  padding: 15px;
}
.btn-primary {
  margin-top: 10px;
  background-color: rgba(113, 166, 201, 0.856);
  border: none;
}
h3 {
  margin-bottom: 20px;
  font-weight: bold;
}
</style>
