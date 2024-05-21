<template>
  <div class="container">
    <h1 class="mb-4">적금 상품</h1>
    <div class="d-flex justify-content-between mb-3">
      <button v-if="!isRecommendVisible" @click="toggleRecommend" class="btn button_blue">추천받기</button>
      <button v-if="!isSearchVisible" @click="toggleSearch" class="btn button_blue">검색하기</button>
    </div>
    <hr>

    <div v-if="isSearchVisible">
      <h2 class="mb-3">검색 조건을 입력하세요</h2>
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
              <option value="6">6개월</option>
              <option value="12">12개월</option>
              <option value="24">24개월</option>
              <option value="36">36개월</option>
            </select>
          </div>
          <div class="col-md-2 mt-4 d-flex justify-content-center">
            <input type="submit" value="검색" class="btn button_blue">
          </div>
        </div>
      </form>
    </div>

    <div v-if="isRecommendVisible">
      <h2 class="mb-3">추천 조건을 입력하세요</h2>
      <form @submit.prevent="onClickRecommend">
        <div class="row">
          <div class="col-md-4">
            <label for="inputAmount">예치금액을 입력하세요</label>
            <input type="number" id="inputAmount" v-model="inputAmount" class="form-control" :min="0">
          </div>
          <div class="col-md-4">
            <label for="targetAmount">목표 금액을 입력하세요</label>
            <input type="number" id="targetAmount" v-model="targetAmount" class="form-control" :min="0">
          </div>
          <div class="col-md-2 mt-4 d-flex justify-content-center">
            <input type="submit" value="추천받기" class="btn button_blue">
          </div>
        </div>
      </form>
    </div>
  </div>

  <div class="container">
    <button @click="toggleCalculator" class="btn my-2 button_blue">{{ isOpen ? '이자계산기 닫기' : '이자계산기 열기' }}></button>
    <div v-if="isOpen">
      <h4>간편 예적금 계산기</h4>
      <div>저축 방식 :
        <select v-model="type" class="form-control">
          <option disabled value="">유형을 선택해 주세요</option>
          <option>예금</option>
          <option>적금</option>
        </select>
      </div>
      <div>
        <label for="inputmoney">예치 금액 : </label>
        <input type="number" id="inputmoney" v-model="inputmoney" :min="0" class="form-control">원
      </div>
      <div>이자 방식 :
        <select v-model="intr_rate_type" class="form-control">
          <option disabled value="">유형을 선택해 주세요</option>
          <option>단리</option>
          <option>복리</option>
        </select>
      </div>
      <div>
        <label for="save_trm">예금 기간 : </label>
        <input type="number" id="save_trm" v-model="save_trm" :min="0" class="form-control">(개월)
      </div>
      <div>    
        <label for="intr_rate">연이자율 : </label>
        <input type="number" id="intr_rate" v-model="intr_rate" :min="0" class="form-control">(%)
      </div>
      <div>
        <p><strong>원금 합계 : </strong>{{ calinput.toLocaleString('ko-KR') }}(원)</p>
      </div>
      <div>
        <p><strong>세전이자 :</strong> {{ beforintr.toLocaleString('ko-KR') }}(원)</p>
      </div>
      <div>
        <p><strong>이자과세 :</strong> -{{ taxintr.toLocaleString('ko-KR') }}(원)</p>
      </div>
      <div>
        <p><strong>세후 수령액 :</strong>{{ mymoney.toLocaleString('ko-KR') }}(원)</p>
        <button @click.prevent="calculator()" class="btn button_blue">계산</button>
      </div>
    </div>

    <div>
      <hr>
      <h2>적금 리스트</h2>
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
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import SavingListItem from '@/components/SavingListItem.vue'
import axios from 'axios';

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

// Period only filter
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

// Period and bank filter
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
    // Bank only filter
    result.value = store.savingList.filter((item) => {
      if (item.kor_co_nm === bank.value) {
        return item
      }
    })
  } else {
    result.value = termBankFilter(bank.value, term.value)
  }
  // console.log(result.value.length)
}

const onClickRecommend = function () {
  const amount = {
    inputAmount: inputAmount.value,
    targetAmount: targetAmount.value
  }
  store.getSavingRecommendation(amount)
}



const isOpen = ref(false)
const type = ref('')  // Deposit or savings type
const inputmoney = ref('')  // Deposit amount
const intr_rate_type = ref('')  // Interest rate type
const save_trm = ref('')  // Deposit period
const intr_rate = ref('')  // Basic interest rate
const calinput = ref('')  // Total principal amount
const beforintr = ref('')  // Pre-tax interest
const taxintr = ref('')  // Tax amount
const mymoney = ref('')  // Expected amount

const calculator = function () {
  if (type.value === "예금") {
    if (intr_rate_type.value === "단리") {
      calinput.value = inputmoney.value * (save_trm.value / 12)
      beforintr.value = (calinput.value * (intr_rate.value / 100))
      taxintr.value = (beforintr.value * 0.154)
      mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
    } else {
      calinput.value = inputmoney.value * (save_trm.value / 12)
      beforintr.value = (inputmoney.value * ((1+(intr_rate.value/1200))*save_trm.value) - inputmoney.value)
      taxintr.value = (beforintr.value * 0.154)
      mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
    }
  } else { // 적금
    if (intr_rate_type.value === "단리") {
      calinput.value = inputmoney.value * save_trm.value
      beforintr.value = (inputmoney.value * (intr_rate.value / 1200) * (Math.round(((save_trm.value + 1) * save_trm.value) / 2)))
      taxintr.value = (beforintr.value * 0.154)
      mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
    } else {
      calinput.value = inputmoney.value * save_trm.value
      beforintr.value = ((inputmoney.value*((1+intr_rate.value/1200)*(save_trm.value+1))) - (inputmoney.value*(1+intr_rate.value/1200))) / (1+intr_rate.value/1200)
      taxintr.value = (beforintr.value * 0.154)
      mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
    }
  }
}

const toggleCalculator = function () {
  isOpen.value = !isOpen.value
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* Changed to 2 columns for wider items */
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
  height: auto; /* Adjusted to auto for flexible height */
  width: 100%; /* Ensure items take full width of their grid area */
}

.button_blue {
  background-color: rgb(59 130 153);
  color: white;
}

button.button_blue.my-2 {
  display: block;
  margin: 20px auto;
}
</style>
