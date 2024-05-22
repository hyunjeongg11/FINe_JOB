<template>
  <div class="outer-box">
    <div class="d-flex justify-content-center container">
      <div class="col-md-6 login-outer position-relative">
        <h1 class="mb-4 login-title">로그인</h1>
        <div class="login-content">
          <form @submit.prevent="logIn">
            <div class="mb-3">
              <label for="username" class="form-label">아이디</label>
              <input type="text" class="form-control" v-model.trim="username"><br>
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">비밀번호</label>
              <input type="password" class="form-control" v-model.trim="password"><br>
            </div>
            <div class="text-center">
              <input type="submit" class="login-btn" value="로그인">
            </div>
          </form>
        </div>
        <RouterLink class="router-link signup-link" :to="{name : 'signup'}">회원가입</RouterLink>
      </div>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { userCheckStore } from '@/stores/usercheck.js'

const store = userCheckStore()

const username = ref(null)
const password = ref(null)

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.ms-3 {
  margin-left: 1rem;
}

.outer-box {
  margin-top: 2rem;
}

.login-title {
  text-align: center;
}

.login-outer {
  padding: 1.5rem;
  border: 1px solid #e9ecef;
  background-color: rgb(236, 245, 248);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: relative;
}

.signup-link {
  position: absolute;
  bottom: 2rem;
  right: 2rem;
  color: rgba(0, 0, 0, 0.418);
  text-decoration: none; 
  margin-right: 3%;
}


.signup-link:hover {
  color: rgb(0, 0, 0);
}

.login-content {
  background-color: white;
  padding: 1rem;
  border-radius: 10px;
}

.login-btn {
  width: 100px;
  margin: 10px auto;
  background-color: rgb(180, 212, 255);
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}

.login-btn:hover {
  background-color: rgb(104, 142, 206);
}
</style>
