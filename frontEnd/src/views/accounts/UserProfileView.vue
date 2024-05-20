<template>
	<div class="profile-page">
	  <h1>{{ userStore.userId }}님의 프로필페이지</h1>
	  <div class="profile-container">
		<div class="profile-info">
		  <UserProfile />
		</div>
		<div class="additional-info">
		  <SubscribeProduct />
		  <AgeBoardRecord />
		  <FreeBoardRecord />
		</div>
	  </div>
	</div>
	<RouterView />
  </template>
  
  <script setup>
  import { RouterView } from 'vue-router'
  import UserProfile from '@/components/UserProfile.vue'
  import SubscribeProduct from '@/components/SubscribeProduct.vue'
  import AgeBoardRecord from '@/components/AgeBoardRecord.vue'
  import FreeBoardRecord from '@/components/FreeBoardRecord.vue'
  import { userCheckStore } from '@/stores/usercheck'
  
  const userStore = userCheckStore()
  </script>
  
  <style scoped>
  .profile-page {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 20px;
  }
  
  .profile-container {
	display: flex;
	width: 100%;
  }
  
  .profile-info {
	width: 50%; /* Left half of the screen */
  }
  
  .additional-info {
	width: 50%; /* Right half of the screen */
	display: flex;
	flex-direction: column;
  }
  
  h1 {
	text-align: center;
	margin-bottom: 20px;
  }
  </style>
  