<template>
  <div id="app">
    <header>
      <div class="header-top">
        <RouterLink :to="{ name: 'main' }">
          <img :src="`/assets/logo/small_logo.png`" alt="Logo" class="logo">
        </RouterLink>
        <nav v-if="!store.token" class="auth-nav">
          <RouterLink :to="{ name: 'login' }">로그인</RouterLink> |
        </nav>
        <nav v-else class="auth-nav">
          <p>{{ store.userId }}</p>
          <button @click="store.logOut">로그아웃</button>|
          <RouterLink :to="{ name: 'userprofile' }">마이페이지</RouterLink> |
        </nav>
      </div>
      <nav class="main-nav">
        <RouterLink :to="{ name: 'main' }">메인페이지</RouterLink> |
        <RouterLink :to="{ name: 'searchbank' }">근처 은행 찾기</RouterLink> |
        <RouterLink :to="{ name: 'freeboard' }">게시판</RouterLink> |
        <RouterLink :to="{ name: 'deposit' }">예금 상품</RouterLink> |
        <RouterLink :to="{ name: 'saving' }">적금 상품</RouterLink> |
        <RouterLink :to="{ name: 'job' }">일자리</RouterLink> |
      </nav>
    </header>

    <main>
      <RouterView />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from '@/components/Footer.vue'
import { userCheckStore } from '@/stores/usercheck.js'

const store = userCheckStore()

</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  /* background-color: rgb(238, 245, 255); */
}

header {
  /* background: #f8f9fa; */
  padding: 1rem;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.logo {
  height: 40px;
}

.main-nav {
  background: #e9ecef;
  padding: 1rem;
}

.auth-nav {
  display: flex;
  gap: 1rem;
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
</style>
