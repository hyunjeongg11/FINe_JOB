[SavingListItem.vue]
<template>
  <div class="container-fluid">
    <div class="cards-container">
      <div class="card" @click="goDetail(saving.fin_prdt_cd, saving.id)">
        <div class="card-content">
          <div class="card-img-container">
            <img :src="`/assets/banks/${saving.kor_co_nm}.png`" class="card-img" alt="Bank Logo">
            <p class="bank-name">{{ saving.kor_co_nm }}</p>
          </div>
          <div class="card-text-content">
            <p class="join-way">{{ saving.join_way }}</p>
            <h4 class="product-name">{{ saving.fin_prdt_nm }}</h4>
            <h5 class="rate">최대 우대금리: <strong>{{ calculateMaxRate(saving.saving_options).maxRate }}</strong>%</h5>
            <p class="term">기간: {{ calculateMaxRate(saving.saving_options).maxTerm }}개월</p>
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
import { userCheckStore } from '@/stores/usercheck'

const router = useRouter()
const userStore = userCheckStore() 
const props = defineProps({
  saving: Object
})

const goDetail = function (bank, id) {
  if (!userStore.isLogin) {
    alert('로그인 해주세요')
    router.push({ name: 'login' })
  } else {
    router.push({ name: 'savingdetail', params: { fin_prdt_cd: bank, id: id } })
  }
}

const calculateMaxRate = (savingOptions) => {
  let maxRate = 0
  let maxTerm = 0

  for (const option of savingOptions) {
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
  justify-content: space-between;
  gap: 20px;
}

.card-container {
  flex: 0 0 calc(33.33% - 20px);
  box-sizing: border-box;
  margin-bottom: 20px;
}

.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* box-shadow: 0 0 15px rgba(0, 0, 0, 0.2); */
  cursor: pointer;
  width: 100%;
  background-color: white;
  border: none;
}

.card-content {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  padding: 20px;
}

.card-img-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
  margin-right: 20px;
}

.card-img {
  width: 100px;
  height: 100px;
  margin-bottom: 10px;
}

.bank-name {
  margin-top: 10px;
  font-size: 14px;
  text-align: center;
}

.card-text-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex: 1;
  padding-left: 10px;
}

.join-way,
.product-name,
.rate,
.term {
  margin-bottom: 10px;
}

.btn-primary {
  margin-top: 10px;
  background-color: rgba(113, 166, 201, 0.856);
  border: none;
  color: white;
}
</style>
