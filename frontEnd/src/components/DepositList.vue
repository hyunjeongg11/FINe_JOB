<template>
  <div class="container">
    <h1 class="mb-4">예금 상품</h1>
    <h2 class="mb-3">검색하기</h2>
    <h4 class="mb-3">검색 조건을 입력하세요</h4>
    <hr>
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
            <option>6</option>
            <option>12</option>
            <option>24</option>
            <option>36</option>
          </select>
        </div>
        <div class="col-md-2 mt-4 d-flex justify-content-center">
          <input type="submit" value="검색" class="btn button_blue">
        </div>
      </div>
    </form>
  </div>
  <div class="container">
    <button @click="toggleCalculator" class="btn button_blue my-2">{{ isOpen ? '이자계산기 닫기' : '이자계산기 열기' }}></button>
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
      <h2>예금 리스트</h2>
      <div>
        <div class="grid-container" v-if="result.length > 0">
          <DepositListItem v-for="deposit in result" :key="deposit.id" :deposit="deposit" class="grid-item" />
        </div>
        <div v-else>
          <p class="text-center">조건에 맞는 결과가 없습니다.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import DepositListItem from '@/components/DepositListItem.vue'

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


// 기간만 필터링
const termFilter = function (term) {
  const result = []
  for (const product of store.depositList) {
    const saving_options = []
    console.log(product)
    for (const option of product.deposit_options) {
      if (option.save_trm == term) {
        saving_options.push(option)
      }
    }
    if (saving_options.length != 0) {
      product.saving_options = saving_options
      // console.log('상품:', product)
      result.push(product)
    }
  }
  return result
}


// 기간과 은행을 같이 필터링
const termBankFilter = function (bank, term) {
  const result = []
  for (const product of store.depositList) {
    if (product.kor_co_nm === bank) {
      const saving_options = []
      for (const option of product.deposit_options) {
        if (option.save_trm == term) {
          saving_options.push(option)
        }
      }
      if (saving_options.length != 0) {
        product.deposit_options = saving_options
        // console.log('상품:', product)
        result.push(product)
      }
    }
  }
  return result
}


const result = ref([])
const onClickFilter = function () {
  if (bank.value === '전체 은행' && term.value === '전체 기간') {
    result.value = store.depositList

  } else if (bank.value === '전체 은행' && term.value !== '전체 기간') {
    result.value = termFilter(term.value)

  } else if (bank.value !== '전체 은행' && term.value === '전체 기간') {

    // 은행만 필터링
    result.value = store.depositList.filter((item) => {
      if (item.kor_co_nm === bank.value) {
        return item
      }
    })
    console.log(result.value)
  } else {
    result.value = termBankFilter(bank.value, term.value)
  }
  console.log(result.value)
}

const isOpen = ref(false)
const type = ref('')  //예,적금 형식
const inputmoney = ref('')  // 예치 금액
const intr_rate_type = ref('')  // 예치 유형
const save_trm = ref('')  // 예금 기간
const intr_rate = ref('')  // 기본금리
const calinput = ref('')  // 원금 총액
const beforintr = ref('')  // 세전 이율
const taxintr = ref('')  // 과세 금액
const mymoney = ref('')  // 예상 금액

const calculator = function () {
  if (type.value === "예금") {
    if (intr_rate_type.value === "단리") {
      calinput.value = inputmoney.value * (save_trm.value / 12)
      beforintr.value = (calinput.value * (intr_rate.value / 100))
      taxintr.value = (beforintr.value * 0.154)
      mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
    }
    else {
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
    }
    else {
      calinput.value = inputmoney.value * save_trm.value
      beforintr.value = ((inputmoney.value*((1+intr_rate.value/1200)(save_trm.value+1))) - (inputmoney.value*(1+intr_rate.value/1200))) / (1+intr_rate.value/1200)
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
