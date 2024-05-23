<template>
  <div>
    <div v-if="userStore.token">
      <p class="login-main-text">{{ userStore.userId }}님 환영합니다!</p>
      <div class="btn-login-main">
        <button class="btn-login" @click="userStore.logOut">로그아웃</button>
      </div>
    </div>
    <div v-else>
      <p class="login-main-text">FINe JOB을 더 편리하게 이용하세요!</p>
      <div class="btn-login-main">
        <button class="btn-login" @click="goLogin">로그인</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { userCheckStore } from '@/stores/usercheck'
import { RouterLink, RouterView, useRouter } from 'vue-router'
const userStore = userCheckStore()
const router = useRouter()

const goLogin = function () {
  router.push({ name: 'login'})
}
</script>

<style scoped>
.btn-login-main {
  display: flex;
  justify-content: center;
}

.btn-login {
  width: 100%;
  padding: 13px;
  background-color: rgb(255, 255, 255);
  border-color: #33333346;
  border-radius: 5px;

  font-size: 18px;
}

.login-main-text{
  text-align: center;
  font-size: 18px;
}
</style>