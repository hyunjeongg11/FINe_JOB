<template>
      <button @click="goBack" class="back-button">
      <img :src="`/assets/back.png`" alt="뒤로가기" style="width: 50px; height: 50px;">
    </button>
  <div class="container mt-5">
    <h1 class="mb-4">{{ detail.fin_prdt_nm }} 상품 상세 정보</h1>
    <div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
      <div class="btn-group me-2" role="group" aria-label="First group">
        <button @click="onClick" class="btn" :class="{'btn-primary': buttonText === '가입하기', 'btn-danger': buttonText === '해지하기'}">{{ buttonText }}</button>
      </div>
      <div class="btn-group me-2" role="group" aria-label="Second group">
        <button @click="moveToLink(store.searchBankLink(detail.kor_co_nm))" class="btn btn-secondary">은행홈페이지</button>
      </div>
    </div>
    
    

    <div class="mt-4">
      <h5><strong>추가 정보:</strong></h5>
      <ul class="list-group">
        <li class="list-group-item"><strong>공시 제출월 :</strong> {{ detail.dcls_month }}</li>
        <li class="list-group-item"><strong>금융회사명 :</strong> {{ detail.kor_co_nm }}</li>
        <li class="list-group-item"><strong>가입 방법 :</strong> {{ detail.join_way }}</li>
        <li class="list-group-item"><strong>가입 대상 :</strong> {{ detail.join_member }}</li>
        <li class="list-group-item"><strong>우대 조건 :</strong> {{ detail.spcl_cnd }}</li>
      </ul>
    </div>

    <div class="table-responsive mt-4">
      <table class="table table-striped">
        <thead class="table-dark">
          <tr class="text-center">
            <th>저축 금리 유형</th>
            <th>저축 금리</th>
            <th>우대 금리</th>
            <th>저축 기간</th>
          </tr>
        </thead>
        <tbody class="text-center">
          <tr v-for="option in detail.saving_options" :key="option.intr_rate">
            <td>{{ option.intr_rate_type_nm }}</td>
            <td>{{ option.intr_rate }}</td>
            <td>{{ option.intr_rate2 }}</td>
            <td>{{ option.save_trm }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <strong>etc :</strong>
    <p class="mt-4">{{ detail.etc_note }}</p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { userCheckStore } from '@/stores/usercheck'
import { useRoute, useRouter } from 'vue-router'

const store = useFinanceStore()
const userStore = userCheckStore()
const detail = ref('')

const route = useRoute()
const router = useRouter()

const fin_prdt_cd = route.params.fin_prdt_cd

function goBack() {
    router.back();
}


onMounted(() => {
  // if (store.userId == null) {
  //   router.push({name: 'login'})
  // }
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/financial_products/saving_product_detail/${fin_prdt_cd}/`,
    headers: {
        Authorization: `Token ${userStore.token}`
      }
  })
    .then((res) => {
      detail.value = res.data
      // console.log(res.data)
      check_likes_user()
    })
    .catch((err) => {
      console.log(err)
    })
})

const check_likes_user = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/financial_products/like_saving_check/${route.params.id}/`,
    headers: {
        Authorization: `Token ${userStore.token}`

      }
  })
    .then((res) => {
      if (res.data.user) {
        buttonText.value = '해지하기'
      }
      else {
        buttonText.value = '가입하기'
      }
    })
    .catch((err) => {
      console.log(err)
    })
}

const buttonText = ref('')
const onClick = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/financial_products/like_saving/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then((res) => {
      // console.log(res.data.liked)
      if (res.data.liked) {
        buttonText.value = "해지하기"
      } else {
        buttonText.value = "가입하기"
      }
    })
    .catch((err) => {
      // console.log(route.params.id)
      console.log(err)
    })
}

const moveToLink = function (link) {
  window.open(link)
}
</script>

<style scoped>
.back-button {
    margin: 0px 10px;
    /* padding: 5px 10px; */
    font-size: 16px;
    color: black;
    background-color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.back-button:hover {
    background-color: rgb(165, 165, 165);
}
</style>