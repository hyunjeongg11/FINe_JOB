<template>
	<div>
		<h5>{{ ageBoard.id }}</h5>
		<p>{{ ageBoard.title }}</p>
		<p>{{ ageBoard.content }}</p>
		<hr>
	</div>
</template>

<script setup>
defineProps({
	ageBoard: Object
})
</script>

<style scoped>

</style>