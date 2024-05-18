<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">username : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password1">password : </label>
        <input type="password" v-model.trim="password1" id="password1">
      </div>
      <div>
        <label for="password2">password confirmation : </label>
        <input type="password" v-model.trim="password2" id="password2">
      </div>
      <div>
        <label for="email">email : </label>
        <input type="text" v-model.trim="email" id="email">
      </div>
      <div>
        <label for="nickname">nickname : </label>
        <input type="text" v-model.trim="nickname" id="nickname">
      </div>
      <div>
        <label for="birthdate">birthdate : </label>
        <input type="date" v-model.trim="birthdate" id="birthdate">
      </div>
      <div>
        <label for="gender">Gender : </label>
        <div>
          <input type="radio" id="male" value="M" v-model="gender">
          <label for="male">Male</label>
        </div>
        <div>
          <input type="radio" id="female" value="F" v-model="gender">
          <label for="female">Female</label>
        </div>
      </div>
      <div>
        <label for="address">address : </label>
        <input type="text" v-model.trim="address" id="address">
      </div>
      <div>
        <label for="asset">Asset : </label>
        <input type="text" v-model.trim="asset" id="asset">
      </div>
      <div>
        <label for="salary">Salary : </label>
        <input type="text" v-model.trim="salary" id="salary">
      </div>
      <div>
        <label for="interest_industry">interest_industry : </label>
        <input type="text" v-model.trim="interest_industry" id="interest_industry">
      </div>
      <input type="submit">
    </form>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { userCheckStore } from '@/stores/usercheck.js'

const username = ref(null) 
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const nickname = ref(null)
const birthdate = ref(null)
const gender = ref(null)
const address = ref(null)
const asset = ref(null)
const salary = ref(null)
const interest_industry = ref(null)
const store = userCheckStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    nickname: nickname.value,
    birthday: birthdate.value,
    gender: gender.value,
    address: address.value,
    asset: asset.value || 0,
    salary: salary.value || 0,
    interest_industry: interest_industry.value
  }
  store.signUp(payload)
}

const handleFileUpload = function (event) {
  profile_img.value = event.target.files[0]
}

</script>

<style scoped>

</style>