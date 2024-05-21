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
import CurrencyConverter from '@/components/CurrencyConverter.vue'
import RecommendJobList from '@/components/RecommendJobList.vue'
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.main-container {
  display: grid;
  grid-template-areas:
    "currency-converter popular-products"
    "news today-info";
  grid-template-columns: 1fr 1fr;
  gap: 20px; /* 간격을 늘립니다. */
}

.main-container > div {
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.currency-converter {
  grid-area: currency-converter;
  width: 60%;
  margin-left: 22.5%;
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
  margin-bottom: 5%;
  background-color: rgb(219, 236, 241);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 10px;
}

.popular-products > div {
  border: 1px solid black;
}

.today-luck {
  height: 38%;
}

.recommend-job {
  height: 60%;
}

.popular-saving, .popular-deposit {
  width: 48%;
}
</style>
