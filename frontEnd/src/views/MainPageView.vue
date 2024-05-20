<template>
  <main class="main-container">
    <div class="currency-converter">
      <CurrencyConverter />
    </div>
    <div class="popular-products">
      <div class="popular-deposit">
        <PopularDepositList />
      </div>
      <div class="popular-saving">
        <PopularSavingList />
      </div>
    </div>
    <div class="news">
      <NaverNews />
    </div>
    <div class="today-info">
      <div class="today-luck">
        <TodayLuck />
      </div>
      <div class="recommend-job">
        <RecommendJobList />
      </div>
    </div>
  </main>
</template>

<script setup>
import PopularDepositList from '@/components/PopularDepositList.vue'
import PopularSavingList from '@/components/PopularSavingList.vue'
import TodayLuck from '@/components/TodayLuck.vue'
import NaverNews from '@/components/NaverNews.vue'
import FreeBoardList from '@/components/FreeBoardList.vue'
import AgeBoardList from '@/components/AgeBoardList.vue'
import CurrencyConverter from '@/components/CurrencyConverter.vue'
import RecommendJobList from '@/components/RecommendJobList.vue'
</script>

<style scoped>
.main-container {
  display: grid;
  grid-template-areas:
    "currency-converter popular-products"
    "news today-info";
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.main-container > div {
  /* border: 1px solid black; */
  padding: 10px;
}

.currency-converter {
  grid-area: currency-converter;
  width: 85%;
  margin-left: 10%;
}

.popular-products {
  grid-area: popular-products;
  display: flex;
  justify-content: space-around;
  width: 90%;
}

.news {
  grid-area: news;
  width: 85%;
  margin-left: 10%;
}

.today-info {
  grid-area: today-info;
  width: 90%;
  justify-content: space-around;
}

.today-info > div {
  border: 1px solid black;
}


.popular-products > div {
  border: 1px solid black;
}


.today-luck {
  height: 30%;
  margin-bottom: 5%;
}

.recommend-job {
  height: 65%;
}

.popular-saving, .popular-deposit {
  width: 48%;
}
</style>
