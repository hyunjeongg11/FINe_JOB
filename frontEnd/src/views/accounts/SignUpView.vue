<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6 signup-outer position-relative">
        <h1 class="mb-4 signup-title">회원가입</h1>
        <div class="signup-content">
          <form @submit.prevent="signUp">
            <div class="mb-2">
              <label for="username" class="form-label">아이디</label>
              <input type="text" class="form-control" v-model.trim="username" id="username" placeholder="아이디 입력">
            </div>
            <div class="mb-2">
              <label for="password1" class="form-label">비밀번호</label>
              <input type="password" class="form-control" v-model.trim="password1" id="password1" placeholder="비밀번호 입력">
            </div>
            <div class="mb-2">
              <label for="password2" class="form-label">비밀번호 확인</label>
              <input type="password" class="form-control" v-model.trim="password2" id="password2" placeholder="비밀번호 확인">
            </div>
            <div class="mb-2">
              <label for="email" class="form-label">이메일</label>
              <input type="text" class="form-control" v-model.trim="email" id="email" placeholder="이메일 입력">
            </div>
            <div class="mb-2">
              <label for="nickname" class="form-label">닉네임</label>
              <input type="text" class="form-control" v-model.trim="nickname" id="nickname" placeholder="닉네임 입력">
            </div>
            <div class="mb-2">
              <label for="birthdate" class="form-label">생년월일</label>
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
              <input type="text" class="form-control" v-model.trim="address" id="address" placeholder="주소 입력">
            </div>
            <div class="mb-2">
              <label for="asset" class="form-label">자산</label>
              <input type="text" class="form-control" v-model.trim="asset" id="asset" placeholder="개인 자산 입력">
            </div>
            <div class="mb-2">
              <label for="salary" class="form-label">월 수입</label>
              <input type="text" class="form-control" v-model.trim="salary" id="salary" placeholder="월 수입 입력">
            </div>
            <div class="mb-2">
              <label for="interest_industry" class="form-label">관심산업</label>
              <select class="form-control" v-model="interest_industry" id="interest_industry">
                <option disabled value="">관심산업 선택</option>
                <option v-for="industry in industries" :key="industry" :value="industry">{{ industry }}</option>
              </select>
            </div>
            <div class="text-center">
              <input type="submit" class="signup-btn" value="가입하기">
            </div>
          </form>
        </div>
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

const industries = [
  'IT', '서비스', '금융', '보험', '인사', '노무', '회계', '세무', '재무', '디자인', 
  '생산', '영업', '상품기획', '교육', 'R&D', '의료', '건축', '전기', '기계', 
  '고객상담', '운송', '미디어', '스포츠', '복지'
]

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

.signup-title {
  text-align: center;
}

.signup-content {
  background-color: white;
  padding: 1rem;
  border-radius: 10px;
}

.signup-outer {
  padding: 2rem;
  border: 1px solid #e9ecef;
  background-color: rgb(236, 245, 248);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: relative;
}

.signup-btn {
  width: 100px;
  margin: 10px auto;
  background-color: rgb(180, 212, 255);
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}

.signup-btn:hover {
  background-color: rgb(104, 142, 206);
}
</style>
