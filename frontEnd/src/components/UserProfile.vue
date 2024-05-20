<template>
  <div class="container sort">
    <!-- <div class="mb-2">
      <label for="profile_img" class="form-label">ID : {{ profile_img }}</label>
    </div> -->
    <div class="mb-2">
      <label for="username" class="form-label">ID : {{ username }}</label>
    </div>
    <div class="mb-2">
      <label for="email" class="form-label">E-Mail : {{ email }}</label>
    </div>
    <div class="mb-2">
      <label for="nickname" class="form-label">닉네임 : {{ nickname }}</label>
    </div>
    <div class="mb-2">
      <label for="birthday" class="form-label">생년월일 : {{ birthday }}</label>
    </div>
    <div class="mb-2">
      <label for="gender" class="form-label">성별 : {{ gender === 'M' ? '남자' : gender === 'W' ? '여자' : '기타' }}</label>
    </div>
    <div class="mb-2">
      <label for="asset" class="form-label">자산 : {{ asset || '입력한 값이 없습니다.' }}</label>
    </div>
    <div class="mb-2">
      <label for="salary" class="form-label">연봉 : {{ salary || '입력한 값이 없습니다.' }}</label>
    </div>
    <button @click="goUserProfileEdit" class="btn btn-primary">개인정보 수정</button>
  </div>
</template>


<script setup>
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck'
import { ref, onMounted, computed, watch } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const userStore = userCheckStore()

const username = ref(null)
const email = ref(null)
const birthday = ref(null)
const nickname = ref(null)
const gender = ref(null)
const address = ref(null)
const profile_img = ref(null)
const asset = ref(null)
const salary = ref(null)
const interest_industry = ref(null)

const goUserProfileEdit = function (pk) {
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
			// console.log(userStore.token)
			console.log(res.data.user_data)
			username.value = res.data.user_data.username
			email.value = res.data.user_data.email
			nickname.value = res.data.user_data.nickname
			birthday.value = res.data.user_data.birthday
			gender.value = res.data.user_data.gender
			// province.value = res.data.user_data.address.split(' ')[0]
			// country.value = res.data.user_data.address.split(' ')[1]
			asset.value = res.data.user_data.asset
			salary.value = res.data.user_data.salary
			interest_industry.value = res.data.user_data.interest_industry
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
.container {
  border: 1px solid black;
}
</style>