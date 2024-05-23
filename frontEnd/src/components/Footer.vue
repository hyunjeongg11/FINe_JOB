<template>
  <div>
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-item">
          <p>조현정</p>
          <a href="https://github.com/hyunjeongg11" target="_blank">
            <img 
              :src="isHovered1 ? '/assets/footer/github1.png' : '/assets/footer/github2.png'" 
              @mouseover="isHovered1 = true" 
              @mouseout="isHovered1 = false" 
              alt="GitHub" 
              class="github-icon">
          </a>
          <p>github.com/hyunjeongg11</p>
        </div>
        <div class="footer-item">
          <br>
          <p>SSAFY 11기 금융프로젝트</p>
          <p><a href="https://github.com/hyunjeongg11/FINe_JOB">FINe JOB github</a></p>
          <br>
          <p>&copy;FINe Job All rights reserved.</p>
        </div>
        <div class="footer-item">
          <p>손우혁</p>
          <a href="https://github.com/rt21hyuk" target="_blank">
            <img 
              :src="isHovered2 ? '/assets/footer/github1.png' : '/assets/footer/github2.png'" 
              @mouseover="isHovered2 = true" 
              @mouseout="isHovered2 = false" 
              alt="GitHub" 
              class="github-icon">
          </a>
          <p>github.com/rt21hyuk</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isHovered1 = ref(false)
const isHovered2 = ref(false)
</script>

<style scoped>
.footer {
  background-color: #f8f9fa;
  padding: 20px 0;
  border-top: 1px solid #00000044;
  text-align: center;
  margin-top: 150px;
}

.footer-content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  max-width: 800px;
  margin: 0 auto;
  margin-bottom: 60px;
  font-size: 13px;
}

.footer-item {
  text-align: center;
  color: #000000c0;
}

.footer-item p {
  margin: 5px 0;
}

.github-icon {
  width: 40px;
  height: 40px;
}
</style>
