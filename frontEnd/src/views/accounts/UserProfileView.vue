<template>
    <div>
        <h1>마이페이지</h1>
        <RouterLink :to="{name : 'changepassword'}">비밀번호 변경</RouterLink>
        <UserProfile />
        <SubscribeProduct />
        <AgeBoardRecord />
        <FreeBoardRecord />
    </div>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import UserProfile from '@/components/UserProfile.vue'
import SubscribeProduct from '@/components/SubscribeProduct.vue'
import AgeBoardRecord from '@/components/AgeBoardRecord.vue'
import FreeBoardRecord from '@/components/FreeBoardRecord.vue'
</script>

<style scoped>

</style>