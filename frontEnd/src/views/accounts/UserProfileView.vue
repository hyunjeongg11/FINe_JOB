<template>
  <div class="profile-page">
    <h1>{{ userStore.userId }}님의 프로필페이지</h1>
    <div class="content">
      <nav class="sidebar">
				<RouterLink :to="{ name: 'userprofile' }" class="link" active-class="active-link">내 프로필</RouterLink>
				<RouterLink :to="{ name: 'subscribeproduct' }" class="link" active-class="active-link">가입한 금융 상품</RouterLink>
				<RouterLink :to="{ name: 'boardrecord'}" class="link" active-class="active-link">작성한 게시글</RouterLink>
      </nav>
      <div class="detail-view">
        <UserProfileDetailView />
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import UserProfileDetailView from '@/views/accounts/UserProfileDetailView.vue'
import { userCheckStore } from '@/stores/usercheck'

const userStore = userCheckStore()
</script>

<style scoped>
.profile-page {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1 {
  text-align: center;
}

.content {
  display: flex;
  width: 100%;
  max-width: 1500px;
}

.sidebar {
  border: 1px solid black;
  padding: 20px;
	height: 60%;
  width: 250px;
  margin-right: 30px;
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
