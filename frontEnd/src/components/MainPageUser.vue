<template>
  <div>
    <div v-if="userStore.token">
      <img :src="`/assets/profile/profile${userStore.profile_img_index}.png`" alt="profile" >
      <span class="login-main-text">&nbsp;&nbsp;{{ userStore.userId }} 님 안녕하세요!</span>
      <!-- <p> {{ userStore.email }}</p> -->
      <div class="detail-page">
        <RouterLink :to="{name: 'subscribeproduct'}" class="mypage">가입한상품&nbsp;</RouterLink> | 
        <RouterLink :to="{ name: 'userprofile'}"  class="mypage">&nbsp;마이페이지</RouterLink>
      </div>
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

console.log(userStore)
</script>

<style scoped>
.btn-login-main {
  display: flex;
  justify-content: center;
}

.btn-login {
  width: 100%;
  padding: 8px;
  background-color: rgb(255, 255, 255);
  border-color: #33333346;
  border-radius: 5px;

  font-size: 18px;
}

.login-main-text{
  text-align: center;
  font-size: 18px;
}

.detail-page {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  cursor: pointer;
  flex: 1;
  font-size: 18px;
  color: black;
}

.mypage {
  color: black;
  text-decoration: none;
  display: flex;
  justify-content: center;
  align-items: center;
  /* margin-bottom: 10px; */
  cursor: pointer;
  flex: 1;
  font-weight: bold;
}

.mypage:hover {
  color: #109094;
}

img {
  height: 50px; 
  width: 50px; 
  border-radius: 20px; 
  margin-bottom: 10px; 
  border: rgb(190, 190, 190) 1px solid;
}
</style>