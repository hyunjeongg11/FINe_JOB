<template>
  <div class="container">
    <ul class="nav nav-underline">
      <li class="nav-item">
        <RouterLink :to="{name: 'freeboard'}" class="nav-link" :class="{ active: isActiveRoute('freeboard') }">자유게시판</RouterLink>
      </li>
      <li class="nav-item"> 
        <RouterLink :to="{name: 'ageboard'}" class="nav-link" :class="{ active: isActiveRoute('ageboard') }">연령별게시판</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink :to="{name: 'FAQ'}" class="nav-link" :class="{ active: isActiveRoute('FAQ') }">FAQ</RouterLink>
      </li>
    </ul>
    <div class="container">
      <FreeBoardList />
    </div>
  </div>
</template>

<script setup>
import { RouterLink, useRouter, useRoute } from 'vue-router'
import FreeBoardList from '@/components/FreeBoardList.vue'
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()
const router = useRouter()
const route = useRoute()

onMounted(() => {
  store.getFreeBoards()
})

function goBack() {
  router.back()
}

function isActiveRoute(name) {
  return route.name === name
}
</script>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 20px;
}
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

nav {
  margin-bottom: 20px;
}

.nav-link {
  color: black;
  font-size: 20px;
}

.nav-link.active {
  color: black;
  border-bottom: 2px solid black;
}

.nav-link:hover,
.nav-link.active {
  color: rgb(59, 130, 153);
}

.nav-underline {
  display: flex;
  justify-content: flex-start;
  list-style: none;
  padding-left: 40px;
  /* border-bottom: 1px solid #dee2e6; */
}

.nav-item {
  margin-right: 20px;
}
</style>
