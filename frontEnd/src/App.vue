<template>
  <div id="app">
    <header>
      <div class="header-top">
        <nav v-if="!store.token" class="auth-nav">
          <button @click="goLogin" class="login-btn">
            로그인
          </button>
        </nav>
        <nav v-else class="auth-nav">
          <p class="nav-link dropdown-toggle username" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <img :src="`/assets/profile.png`" alt="profile" style="height: 35px; width: 35px; border-radius: 20px;">
            {{ store.userId }}님
          </p>
          <ul class="dropdown-menu">
            <li><RouterLink :to="{ name: 'userprofile' }" class="dropdown-item" href="#">마이페이지</RouterLink></li>
            <li><a @click="store.logOut" class="dropdown-item" href="#">로그아웃</a></li>
          </ul>
        </nav>
      </div>
      <nav class="navbar navbar-expand-lg main-nav">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-center" id="navbarNavDropdown">
            <ul class="navbar-nav">
              <li class="nav-item">
                <RouterLink :to="{ name: 'main' }">
                  <img :src="logoSrc" @mouseover="logoSrc = '/assets/logo/small_logo_hover.png'" @mouseout="logoSrc = '/assets/logo/small_logo.png'" alt="Logo" class="logo">
                </RouterLink>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  금융상품 FIN
                </a>
                <ul class="dropdown-menu">
                  <li><RouterLink :to="{ name: 'deposit' }" class="dropdown-item" href="#">예금 상품</RouterLink></li>
                  <li><RouterLink :to="{ name: 'saving' }" class="dropdown-item" href="#">적금 상품</RouterLink></li>
                </ul>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  일자리 JOB
                </a>
                <ul class="dropdown-menu">
                  <li><RouterLink :to="{ name: 'job' }" class="dropdown-item" href="#">일자리 목록</RouterLink></li>
                  <li><RouterLink :to="{ name: 'recommendjoblist'}" class="dropdown-item" href="#">추천 일자리</RouterLink></li>
                </ul>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  편의서비스
                </a>
                <ul class="dropdown-menu">
                  <li><RouterLink :to="{ name: 'searchbank' }" class="dropdown-item" href="#">주변 은행 찾기</RouterLink></li>
                  <li><RouterLink :to="{ name: 'currencyconverter' }" class="dropdown-item" href="#">환율 계산기</RouterLink></li>
                  <li><RouterLink :to="{ name: 'interestcalculator' }" class="dropdown-item" href="#">이자 계산기</RouterLink></li>
                </ul>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'freeboard' }" class="nav-link" aria-current="page">커뮤니티</RouterLink>
              </li>
            </ul>
            <form class="d-flex position-relative" role="search" @submit.prevent="performSearch">
              <input class="form-control me-2" type="search" placeholder="검색어" aria-label="Search" v-model="searchQuery" @focus="showSearchResults" @input="updateSearchResults" @blur="hideSearchResults">
              <button class="btn btn-outline-success" type="submit" :style="{ backgroundColor: 'rgb(59, 130, 153)', borderColor: 'rgb(59, 130, 153)', color: 'white' }">Search</button>
              <ul class="dropdown-menu search-results" :class="{ show: searchResultsVisible }">
                <li v-for="result in searchResults" :key="result.name">
                  <RouterLink :to="result.link" class="dropdown-item" @mousedown.prevent="navigateTo(result.link)">{{ result.name }}</RouterLink>
                </li>
              </ul>
            </form>
          </div>
        </div>
      </nav>
    </header>

    <main>
      <RouterView v-slot="{ Component, route }">
        <keep-alive include="DepositList">
          <component :is="Component" :key="route.path" />
        </keep-alive>
      </RouterView>
    </main>
    <Footer />
    <button @click="scrollToTop" class="scroll-to-top">
      <img :src="`/assets/up.png`" alt="맨 위로" class="up-icon">
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import Footer from '@/components/Footer.vue'
import { userCheckStore } from '@/stores/usercheck.js'

