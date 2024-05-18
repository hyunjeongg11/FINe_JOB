<template>
  <div>
    <h2>환율 계산기</h2>
    <p>매매기준율로 계산됩니다.</p>
    <div class="container">
      <div class="row">
        <div class="col-10 my-1">
          <div class="source-input my-1 row">
            <label for="source-input" class="w-25 fs-5 col-4">FROM</label>
            <select id="source-input" v-model="from" class="form-select mx-1 col-6">
              <option value="AED">아랍에미리트 디르함</option>
              <option value="AUD">호주 달러</option>
              <option value="BHD">바레인 디나르</option>
              <option value="BND">브루나이 달러</option>
              <option value="CAD">캐나다 달러</option>
              <option value="CHF">스위스 프랑</option>
              <option value="CNH">중국 위안화</option>
              <option value="DKK">덴마크 크로네</option>
              <option value="EUR">유럽연합 유로</option>
              <option value="GBP">영국 파운드</option>
              <option value="HKD">홍콩 달러</option>
              <option value="IDR(100)">인도네시아 루피아</option>
              <option value="JPY(100)">일본 엔</option>
              <option value="KRW">한국 원</option>
              <option value="KWD">쿠웨이트 디나르</option>
              <option value="MYR">말레이시아 링깃</option>
              <option value="NOK">노르웨이 크로네</option>
              <option value="NZD">뉴질랜드 달러</option>
              <option value="SAR">사우디 리얄</option>
              <option value="SEK">스웨덴 크로나</option>
              <option value="SGD">싱가포르 달러</option>
              <option value="THB">태국 달러</option>
              <option value="USD">미국 달러</option>
            </select>
            <img v-if="from" :src="`/assets/flags/${from}.png`" alt="" class="col-2" style="width: 4rem; height: 2.5rem;">
          </div>
          <div class="source-output my-2 row">
            <label for="source-output" class="w-25 fs-5 col-3">TO</label>
            <select id="source-output" v-model="to" class="form-select mx-1 col-6">
              <option value="AED">아랍에미리트 디르함</option>
              <option value="AUD">호주 달러</option>
              <option value="BHD">바레인 디나르</option>
              <option value="BND">브루나이 달러</option>
              <option value="CAD">캐나다 달러</option>
              <option value="CHF">스위스 프랑</option>
              <option value="CNH">중국 위안화</option>
              <option value="DKK">덴마크 크로네</option>
              <option value="EUR">유럽연합 유로</option>
              <option value="GBP">영국 파운드</option>
              <option value="HKD">홍콩 달러</option>
              <option value="IDR(100)">인도네시아 루피아</option>
              <option value="JPY(100)">일본 엔</option>
              <option value="KRW">한국 원</option>
              <option value="KWD">쿠웨이트 디나르</option>
              <option value="MYR">말레이시아 링깃</option>
              <option value="NOK">노르웨이 크로네</option>
              <option value="NZD">뉴질랜드 달러</option>
              <option value="SAR">사우디 리얄</option>
              <option value="SEK">스웨덴 크로나</option>
              <option value="SGD">싱가포르 달러</option>
              <option value="THB">태국 달러</option>
              <option value="USD">미국 달러</option>
            </select>
            <img v-if="to" :src="`/assets/flags/${to}.png`" alt="" class="col-2" style="width: 4rem; height: 2.5rem;">
          </div>
        </div>
        <button @click="changeFromTo" class="btn col-2"><img style="width: 20px;" src="/assets/exchange.png" alt=""></button>
      </div>
    </div>
    <button @click="calculate" class="btn btn-calc">계산하기</button>
      <div class="d-flex flex-column my-3 text-center">
        <div class="row m-2">
          <input type="number" v-model="fromValue" id="source-input-value" placeholder="금액 입력" class="form-control col-8">
          <p class="fw-bold fs-5 col-4 my-auto">{{ from.includes('(100)') ? from.slice(0,3) : from }}</p>
        </div>
        <div class="row">
          <p class="fw-bold col-2 fs-5"> = </p>
          <p class="col-6 fs-5">{{ toValue }}</p>
          <p class="fw-bold fs-5 col-3">{{ to.includes('(100)') ? to.slice(0,3) : to }}</p>
        </div>
      </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, watch } from 'vue'
  import { useBoardStore } from '@/stores/board'
  import axios from 'axios'
  const store = useBoardStore()
  const currentDate = new Date()
  const searchDate = ref(currentDate.toISOString().slice(0,10))
  const from = ref('')
  const fromValue = ref('')
  const to = ref('')
  const toValue = ref('')
  const mod = ref(1)
  const baseURL = `${store.API_URL}/api/v1/exchange_rate/calculate/`
  const rate = ref('')
  const warningMsg = ref('')

  // from 이나 to에서 100 단위 환율인 인도네시아 루피아, 일본 엔 선택 시 => mod 값을 100으로 변경 / 다른 화폐는 모두 mod 값이 1
  watch([from, to], () => {
    fromValue.value = ''
    toValue.value = ''
    if (['IDR(100)', 'JPY(100)'].includes(from.value) | ['IDR(100)', 'JPY(100)'].includes(to.value)) {
        mod.value = 100
    } 
    else {
        mod.value = 1
    }
  })

  // from 에서 한국 원이 아닌 다른 화폐를 선택한 경우, to는 한국 원으로 바꿔줌
watch(from, (newVal, oldVal) => {
  if (newVal != 'KRW') {
      to.value = 'KRW'
  }
})


// to 에서 한국 원이 아닌 다른 화폐를 선택한 경우, from은 한국 원으로 바꿔줌
watch(to, (newVal, oldVal) => {
  if (newVal != 'KRW') {
      from.value = 'KRW'
  }
})


// fromValue에 변화가 있으면, toValue 초기화
watch(fromValue, (newVal, oldVal) => {
  toValue.value = ''
})

const calculate = function() {
const URL = `${baseURL}?searchDate=${searchDate.value}&from=${from.value}&to=${to.value}`
axios({
  method: 'get',
  url: URL
})
  .then(res => {
    console.log(res.data)
    const data = res.data
    const idx = data.findIndex(item => {
      if(to.value === 'KRW') {
        return item.cur_unit === from.value
      }
      else {
        return item.cur_unit === to.value
      }
    })
    rate.value = parseFloat(data[idx].deal_bas_r.replace(',','')) // 매매 기준율

    if (to.value === 'KRW') {
        toValue.value = ((fromValue.value * rate.value) / mod.value).toFixed(2)
    } else {
        toValue.value = ((fromValue.value / rate.value) * mod.value).toFixed(2)
    }

    if (searchDate.value != data[idx].search_date) {
        window.alert(`비영업일 또는 영업 시간 이전이므로 ${data[idx].search_date}의 환율으로 계산됩니다.`)
        warningMsg.value = `비영업일 또는 영업 시간 이전이므로 ${data[idx].search_date}의 환율으로 계산됩니다.`
    } else {
        warningMsg.value = ''
    }
  })
  .catch((error) => {
      console.log(error)
  })
}

const changeFromTo = () => {
  [from.value, to.value] = [to.value, from.value]
}
</script>

<style scoped>

</style>