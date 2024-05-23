[SavingList.vue]
<template>
  <div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1 class="mb-0">{{ isRecommendVisible ? '적금 상품 추천받기' : '적금 상품 검색하기' }}</h1>
      <button v-if="isRecommendVisible" @click="toggleSearch" class="btn button_blue">검색하기로 이동</button>
      <button v-if="isSearchVisible" @click="toggleRecommend" class="btn button_blue">추천받기로 이동</button>
    </div>
    <hr>

    <div v-if="isSearchVisible">
      <h3 class="mb-3">검색 조건을 입력하세요</h3>
      <form @submit.prevent="onClickFilter">
        <div class="row">
          <div class="col-md-4">
            <p>은행을 선택하세요.</p>
            <select name="bank" id="bank" v-model="bank" class="form-control">
              <option value="전체 은행">전체 은행</option>
              <option :value="bk" v-for="bk in bankList">{{ bk }}</option>
            </select>
          </div>
          <div class="col-md-4">
            <p>예치기간을 선택하세요.</p>
            <select name="term" id="term" v-model="term" class="form-control">
              <option value="전체 기간">전체 기간</option>
              <option value="6">6 개월</option>
              <option value="12">12 개월</option>
              <option value="24">24 개월</option>
              <option value="36">36 개월</option>
            </select>
          </div>
          <div class="col-md-2 mt-4 d-flex justify-content-start">
            <input type="submit" value="검색하기" class="btn button_blue" style="width: 100px;">
          </div>
        </div>
      </form>
    </div>
    <div v-if="isRecommendVisible">
      <h3 class="mb-3">추천 조건을 입력하세요</h3>
      <form @submit.prevent="onClickRecommend">
        <div class="row">
          <div class="col-md-4">
            <label for="inputAmount">예치금액을 입력하세요</label>
            <input type="number" id="inputAmount" v-model="inputAmount" class="form-control" :min="0">
          </div>
          <div class="col-md-4">
            <label for="targetAmount">목표금액을 입력하세요</label>
            <input type="number" id="targetAmount" v-model="targetAmount" class="form-control" :min="0">
          </div>
          <div class="col-md-2 mt-4 d-flex justify-content-start">
            <input type="submit" value="추천받기" class="btn button_blue" style="width: 100px;">
          </div>
        </div>
      </form>
    </div>
  </div>

  <div class="container">
    <hr>
    <h4>적금 상품 목록</h4>
    <div v-if="isSearchVisible">
      <div class="grid-container" v-if="result.length > 0">
        <SavingListItem v-for="saving in result" :key="saving.id" :saving="saving" class="grid-item" />
      </div>
      <div v-else>
        <p class="text-center">조건에 맞는 결과가 없습니다.</p>
      </div>
    </div>
    <div v-else>
      <div class="grid-container" v-if="store.recommendSavingList.length > 0">
        <SavingListItem v-for="saving in store.recommendSavingList" :key="saving.id" :saving="saving" class="grid-item" />
      </div>
      <div v-else>
        <p class="text-center">조건에 맞는 결과가 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import SavingListItem from '@/components/SavingListItem.vue'

const store = useFinanceStore()
const bankList = [
  '우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행',
  '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행',
  '한국산업은행', '국민은행', '신한은행', '농협은행주식회사',
  '하나은행', '수협은행', '주식회사 케이뱅크',
  '주식회사 카카오뱅크', '토스뱅크 주식회사'
]

const bank = ref('전체 은행')
const term = ref('전체 기간')

const isSearchVisible = ref(true)
const isRecommendVisible = ref(false)

const toggleSearch = () => {
  isSearchVisible.value = true
  isRecommendVisible.value = false
}

const toggleRecommend = () => {
  isSearchVisible.value = false
  isRecommendVisible.value = true
}

// Recommendation form data
const inputAmount = ref(0)
const targetAmount = ref(0)

// 기간만 필터링
const termFilter = function (term) {
  const result = []
  for (const product of store.savingList) {
    const saving_list = []
    for (const option of product.saving_options) {
      if (option.save_trm == term) {
        saving_list.push(option)
      }
    }
    if (saving_list.length != 0) {
      product.saving_list = saving_list
      result.push(product)
    }
  }
  return result
}

// 기간과 은행을 같이 필터링
const termBankFilter = function (bank, term) {
  const result = []
  for (const product of store.savingList) {
    if (product.kor_co_nm === bank) {
      const saving_list = []
      for (const option of product.saving_options) {
        if (option.save_trm == term) {
          saving_list.push(option)
        }
      }
      if (saving_list.length != 0) {
        product.saving_options = saving_list
        result.push(product)
      }
    }
  }
  return result
}

watch(() => store.recommendSavingList, (newValue) => {
  result.value = newValue
})

const result = ref([])
const onClickFilter = function () {
  if (bank.value === '전체 은행' && term.value === '전체 기간') {
    result.value = store.savingList
  } else if (bank.value === '전체 은행' && term.value !== '전체 기간') {
    result.value = termFilter(term.value)
  } else if (bank.value !== '전체 은행' && term.value === '전체 기간') {
    // 은행만 필터링
    result.value = store.savingList.filter((item) => item.kor_co_nm === bank.value)
  } else {
    result.value = termBankFilter(bank.value, term.value)
  }
}

const onClickRecommend = function () {
  const amount = {
    inputAmount: inputAmount.value,
    targetAmount: targetAmount.value
  }
  store.getSavingRecommendation(amount)
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr); 
  gap: 20px;
}

.grid-item {
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px;
  height: auto;
  width: 100%;
}

#inputAmount, #targetAmount {
  margin-top: 10px;
}

.button_blue {
  background-color: rgb(59 130 153);
  color: white;
}


label {
  display: inline-block;
  margin-bottom: 0.5rem;
}

form .row > div {
  display: flex;
  flex-direction: column;
}

form .row > div > input, form .row > div > select {
  margin-top: auto;
}

form .row > div.mt-4.d-flex.justify-content-center, form .row > div.mt-4.d-flex.justify-content-start {
  margin-top: auto;
  justify-content: flex-start !important;
}
</style>