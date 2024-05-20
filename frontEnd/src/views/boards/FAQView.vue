<template>
  <div>
    <button @click="goBack" class="back-button">뒤로 가기</button>
    <nav>
      <RouterLink :to="{name: 'freeboard'}">자유게시판</RouterLink> | 
      <RouterLink :to="{name: 'ageboard'}">연령별 게시판</RouterLink> | 
      <RouterLink :to="{name: 'FAQ'}">FAQ</RouterLink>
    </nav>
    <div class="container">
      <h1>FAQ 페이지</h1>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

function goBack() {
    router.back();
}
</script>

<style scoped>
  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  .container {
    max-width: 1500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  nav {
    text-align: center;
    margin-bottom: 20px;
  }

  .back-button {
    margin: 10px 10px;
    padding: 5px 10px;
    font-size: 16px;
    color: black;
    /* background-color: #555; */
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.back-button:hover {
    background-color: rgb(165, 165, 165);
}
</style>