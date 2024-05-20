<template>
  <div>
    <p>모집공고 : <a :href="jobBoard.url" target="_blank">{{ jobBoard.title }}</a></p>
    <p>회사 : {{ jobBoard.company }}</p>
    <p>마감일 : {{ jobBoard.deadline }}</p>
    <p>근무지 : {{ jobBoard.location }}</p>
    <p>경력사항 : {{ jobBoard.experience }}</p>
    <p>요구사항 : {{ jobBoard.requirement }}</p>
    <p>근무형태 : {{ jobBoard.jobtype }}</p>
    <hr>
    <!-- <p>{{ jobBoard.experience }}</p> -->
  </div>
</template>

<script setup>
defineProps({
	jobBoard: Object
})
</script>

<style scoped>

</style>