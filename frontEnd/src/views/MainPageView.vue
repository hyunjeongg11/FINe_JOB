<template>
  <main class="main-container">
    <div class="image-carousel">
      <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <RouterLink :to="{ name : 'deposit'}">
            <div class="carousel-item">
              <img src="/assets/main/main1.png" class="d-block" alt="Image 1">
            </div>
          </RouterLink>
          <RouterLink :to="{ name : 'deposit'}">
            <div class="carousel-item active">
              <img src="/assets/main/main2.png" class="d-block" alt="Image 1">
            </div>
          </RouterLink>
          <RouterLink :to="{ name : 'saving'}">
            <div class="carousel-item">
              <img src="/assets/main/main3.png" class="d-block" alt="Image 2">
            </div>
          </RouterLink>
          <RouterLink :to="{ name : 'searchbank'}">
            <div class="carousel-item">
              <img src="/assets/main/main4.png" class="d-block" alt="Image 3">
            </div>
          </RouterLink>
          <RouterLink :to="{ name : 'currencyconverter'}">
            <div class="carousel-item">
              <img src="/assets/main/main5.png" class="d-block" alt="Image 4">
            </div>
          </RouterLink>
          <RouterLink :to="{ name : 'freeboard'}">
            <div class="carousel-item">
              <img src="/assets/main/main6.png" class="d-block" alt="Image 5">
            </div>
          </RouterLink>
          <RouterLink :to="{ name : 'main'}">
            <div class="carousel-item">
              <img src="/assets/main/main7.png" class="d-block" alt="Image 6">
            </div>
          </RouterLink>
          <RouterLink :to="{ name : 'intro'}">
            <div class="carousel-item">
              <img src="/assets/main/main8.png" class="d-block" alt="Image 7">
            </div>
          </RouterLink>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
        </button>
      </div>
    </div>
    <div class="icons">
      <div class="login-area">
        <div>
          <MainPageUser />
        </div>
      </div>
      <div class="icons-area">
        <RouterLink to="/deposit" class="icon-item icon-top-left" @mouseover="changeIconToColor($event, 'fin')" @mouseout="changeIconToBlackAndWhite($event, 'fin')">
          <img :src="iconPaths.금융" alt="금융">
          <p class="p-tag">금융</p>
        </RouterLink>
        <RouterLink to="/currencyconverter" class="icon-item icon-top-right" @mouseover="changeIconToColor($event, 'exchange')" @mouseout="changeIconToBlackAndWhite($event, 'exchange')">
          <img :src="iconPaths.환율" alt="환율">
          <p class="p-tag">환율</p>
        </RouterLink>
        <RouterLink to="/job" class="icon-item icon-bottom-left" @mouseover="changeIconToColor($event, 'job')" @mouseout="changeIconToBlackAndWhite($event, 'job')">
          <img :src="iconPaths.일자리" alt="일자리">
          <p class="p-tag">일자리</p>
        </RouterLink>
        <RouterLink to="/searchbank" class="icon-item icon-bottom-right" @mouseover="changeIconToColor($event, 'map')" @mouseout="changeIconToBlackAndWhite($event, 'map')">
          <img :src="iconPaths.은행지도" alt="지도">
          <p class="p-tag">은행 지도</p>
        </RouterLink>
      </div>
    </div>
    <div class="news">
      <NaverNews />
    </div>
    <div class="today-luck">
      <TodayLuck />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import TodayLuck from '@/components/TodayLuck.vue'
import NaverNews from '@/components/NaverNews.vue'
import MainPageUser from '@/components/MainPageUser.vue'
import { RouterLink } from 'vue-router'

const iconPaths = ref({
  금융: '/assets/icons/fin_black.png',
  환율: '/assets/icons/exchange_black.png',
  일자리: '/assets/icons/job_black.png',
  은행지도: '/assets/icons/map_black.png',
})

const changeIconToColor = (event, iconName) => {
  event.target.src = `/assets/icons/${iconName}_color.png`
}

const changeIconToBlackAndWhite = (event, iconName) => {
  event.target.src = `/assets/icons/${iconName}_black.png`
}
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.main-container {
  display: grid;
  grid-template-areas:
    "image-carousel icons"
    "news today-luck";
  grid-template-columns: 3fr 1fr;
  grid-template-rows: auto auto;
  gap: 30px;
  width: 84%;
  margin: auto;
  border-color: darkgray 2px solid;
}

.image-carousel {
  grid-area: image-carousel;
  width: 100%;
  height: 650px;
  overflow: hidden;
}

.image-carousel img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.icons {
  grid-area: icons;
  display: flex;
  flex-direction: column;
  margin-bottom: 5px;
}

.login-area {
  height: 35%;
  margin-bottom: 5%;
  background-color: rgb(219, 236, 241);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border-color: rgb(88, 81, 81) 2px solid;
}

.icons-area {
  height: 60%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  justify-items: center;
  align-items: center;
}

.icon-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* padding: 10px; */
  transition: transform 0.3s ease;
}

.icon-item:hover {
  transform: translateY(-4px); 
}

.icon-item img {
  width: 115px;
  height: 115px;
  margin: 3px;
  padding: 20px;
  border-radius: 20%;
  border: 2px solid black;
}

/* 나머지 아이콘들의 위치 지정 */
.icon-top-left {
  grid-column: 1;
  grid-row: 1;
}

.icon-top-right {
  grid-column: 2;
  grid-row: 1;
}

.icon-bottom-left {
  grid-column: 1;
  grid-row: 2;
}

.icon-bottom-right {
  grid-column: 2;
  grid-row: 2;
}

.news {
  grid-area: news;
}

.today-luck {
  grid-area: today-luck;
}

.main-container > div {
  padding: 15px;
}

.login {
  background-color: aqua;
}

.icon-item .p-tag {
  color: black;
}
</style>
