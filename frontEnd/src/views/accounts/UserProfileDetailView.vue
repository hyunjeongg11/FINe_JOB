<template>
  <div class="profile-container">
    <img :src="`/assets/profile.png`" alt="Profile Image" class="profile-img" />
    <div class="profile-info">
      <div class="info-item">
        <span class="label">ID:</span>
        <span class="value">{{ username }}</span>
      </div>
      <div class="info-item">
        <span class="label">E-Mail:</span>
        <span class="value">{{ email }}</span>
      </div>
      <div class="info-item">
        <span class="label">닉네임:</span>
        <span class="value">{{ nickname || '닉네임이 없습니다' }}</span>
      </div>
      <div class="info-item">
        <span class="label">생년월일:</span>
        <span class="value">{{ birthday || '생년월일이 입력되지 않았습니다' }}</span>
      </div>
      <div class="info-item">
        <span class="label">성별:</span>
        <span class="value">{{ gender === 'M' ? '남성' : gender === 'W' ? '여성' : '성별이 입력되지 않았습니다'}}</span>
      </div>
      <div class="info-item">
        <span class="label">자산:</span>
        <span class="value">{{ asset ? asset + '원' : '자산이 입력되지 않았습니다' }}</span>
      </div>
      <div class="info-item">
        <span class="label">연봉:</span>
        <span class="value">{{ salary ? salary + '원' : '연봉이 입력되지 않았습니다' }}</span>
      </div>
      <div class="info-item">
        <span class="label">관심 산업:</span>
        <span class="value">{{ interest_industry || '선택된 관심 산업이 없습니다.' }}</span>
      </div>
    </div>
    <button @click="goUserProfileEdit" class="btn update-button">개인정보 수정</button>
  </div>
</template>


<script setup>
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const userStore = userCheckStore()

const username = ref(null)
const email = ref(null)
const birthday = ref(null)
const nickname = ref(null)
const gender = ref(null)
const profile_img = ref(null)
const asset = ref(null)
const salary = ref(null)
const interest_industry = ref(null)

const goUserProfileEdit = function () {
      router.push({ name: 'userprofileedit' })
  }

const checkUser = function () {
	axios({
		method: 'get',
		url: `${userStore.API_URL}/api/v1/accounts/user_detail/${userStore.userId}`,
		headers: {
			Authorization: `Token ${userStore.token}`
		}
	})
		.then((res) => {
      console.log(res.data.user_data)
			const userData = res.data.user_data
			username.value = userData.username
			email.value = userData.email
			nickname.value = userData.nickname
			birthday.value = userData.birthday
			gender.value = userData.gender
			asset.value = userData.asset
			salary.value = userData.salary
      interest_industry.value = userData.interest_industry

		})
		.catch((err) => {
			console.log(err)
		})
}

onMounted(() => {
		checkUser()
})
</script>

<style scoped>
.profile-container {
  width: 400px;
  margin: 30px 20%;
  text-align: center;
}

.profile-img {
  width: 250px;
  height: 250x;
  margin-bottom: 20px;
}

.profile-info {
  text-align: left;
}

.profile-info .info-item {
  margin-bottom: 15px;
}

.label {
  display: inline-block;
  width: 120px;
  font-weight: bold;
  font-size: 18px;
}

.value {
  display: inline-block;
  font-size: 18px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 70%;
  text-align: left;
}

.update-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

.update-button:disabled {
  background-color: #007bff;
  opacity: 0.65;
  cursor: not-allowed;
}
</style>
