
<template>
      <nav>
        <RouterLink :to="{name : 'main'}">Home</RouterLink> | 
        <RouterLink :to="{name: 'searchbank'}">근처 은행 찾기</RouterLink> | 
        <RouterLink :to="{name: 'board'}">커뮤니티</RouterLink> | 
        <RouterLink :to="{name: 'deposit'}">예금 상품</RouterLink> | 
        <RouterLink :to="{name: 'saving'}">적금 상품</RouterLink> | 
        <RouterLink :to="{name: 'job'}">일자리</RouterLink> | 
      </nav>

      <nav>
        <RouterLink :to="{name : 'login'}">로그인</RouterLink> | 
        <RouterLink :to="{name :'signup'}">회원가입</RouterLink> | 
        <RouterLink :to="{name :'userprofile'}">마이페이지</RouterLink> |
      </nav>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>
