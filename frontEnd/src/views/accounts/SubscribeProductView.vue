<template>
  <div class="container mt-5">
    <div class="main-content">
    <nav class="sidebar">
      <RouterLink :to="{ name: 'userprofile' }" class="link" active-class="active-link">내 프로필</RouterLink>
				<RouterLink :to="{ name: 'subscribeproduct' }" class="link" active-class="active-link">가입한 금융 상품</RouterLink>
				<RouterLink :to="{ name: 'boardrecord'}" class="link" active-class="active-link">작성한 게시글</RouterLink>
    </nav>
      <div class="detail-view">
        <h3 class="mb-3">가입한 예금 상품</h3>
        <ul class="list-group mb-5">
          <li v-for="(deposit, index) in products.deposit_list" :key="deposit.id" class="list-group-item"> 
            <span> {{ index + 1 }}. {{ deposit.kor_co_nm }} - {{ deposit.fin_prdt_nm }}</span>
            <button @click="goDetailDeposit(deposit.fin_prdt_cd, deposit.id)" class="btn btn-link p-0 ms-2">상세정보</button>
          </li>
        </ul>

        <h3 class="mb-3">가입한 적금 상품</h3>
        <ul class="list-group mb-5">
          <li v-for="(saving, index) in products.saving_list" :key="saving.id" class="list-group-item">
            <span>{{ index + 1 }}. {{ saving.kor_co_nm }} - {{ saving.fin_prdt_nm }}</span>
            <button @click="goDetailSaving(saving.fin_prdt_cd, saving.id)" class="btn btn-link p-0 ms-2">상세정보</button>
          </li>
        </ul>

        <h3 class="mb-3">가입한 상품 금리</h3>
        <canvas id="interest-chart"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck'
import { useRouter } from 'vue-router'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const router = useRouter()

const goDetailDeposit = function (bank, id) {
  router.push({ name: 'depositdetail', params: { fin_prdt_cd: bank, id: id } })
}

const goDetailSaving = function (bank, id) {
  router.push({ name: 'savingdetail', params: { fin_prdt_cd: bank, id: id } })
}

const store = userCheckStore()
const products = ref({
  deposit_list: [],
  saving_list: []
})

const colorPairs = [
  { 
    background: ['rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)'],
    border: ['rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)']
  },
  { 
    background: ['rgba(255, 159, 64, 0.2)', 'rgba(54, 162, 235, 0.2)'],
    border: ['rgba(255, 159, 64, 1)', 'rgba(54, 162, 235, 1)']
  }
]

const getLikeBankProducts = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/accounts/like_list/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      products.value = res.data
      renderChart()
    })
    .catch((err) => {
      console.log(err)
    })
}

const renderChart = () => {
  setTimeout(() => {
    const labels = []
    const interestRates = []
    const interestRates2 = []
    const backgroundColors = []
    const borderColors = []
    let colorIndex = 0

    const addData = (productList, type) => {
      productList.forEach(product => {
        const colorPair = colorPairs[colorIndex % colorPairs.length]
        product[`${type}_options`].forEach(option => {
          labels.push(`${product.fin_prdt_nm} (${option.intr_rate_type_nm})`)
          interestRates.push(option.intr_rate)
          interestRates2.push(option.intr_rate2)
          backgroundColors.push(colorPair.background[0])
          borderColors.push(colorPair.border[0])
          backgroundColors.push(colorPair.background[1])
          borderColors.push(colorPair.border[1])
        })
        colorIndex++
      })
    }

    addData(products.value.deposit_list, 'deposit')
    addData(products.value.saving_list, 'saving')

    const ctx = document.getElementById('interest-chart').getContext('2d')
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [
          {
            label: '저축 금리',
            data: interestRates,
            backgroundColor: backgroundColors.filter((_, i) => i % 2 === 0),
            borderColor: borderColors.filter((_, i) => i % 2 === 0),
            borderWidth: 1
          },
          {
            label: '최고 우대금리 금리',
            data: interestRates2,
            backgroundColor: backgroundColors.filter((_, i) => i % 2 === 1),
            borderColor: borderColors.filter((_, i) => i % 2 === 1),
            borderWidth: 1
          }
        ]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    })
  }, 500)
}

onMounted(() => {
  getLikeBankProducts()
})
</script>

<style scoped>
.container {
  max-width: 1500px;
  margin: auto;
}

.main-content {
  display: flex;
}

.sidebar {
  border: 1px solid black;
  padding: 20px;
	height: 60%;
  width: 250px;
  margin-right: 30px;
  border-radius: 5px;
}

.link {
  display: block;
  padding: 10px 0;
  color: black;
  text-decoration: none;
}

.active-link {
  font-weight: bold;
  text-decoration: underline;
}

.detail-view {
  flex: 1;
}

#interest-chart {
  margin-bottom: 50px;
}
</style>
