<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-4">
        <h1 class="mb-4">Login</h1>
        <form @submit.prevent="logIn">
          <div class="mb-3">
            <label for="username" class="form-label">아이디:</label>
            <input type="text" class="form-control" v-model.trim="username"><br>
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">비밀번호:</label>
            <input type="password" class="form-control" v-model.trim="password"><br>
          </div>
          <div class="text-center">
            <input type="submit" value="logIn">
          </div>
        </form>
      </div>
    </div>
    <RouterLink :to="{name : 'signup'}">회원가입</RouterLink> 
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

</style>