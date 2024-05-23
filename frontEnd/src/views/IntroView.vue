<template>
  <div class="container">
    <img :src="gifSrc" class="intro-image-gif" alt="인트로 1">
    <img class="intro-image" src="/assets/intro/intro2.png" alt="인트로 2">
    <img class="intro-image" src="/assets/intro/intro3.png" alt="인트로 3">
    <img class="intro-image" src="/assets/intro/intro4.png" alt="인트로 4">
    <img class="intro-image" src="/assets/intro/intro5.png" alt="인트로 5">
    <img class="intro-image" src="/assets/intro/intro6.png" alt="인트로 6">
    <img class="intro-image" src="/assets/intro/intro7.png" alt="인트로 7">
    <img class="intro-image" src="/assets/intro/intro8.png" alt="인트로 8">
    <img class="intro-image" src="/assets/intro/intro9.png" alt="인트로 9">
    <button type="submit" class="btn text-center main-btn" @click="goToMainPage">메인페이지로 이동</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const gifSrc = ref('')
const router = useRouter()

onMounted(() => {
  resetGif()
  setTimeout(() => {
    showImages()
  }, 300) // 0.3초 뒤에 이미지 보이기 함수 호출
  window.addEventListener('scroll', showImages)
})

const showImages = () => {
  const images = document.querySelectorAll('.intro-image')
  images.forEach((image) => {
    if (isElementInViewport(image)) {
      image.classList.add('show')
    }
  })
}

const resetGif = () => {
  const timestamp = new Date().getTime()
  gifSrc.value = `/assets/intro/intro1.gif?${timestamp}`
}

const isElementInViewport = (el) => {
  const rect = el.getBoundingClientRect()
  const windowHeight = window.innerHeight || document.documentElement.clientHeight
  const windowWidth = window.innerWidth || document.documentElement.clientWidth
  const vertInView = (rect.top <= windowHeight) && ((rect.top + rect.height) >= 0)
  const horInView = (rect.left <= windowWidth) && ((rect.left + rect.width) >= 0)
  return (vertInView && horInView)
}

const goToMainPage = () => {
  // 'main' 페이지의 최상단으로 이동
  router.push({ name: 'main' }).then(() => {
    // 페이지 이동 후 스크롤을 맨 위로 올립니다.
    window.scrollTo(0, 0)
  })
}
</script>

<style scoped>
.container {
  text-align: center;
}

.intro-image-gif {
  width: 80%;
  height: auto;
  object-fit: contain;
  margin: 0 auto 250px;
}

.intro-image {
  width: 80%;
  height: auto;
  object-fit: contain;
  margin: 0 auto 250px;
  opacity: 0;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.intro-image.show {
  animation: fadeIn 4s ease forwards;
}

.main-btn {
  background-color: rgb(59, 130, 153);
  border-color: rgb(95, 170, 173);
  width: 300px;
  color: white;
  margin-right: 10%;
  height: 80px;
  font-size: 25px;
}
.main-btn:hover {
  background-color: rgb(45, 101, 119);
}
</style>
