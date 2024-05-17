<template>
    <div>
        <RouterLink :to="{name : 'signup'}">회원가입</RouterLink> 
    </div>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>