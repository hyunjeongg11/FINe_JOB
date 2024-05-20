<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-5">
        <h1 class="mb-4">회원가입</h1>
        <form @submit.prevent="signUp">
          <div class="mb-2">
            <label for="username" class="form-label">아이디</label>
            <input type="text" class="form-control" v-model.trim="username" id="username">
          </div>
          <div class="mb-2">
            <label for="password1" class="form-label">비밀번호</label>
            <input type="password" class="form-control" v-model.trim="password1" id="password1">
          </div>
          <div class="mb-2">
            <label for="password2" class="form-label">비밀번호 확인</label>
            <input type="password" class="form-control" v-model.trim="password2" id="password2">
          </div>
          <div class="mb-2">
            <label for="email" class="form-label">이메일</label>
            <input type="text" class="form-control" v-model.trim="email" id="email">
          </div>
          <div class="mb-2">
            <label for="nickname" class="form-label">닉네임</label>
            <input type="text" class="form-control" v-model.trim="nickname" id="nickname">
          </div>
          <div class="mb-2">
            <label for="birthdate">생년월일</label>
            <input type="date" class="form-control" v-model.trim="birthdate" id="birthdate">
          </div>
          <div class="mb-2">
            <label for="gender" class="form-label">성별</label>
            <div class="genderContainer">
              <div class="form-check">
                <input class="form-check-input" type="radio" id="male" value="M" v-model="gender">
                <label class="form-check-label" for="male">Male</label>
              </div>
              <div class="form-check">
                <input class="form-check-input" type="radio" id="female" value="F" v-model="gender">
                <label class="form-check-label" for="female">Female</label>
              </div>
            </div>
          </div>
          <div class="mb-2">
            <label for="address" class="form-label">주소</label>
            <input type="text" class="form-control"  v-model.trim="address" id="address">
          </div>
          <div class="mb-2">
            <label for="asset" class="form-label">자산</label>
            <input type="text" class="form-control"  v-model.trim="asset" id="asset">
          </div>
          <div class="mb-2">
            <label for="salary" class="form-label">월급</label>
            <input type="text" class="form-control"  v-model.trim="salary" id="salary">
          </div>
          <div class="mb-2">
            <label for="interest_industry" class="form-label">관심산업</label>
            <input type="text" class="form-control"  v-model.trim="interest_industry" id="interest_industry">
          </div>
          <div class="text-center">
            <input type="submit" value="가입하기">
          </div>
        </form>

      </div>
    </div>
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
.genderContainer {
  display: flex;
  justify-content: space-evenly;
}
</style>