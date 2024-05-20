<template>
  <main class="main-container">
    <div class="currency-converter">
      <CurrencyConverter />
    </div>
    <div class="popular-products">
      <PopularDepositList />
      <PopularSavingList />
    </div>
    <div class="today-luck">
      <TodayLuck />
    </div>
    <div class="news">
      <NaverNews />
    </div>
    <div class="boards">
      <div class="free-board">
        <FreeBoardList />
      </div>
      <div class="age-board">
        <AgeBoardList />
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
</script>

<style scoped>
.main-container {
  display: grid;
  grid-template-areas:
    "currency-converter popular-products login-box"
    "news news today-luck"
    "boards boards boards";
  grid-gap: 10px;
  padding: 20px;
}

.currency-converter {
  grid-area: currency-converter;
}

.popular-products {
  grid-area: popular-products;
  display: flex;
  justify-content: space-between;
}


.today-luck {
  grid-area: today-luck;
}

.news {
  grid-area: news;
}

.boards {
  grid-area: boards;
  display: flex;
  justify-content: space-between;
}

.free-board, .age-board {
  width: 48%;
}
</style>