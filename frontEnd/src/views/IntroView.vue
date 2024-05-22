<template>
	<div class="container">
		<img class="intro-image" src="/assets/carousel/1.jpg" alt="인트로 이미지 1">
		<img class="intro-image" src="/assets/carousel/2.jpg" alt="인트로 이미지 2">
		<img class="intro-image" src="/assets/carousel/3.jpg" alt="인트로 이미지 3">
		<img class="intro-image" src="/assets/carousel/4.jpg" alt="인트로 이미지 4">
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

onMounted(() => {
	setTimeout(() => {
		showImages();
	}, 300); // 0.3초 뒤에 이미지 보이기 함수 호출
	window.addEventListener('scroll', showImages);
});

const showImages = () => {
	const images = document.querySelectorAll('.intro-image');
	images.forEach((image) => {
		if (isElementInViewport(image)) {
			image.classList.add('show');
		}
	});
};

const isElementInViewport = (el) => {
	const rect = el.getBoundingClientRect();
	const windowHeight = window.innerHeight || document.documentElement.clientHeight;
	const windowWidth = window.innerWidth || document.documentElement.clientWidth;
	const vertInView = (rect.top <= windowHeight) && ((rect.top + rect.height) >= 0);
	const horInView = (rect.left <= windowWidth) && ((rect.left + rect.width) >= 0);
	return (vertInView && horInView);
};
</script>

<style scoped>
.container {
	text-align: center; /* 내부 컨텐츠의 수평 가운데 정렬을 위해 추가 */
}

.intro-image {
	width: 60%;
	height: auto;
	object-fit: contain;
	margin: 0 auto 300px; /* 이미지를 수평 가운데 정렬하고 아래 여백 추가 */
	opacity: 0; /* 초기에는 이미지를 숨김 */
}


/* 스크롤을 내리면 이미지가 서서히 나타나도록 설정 */
@keyframes fadeIn {
	from {
		opacity: 0;
	}
	to {
		opacity: 1;
	}
}

/* 스크롤 이벤트에 따라 이미지가 나타날 때 애니메이션 적용 */
.intro-image.show {
	animation: fadeIn 2s ease forwards;
}
</style>
