<template>
  <div class="calculator-container">
    <h3>간편 예적금 이자 계산기</h3>
    <div class="form-group">
      <label>저축 방식 :</label>
      <select v-model="type" class="form-control">
        <option disabled value="">유형을 선택해 주세요</option>
        <option>예금</option>
        <option>적금</option>
      </select>
    </div>
    <div class="form-group">
      <label for="inputmoney">예치 금액 :</label>
      <div class="input-group">
        <input type="number" id="inputmoney" v-model="inputmoney" :min="0" class="form-control">
        <span class="input-group-addon">원</span>
      </div>
    </div>
    <div class="form-group">
      <label>이자 방식 :</label>
      <select v-model="intr_rate_type" class="form-control">
        <option disabled value="">유형을 선택해 주세요</option>
        <option>단리</option>
        <option>복리</option>
      </select>
    </div>
    <div class="form-group">
      <label for="save_trm">예금 기간 :</label>
      <div class="input-group">
        <input type="number" id="save_trm" v-model="save_trm" :min="0" class="form-control">
        <span class="input-group-addon">(개월)</span>
      </div>
    </div>
    <div class="form-group">
      <label for="intr_rate">연이자율 :</label>
      <div class="input-group">
        <input type="number" id="intr_rate" v-model="intr_rate" :min="0" class="form-control">
        <span class="input-group-addon">(%)</span>
      </div>
    </div>
    <div class="results">
      <p><strong>원금 합계 :</strong> {{ calinputFormatted }} 원</p>
      <p><strong>세전이자 :</strong> {{ beforintrFormatted }} 원</p>
      <p><strong>이자과세 :</strong> -{{ taxintrFormatted }} 원</p>
      <p><strong>세후 수령액 :</strong> {{ mymoneyFormatted }} 원</p>
    </div>
    <button @click.prevent="calculator" class="btn button_blue">계산</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const type = ref('')  // 예금, 적금 형식
const inputmoney = ref(0)  // 예치 금액
const intr_rate_type = ref('')  // 이자 유형
const save_trm = ref(0)  // 예금 기간
const intr_rate = ref(0)  // 연이자율
const calinput = ref(0)  // 원금 총액
const beforintr = ref(0)  // 세전 이자
const taxintr = ref(0)  // 과세 금액
const mymoney = ref(0)  // 세후 수령액

const calculator = () => {
  if (type.value === "예금") {
    calinput.value = inputmoney.value
    if (intr_rate_type.value === "단리") {
      beforintr.value = Math.floor(inputmoney.value * (intr_rate.value / 100) * (save_trm.value / 12))
    } else {
      beforintr.value = Math.floor(inputmoney.value * Math.pow((1 + intr_rate.value / 100), (save_trm.value / 12)) - inputmoney.value)
    }
  } else { // 적금
    calinput.value = Math.floor(inputmoney.value * save_trm.value)
    if (intr_rate_type.value === "단리") {
      beforintr.value = Math.floor(inputmoney.value * (intr_rate.value / 100) * ((save_trm.value + 1) * save_trm.value / 24))
    } else {
      beforintr.value = Math.floor(inputmoney.value * (save_trm.value * (save_trm.value + 1) / 2) * (intr_rate.value / 100 / 12))
    }
  }
  taxintr.value = Math.floor(beforintr.value * 0.154)
  mymoney.value = Math.floor(calinput.value + beforintr.value - taxintr.value)
}

const calinputFormatted = computed(() => calinput.value.toLocaleString('ko-KR'))
const beforintrFormatted = computed(() => beforintr.value.toLocaleString('ko-KR'))
const taxintrFormatted = computed(() => taxintr.value.toLocaleString('ko-KR'))
const mymoneyFormatted = computed(() => mymoney.value.toLocaleString('ko-KR'))
</script>

<style scoped>
.calculator-container {
  background-color: rgb(219, 236, 241);
  padding: 20px;
  border-radius: 10px;
  max-width: 600px;
  margin: 0 auto;
  /* text-align: center; */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

.input-group {
  display: flex;
  align-items: center;
}

.form-control {
  flex: 1;
  padding: 10px;
  margin-top: 5px;
  margin-bottom: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.input-group-addon {
  padding: 10px;
  margin-left: 5px;
  background-color: #e9ecef;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.results {
  margin-top: 20px;
  text-align: left;
}

.button_blue {
  background-color: rgb(59 130 153);
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

.button_blue:hover {
  background-color: rgb(45, 100, 120);
}
</style>
