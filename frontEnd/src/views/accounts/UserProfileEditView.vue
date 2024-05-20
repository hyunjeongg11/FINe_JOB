<template>
  <button @click="goBack" class="back-button">뒤로 가기</button>
  <div v-if="!userStore.token" class="container">
    <h3>비로그인 사용자입니다.</h3>
  </div>
  <div v-else>
    <div class="container mt-5">
      <h1>개인정보 수정</h1>
      <form @submit.prevent="updateDetail">
        <div class="d-flex justify-content-between align-items-center">
          <span>ID: {{ username }}</span>
          <button @click="goChangePassword" class="btn btn-primary">비밀번호 변경</button>
        </div>
        <hr>
        <div class="container sort">
          <div class="mb-3">
            <label for="email" class="form-label">E-Mail :</label>
            <input type="text" id="email" class="form-control" v-model="email" style="width: 70%;">
          </div>
          <div class="mb-3">
            <label for="nickname" class="form-label">닉네임 :</label>
            <input type="text" id="nickname" class="form-control" v-model="nickname" style="width: 70%;">
          </div>
          <div class="mb-3">
            <label for="province" class="form-label">주소 :</label>
            <select name="province" id="province" class="form-select" v-model="province" style="width: 70%;">
              <option :value="pr" v-for="pr in provinceInput">{{ pr }}</option>
            </select>
            <select name="country" id="country" class="form-select" v-model="country" style="width: 70%;">
              <option :value="ct" v-for="ct in countryInput[prIdx]">{{ ct }}</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="birthday" class="form-label">생년월일 :</label>
            <input type="text" id="birthday" class="form-control" placeholder="YYYYMMDD" v-model="birthday" style="width: 70%;">
          </div>
          <div class="mb-3">
            <label for="gender" class="form-label">성별 :</label>
            <select id="gender" class="form-select" v-model="gender" style="width: 70%;">
              <option disabled value="">다음 중 하나를 선택하세요</option>
              <option value="M">남성</option>
              <option value="W">여성</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="asset" class="form-label">자산 :</label>
            <input type="text" id="asset" class="form-control" v-model="asset" style="width: 70%;">원
          </div>
          <div class="mb-3">
            <label for="salary" class="form-label">연봉 :</label>
            <input type="text" class="form-control" v-model="salary" style="width: 70%;">원
          </div>   
          <div class="mb-3">
            <label for="interest_industry" class="form-label">관심 산업 :</label>
            <select name="interest_industry" id="interest_industry" class="form-select" v-model="interest_industry" style="width: 70%;">
              <option :value="job" v-for="job in jobChoices">{{ job }}</option>
            </select>
          </div>
        </div>
        <div class="d-flex justify-content-center">
          <button type="submit" class="btn btn-primary text-center col-2">수정</button>
        </div>
        <div class="d-flex justify-content-center">
          <button @click="userStore.withdraw" class="btn btn-danger">회원 탈퇴</button>
        </div>
      </form>
    </div>
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
const province = ref()
const country = ref()

const goChangePassword = function (pk) {
  router.push({ name: 'changepassword' })
}

const provinceInput = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도', '강원특별자치도']

const countryInput = {
  0: ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
  1: ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'],
  2: ['군위군', '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구'],
  3: ['강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군', '중구'],
  4: ['광산구', '남구', '동구', '북구', '서구'],
  5: ['대덕구', '동구', '서구', '유성구', '중구'],
  6: ['남구', '동구', '북구', '울주군', '중구'],
  7: [''],
  8: ['가평군', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시 분당구', '성남시 수정구', '성남시 중원구', '수원시 권선구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '시흥시', '안산시 단원구', '안산시 상록구', '안성시', '안양시 동안구', '안양시 만안구', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시 기흥구', '용인시 수지구', '용인시 처인구', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시'],
  9: ['괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천군', '청주시 상당구', '청주시 서원구', '청주시 청원구', '청주시 흥덕구', '충주시'],
  10: ['계롱시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군'],
  11: ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군', '장수군', '전주시 덕진구', '전주시 완산구', '정읍시', '진안군'],
  12: ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '목포시', '무안군', '보성군', '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군'],
  13: ['경산시', '경주시', '고령군', '구미시', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시 남구', '포항시 북구'],
  14: ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군', '창원시 마산합포구', '창원시 마산회원구', '창원시 성산구', '창원시 의창구', '창원시 진해구', '통영시', '하동군', '함안군', '함양군', '합천군'],
  15: ['서귀포시', '제주시'],
  16: ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군']
}

const jobChoices = ['IT', '서비스', '금융', '보험', '인사', '노무', '회계', '세무', '재무', '디자인', '생산', '영업', '상품기획', '교육', 'R&D', '의료', '건축', '전기', '기계', '고객상담', '운송', '미디어', '스포츠', '복지'];

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

const updateDetail = function () {
  axios({
    method: 'put',
    url: `${userStore.API_URL}/api/v1/accounts/edit_user_info/`,
    data: {
      email: email.value,
      nickname: nickname.value,
      gender: gender.value,
      birthday: birthday.value,
      address: address.value,
      asset: asset.value,
      salary: salary.value,
      interest_industry: interest_industry.value,
      userId: userStore.userId,
    },
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
  .then((res) => {
    console.log('프로필 수정 완료');
    window.alert('개인정보 수정이 완료되었습니다.');
    router.push({ name: 'userprofile' });
  })
  .catch((err) => {
    console.error(err);
    window.alert('정보 수정에 실패했습니다.');
  })
}


const prIdx = computed(() => {
  return provinceInput.findIndex((item) => item === province.value)
})

watch([province, country], () => {
  address.value = province.value + ' ' + country.value
})

function goBack() {
  router.back();
}

</script>

<style scoped>
.back-button {
  margin: 10px 10px;
  padding: 5px 10px;
  font-size: 16px;
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.back-button:hover {
  background-color: rgb(165, 165, 165);
}
</style>
