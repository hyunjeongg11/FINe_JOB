<template>
  <div class="container">
    <img :src="gifSrc" class="intro-image-gif" alt="Intro 1">
    <img class="intro-image" src="/assets/intro/intro2.png" alt="Intro 2">
    <img class="intro-image" src="/assets/intro/intro3.png" alt="Intro 3">
    <img class="intro-image" src="/assets/intro/intro4.png" alt="Intro 4">
    <img class="intro-image" src="/assets/intro/intro5.png" alt="Intro 5">
    <img class="intro-image" src="/assets/intro/intro6.png" alt="Intro 6">
    <img class="intro-image" src="/assets/intro/intro7.png" alt="Intro 7">
    <img class="intro-image" src="/assets/intro/intro8.png" alt="Intro 8">
    <img class="intro-image" src="/assets/intro/intro9.png" alt="Intro 9">
    <div class="intro-logo">
      <img 
        class="intro-image logo" :src="logoSrc" alt="FINe">
      <button type="submit" class="btn text-center main-btn" @click="goToMainPage" @mouseover="changeLogo(true)" @mouseleave="changeLogo(false)">메인페이지로 이동</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'

const gifSrc = ref('')
const logoSrc = ref('/assets/logo/big_logo.png')
const hoveringLogo = ref(false)
const router = useRouter()

onMounted(() => {
  resetGif()
  setTimeout(() => {
    showImages()
  }, 300) 
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
  router.push({ name: 'main' }).then(() => {
    window.scrollTo(0, 0)
  })
}

const changeLogo = (hover) => {
  logoSrc.value = hover ? '/assets/logo/big_logo_hover.png' : '/assets/logo/big_logo.png'
  hoveringLogo.value = hover
}
</script>

<style scoped>
.container {
  text-align: center;
}

.intro-logo {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
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
  margin-top: 20px;
  height: 80px;
  font-size: 25px;
}

.main-btn:hover {
  background-color: rgb(45, 101, 119);
}

.logo {
  width: 50%;
  margin: 0 auto;
}

.hover-text {
  font-size: 20px;
  color: rgb(59, 130, 153);
  margin-bottom: 10px;
  width: 100%;
}
</style>
