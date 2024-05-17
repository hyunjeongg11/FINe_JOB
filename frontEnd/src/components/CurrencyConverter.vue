<template>
    <div>
        <h2>환율 계산기</h2>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import axios from 'axios'
    const currentDate = new Date()
    const searchDate = ref(currentDate.toISOString().slice(0,10))
    const from = ref('')
    const to = ref('')
    const baseURL = 'http://localhost:8000/api/v1/exchange_rate/calculate/'
    const calculate = function() {
    const URL = `${baseURL}?searchDate=${searchDate.value}&from=${from.value}&to=${to.value}`
    axios({
        method: 'get',
        url: URL
        })
        .then(res => {
            console.log(res)
            // const data = response.data
            // const idx = data.findIndex((item) => { 
            //     if (to.value === 'KRW') {
            //         return item.cur_unit === from.value
            //     } else {
            //         return item.cur_unit === to.value
            //     }
            // })
            // rate.value = parseFloat(data[idx].deal_bas_r.replace(',','')) // 매매 기준율

            // // console.log('요청일:', searchDate.value, '환율 기준일:', data[idx].search_date)
            // // console.log('rate', rate.value)
            // // console.log('mod', mod.value)
            // if (to.value === 'KRW') {
            //     toValue.value = ((fromValue.value * rate.value) / mod.value).toFixed(2)
            // } else {
            //     toValue.value = ((fromValue.value / rate.value) * mod.value).toFixed(2)
            // }

            // if (searchDate.value != data[idx].search_date) {
            //     window.alert(`비영업일 또는 영업 시간 이전이므로 ${data[idx].search_date}의 환율으로 계산됩니다.`)
            //     warningMsg.value = `비영업일 또는 영업 시간 이전이므로 ${data[idx].search_date}의 환율으로 계산됩니다.`
            // } else {
            //     warningMsg.value = ''
            // }
        })
        .catch((error) => {
            console.log(error)
        })

    calculate() 
    
}

</script>

<style scoped>

</style>