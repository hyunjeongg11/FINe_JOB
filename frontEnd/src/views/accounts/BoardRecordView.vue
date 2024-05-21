<template>
	<div class="container mt-5">
		<div class="main-content">
			<nav class="sidebar">
				<RouterLink :to="{ name: 'userprofile' }" class="link" active-class="active-link">내 프로필</RouterLink>
				<RouterLink :to="{ name: 'subscribeproduct' }" class="link" active-class="active-link">가입한 금융 상품</RouterLink>
				<RouterLink :to="{ name: 'boardrecord'}" class="link" active-class="active-link">작성한 게시글</RouterLink>
			</nav>
      <div class="detail-view">
        <h3 class="mb-3">{{ store.userId }}님이 작성한 연령별게시글</h3>
					<div class="list-group">
						<div v-for="ageboard in boards.age_boards" :key="ageboard.id" @click="goDetailAgeBoard(ageboard.id)" class="list-group-item list-group-item-action d-flex justify-content-between">
							<p class="my-auto"><strong>제목 : </strong>{{ ageboard.title }}</p>
							<p class="my-auto"><strong>작성일 : </strong>{{ formatDate(ageboard.created_at) }}</p>
						</div>
					</div>
				<h3 class="mt-4">{{ store.userId }}님이 작성한 자유게시글</h3>
					<div class="list-group">
						<div v-for="freeboard in boards.free_boards" :key="freeboard.id" @click="goDetailFreeBoard(freeboard.id)" class="list-group-item list-group-item-action d-flex justify-content-between">
							<p class="my-auto"><strong>제목 : </strong>{{ freeboard.title }}</p>
							<p class="my-auto"><strong>작성일 : </strong>{{ formatDate(freeboard.created_at) }}</p>
						</div>
					</div>
				</div>
		</div>
	</div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck'

const router = useRouter()
const store = userCheckStore()
const boards = ref('')

const goDetailAgeBoard = function (id) {
    router.push({name: 'ageboarddetail', params: {id: id}})
}

const goDetailFreeBoard = function (id) {
    router.push({name: 'freeboarddetail', params: {id: id}})
}

const getLog = () => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/boards/user_log/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then((res) => {
            // console.log(res.data)
            boards.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
}
onMounted(() => {
  getLog()
})

const formatDate = function (dateString) {
    const date = new Date(dateString)
    const year = date.getFullYear()
    const month = ('0' + (date.getMonth() + 1)).slice(-2)
    const day = ('0' + date.getDate()).slice(-2);
    const hours = ('0' + date.getHours()).slice(-2);
    const minutes = ('0' + date.getMinutes()).slice(-2);

    // Form the desired date string
    const formattedDate = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes
    return formattedDate
}
</script>

<style scoped>
h2 {
  text-align: center;
	margin-bottom: 30px;
}
.container {
  max-width: 1500px;
  margin: auto;
}

.main-content {
  display: flex;
}

.sidebar {
  border: 1px solid black;
  padding: 20px;
	height: 60%;
  width: 250px;
  margin-right: 30px;
  margin-top: 8px;
  border-radius: 5px;
}

.link {
  display: block;
  padding: 10px 0;
  color: black;
  text-decoration: none;
}

.active-link {
  font-weight: bold;
  text-decoration: underline;
}

.detail-view {
  flex: 1;
}
</style>