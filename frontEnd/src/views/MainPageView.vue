<template>
  <main class="main-container">
    <div class="image-carousel">
      <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="/assets/carousel/1.jpg" class="d-block" alt="Image 1">
          </div>
          <div class="carousel-item">
            <img src="/assets/carousel/2.jpg" class="d-block" alt="Image 2">
          </div>
          <div class="carousel-item">
            <img src="/assets/carousel/3.jpg" class="d-block" alt="Image 3">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
    <div class="icons">
      <div class="login-area">
        <div class="login-form">로그인</div>
      </div>
      <div class="icons-area">
        <div class="icon-item icon-top-left">
          <img src="/assets/carousel/1.jpg" alt="금융">
          <p>금융</p>
        </div>
        <div class="icon-item icon-top-right">
          <img src="/assets/carousel/2.jpg" alt="환율">
          <p>환율</p>
        </div>
        <div class="icon-item icon-bottom-left">
          <img src="/assets/carousel/3.jpg" alt="일자리">
          <p>일자리</p>
        </div>
        <div class="icon-item icon-bottom-right">
          <img src="/assets/carousel/4.jpg" alt="은행 지도">
          <p>은행 지도</p>
        </div>
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
import TodayLuck from '@/components/TodayLuck.vue'
import NaverNews from '@/components/NaverNews.vue'
</script>

<style scoped>
/* 전체 스타일 */
* {
  box-sizing: border-box;
}

.main-container {
  display: grid;
  grid-template-areas:
    "image-carousel icons"
    "news today-luck";
  grid-template-columns: 2fr 1fr;
  grid-template-rows: auto auto;
  gap: 30px;
  width: 84%;
  margin: auto;
}

/* 이미지 카루셀 스타일 */
.image-carousel {
  grid-area: image-carousel;
  width: 100%;
  height: 550px;
  overflow: hidden;
}

.image-carousel img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 아이콘 영역 스타일 */
.icons {
  grid-area: icons;
  display: flex;
  flex-direction: column;
  margin-bottom: 5px;
}

.login-area {
  height: 35%;
  margin-bottom: 5%;
  background-color: skyblue;
  justify-content: center; /* 수평 가운데 정렬 */
  align-items: center; /* 수직 가운데 정렬 */
}

.icons-area {
  height: 60%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 5px;
  justify-items: center;
  align-items: center;
}

.icon-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.icon-item img {
  width: 100px;
  height: 100px;
  margin: 3px;
  border-radius: 50%;
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
</style>