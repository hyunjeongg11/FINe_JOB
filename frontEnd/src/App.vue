
<template>
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink :to="{name: 'searchbank'}">근처 은행 찾기</RouterLink>
      </nav>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>
