<template>
  <div class="container">
    <nav>
      <RouterLink :to="{ name: 'freeboard' }" class="nav-item">자유게시판</RouterLink> | 
      <RouterLink :to="{ name: 'ageboard' }" class="nav-item-here">연령별게시판</RouterLink> | 
      <RouterLink :to="{ name: 'FAQ' }" class="nav-item">FAQ</RouterLink>
    </nav>
    <div v-if="isLogin">
      <div v-if="ageBoard">
        <div class="post-header">
          <h2 class="title">{{ ageBoard.title }}</h2>
          <div class="post-meta">
            <img :src="`/assets/profile.png`" alt="profile" style="height: 35px; width: 35px; border-radius: 20px;"> &nbsp;&nbsp;
            {{ ageBoard.user.username }} | {{ getAgeGroup(ageBoard.user.birthday, ageBoard.created_at) }} | {{ formattedCreatedAt }}
          </div>
          <hr>
        </div>
        <div class="post-content">
          <p>{{ ageBoard.content }}</p>
        </div>
        <div v-if="ageBoard.image" class="attachment">
          첨부파일: <a :href="ageBoard.image" download>{{ fileName }}</a>
        </div>
        <hr>
        <div class="comments-section">
          <AgeBoardComment />
        </div>
        <div class="actions-row">
          <button class="back" @click="goBack">목록으로</button>
          <div class="actions">
            <button class="fix" v-if="ageBoard.user.username === userStore.userId" @click="goToEditPage">게시글 수정</button>
            <button class="delete" v-if="ageBoard.user.username === userStore.userId" @click="deleteBoard">게시글 삭제</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, useRoute, useRouter } from 'vue-router'
import AgeBoardComment from '@/components/AgeBoardComment.vue'
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useBoardStore } from '@/stores/board'
import { userCheckStore } from '@/stores/usercheck'

const store = useBoardStore()
const userStore = userCheckStore()
const route = useRoute()
const router = useRouter()
const ageBoard = ref(null)
const isLogin = computed(() => userStore.isLogin)

function goBack() {
    router.back();
}

onMounted(async () => {
  if (!isLogin.value) {
    alert('로그인 해주세요')
    router.push({ name: 'login' })
  } else {
    try {
      const res = await axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/boards/age/${route.params.id}`,
        headers: {
          Authorization: `Token ${userStore.token}` // 인증 토큰을 헤더에 추가
        }
      });
      ageBoard.value = res.data;
    } catch (err) {
      console.log(err);
    }
  }
})

const formatDateTime = (datetime) => {
  const date = new Date(datetime)
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  const hours = date.getHours()
  const minutes = String(date.getMinutes()).padStart(2, '0')
  return `${year}.${month}.${day} ${hours}:${minutes}`
}

const formattedCreatedAt = computed(() => {
  return ageBoard.value ? formatDateTime(ageBoard.value.created_at) : ''
})

const formattedUpdatedAt = computed(() => {
  return ageBoard.value ? formatDateTime(ageBoard.value.updated_at) : ''
})

const getAgeGroup = (birthday, date) => {
  if (!birthday) {
    return '알 수 없음'
  }
  const age = calculateAgeOnDate(birthday, date)
  if (isNaN(age)) {
    return '알 수 없음'
  }
  if (age <= 20) {
    return '20대 이하'
  } else if (age >= 70) {
    return '70대 이상'
  } else {
    return `${Math.floor(age / 10) * 10}대`
  }
}

const calculateAgeOnDate = (birthday, date) => {
  const birthDate = new Date(birthday)
  const targetDate = new Date(date)
  let age = targetDate.getFullYear() - birthDate.getFullYear()
  const monthDifference = targetDate.getMonth() - birthDate.getMonth()

  if (monthDifference < 0 || (monthDifference === 0 && targetDate.getDate() < birthDate.getDate())) {
    age--
  }
  return age
}

const goToEditPage = () => {
  router.push(`/ageboarddetail/${route.params.id}/update`)
}

const deleteBoard = () => {
  if (confirm('정말로 이 게시글을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/boards/age/${route.params.id}`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(() => {
        alert('게시글이 삭제되었습니다.')
        router.push({ name: 'ageboard' })
      })
      .catch((err) => {
        console.log(err)
        alert('게시글 삭제에 실패했습니다.')
      })
  }
}

const fileName = computed(() => {
  if (ageBoard.value && ageBoard.value.image) {
    const parts = ageBoard.value.image.split('/')
    return parts[parts.length - 1]
  }
  return ''
})
</script>

<style scoped>
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
}

nav {
  margin-bottom: 20px;
}

.nav-item {
  color: black;
  text-decoration: none;
}

.nav-item-here {
  color: black;
}

.post-header {
  margin-bottom: 20px;
}

.post-header h2 {
  margin-bottom: 25px;
}

.post-meta {
  font-size: 14px;
  color: #555;
}

.post-content {
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 4px;
  background-color: #fff;
  height: 150px;
  /* margin-bottom: 40px; */
}

.attachment {
  margin-top: 20px;
}

.actions-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.actions {
  display: flex;
  gap: 10px;
}

.fix {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  color: black;
  cursor: pointer;
}

.fix:hover {
  background-color: rgb(126, 186, 205);
}

.delete {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  color: black;
  cursor: pointer;
}

.delete:hover {
  background-color: #e7707c;
}

.back {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  color: black;
  cursor: pointer;
}

.back:hover {
  background-color: rgb(173, 216, 230);
}

.comments-section {
  margin-top: 20px;
}
</style>
