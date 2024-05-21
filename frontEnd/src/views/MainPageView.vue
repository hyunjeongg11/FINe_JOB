<template>
  <main class="main-container">
    <div class="popular-deposit">
      <PopularDepositList />
    </div>
    <div class="popular-saving">
      <PopularSavingList />
    </div>
    <div class="recommend-job">
      <RecommendJobList />
    </div>
    <div class="news">
      <NaverNews />
    </div>
    <div class="other-feature">
      <div class="currency-converter">
        <CurrencyConverter />
      </div>
      <div class="today-luck">
        <TodayLuck />
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
/* Existing styles */
* {
  box-sizing: border-box;
}

.main-container {
  display: grid;
  grid-template-areas:
    "popular-deposit popular-saving recommend-job"
    "news news other-feature";
  grid-template-columns: 1fr 1fr 1fr;
  width: 84%;
  margin-left: 5%;
}

.main-container > div {
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  margin: 4%;
  padding: 3%;
}

.popular-deposit {
  grid-area: popular-deposit;
}

.popular-saving {
  grid-area: popular-saving;
}

.recommend-job {
  grid-area: recommend-job;
}

.other-feature {
  grid-area: other-feature;
  display: flex;
  width: 175%;
  height: 60%;
  /* padding-left: 8%; Use padding instead of margin */
  margin-top: 10%; /* Add margin-top to create space */
  transform: translateX(-250px);
  gap: 5%;
}

/* Resetting margin for news section */
.news {
  width: 150%;
  margin-top: 0; /* Reset margin-top */
  transform: translateX(-50px); 
}

.currency-converter, .today-luck {
  flex: 1;
}

</style>