const store = userCheckStore()
const searchQuery = ref('')
const searchResults = ref([])
const searchResultsVisible = ref(false)
const logoSrc = ref('/assets/logo/small_logo.png')
const router = useRouter()

const goLogin = function () {
  router.push({ name: 'login'})
}

const navigationItems = [
  { name: '예금 상품', link: { name: 'deposit' } },
  { name: '적금 상품', link: { name: 'saving' } },
  { name: '일자리 목록', link: { name: 'job' } },
  { name: '추천 일자리', link: { name: 'recommendjoblist' } },
  { name: '주변 은행 찾기', link: { name: 'searchbank' } },
  { name: '환율 계산기', link: { name: 'currencyconverter' } },
  { name: '커뮤니티', link: { name: 'freeboard' } },
  { name: '이자 계산기', link: { name: 'interestcalculator' } }
]

const updateSearchResults = () => {
  searchResults.value = navigationItems.filter(item =>
    item.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
  searchResultsVisible.value = true
}

const performSearch = () => {
  if (searchResults.value.length) {
    router.push(searchResults.value[0].link)
    searchQuery.value = ''
    searchResults.value = []
    searchResultsVisible.value = false
  }
}

const showSearchResults = () => {
  if (searchResults.value.length > 0) {
    searchResultsVisible.value = true
  }
}

const hideSearchResults = () => {
  setTimeout(() => {
    searchResultsVisible.value = false
  }, 200)
}

const navigateTo = (link) => {
  router.push(link)
  searchQuery.value = ''
  searchResults.value = []
  searchResultsVisible.value = false
}

onMounted(() => {
  const dropdowns = document.querySelectorAll('.nav-item.dropdown');

  dropdowns.forEach(dropdown => {
    dropdown.addEventListener('mouseover', () => {
      const menu = dropdown.querySelector('.dropdown-menu');
      if (menu) {
        menu.classList.add('show');
      }
    });

    dropdown.addEventListener('mouseout', () => {
      const menu = dropdown.querySelector('.dropdown-menu');
      if (menu) {
        menu.classList.remove('show');
      }
    });
  });
});

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: 'hanbit';
}

header {
  padding: 1rem;
}

.header-top {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: rem;
  margin-right: 8%; 
}

.login-btn {
  padding: 3px 10px;
  background-color: rgb(255, 255, 255);
  border-color: #33333346;
  border-radius: 5px;
}


.login-btn:hover {
  background-color: rgba(184, 184, 184, 0.5);
  border-color: #33333346;
}

.logo {
  height: 60px;
  margin-right: 40px;
}

.auth-nav {
  display: flex;
  gap: 1rem;
}

.username {
  cursor: pointer;
  font-size: 18px;
}

.main-nav {
  width: 100%;
  background-color: #fff;
  border-bottom: 2px solid rgb(59, 130, 153);
  padding: 0 7%;
  margin-bottom: 20px;
}

.navbar-nav {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

.nav-item {
  flex: 1;
  text-align: center;
  font-size: 20px;
  position: relative;
}

.dropdown-menu {
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
}

.dropdown-item:hover {
  background-color: rgb(219, 236, 241);
}

.search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 1000;
}

main {
  flex: 1;
}

footer {
  background-color: #333;
  color: white;
  padding: 20px 0;
  text-align: center;
}

.scroll-to-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.scroll-to-top .up-icon {
  width: 50px;
  height: 50px;
}

@font-face {
  font-family: 'pretty';
  src: url('../assets/fonts/Cafe24Oneprettynight-v2.0.ttf') format('truetype');
}

@font-face {
  font-family: 'magic';
  src: url('../assets/fonts/Cafe24Supermagic-Regular-v1.0.ttf') format('truetype');
}

@font-face {
  font-family: 'hanbit';
  src: url('../assets/fonts/KCC-Hanbit.ttf') format('truetype');
}

body {
  font-family: 'pretty', 'magic', 'hanbit', sans-serif;
}
</style>