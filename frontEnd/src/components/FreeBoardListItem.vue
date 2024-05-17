<template>
    <div>
        <h5>{{ freeBoard.id }}</h5>
        <p>{{ freeBoard.title }}</p>
        <p>{{ freeBoard.content }}</p>
        <hr>
    </div>
</template>

<script setup>
defineProps({
    freeBoard: Object
})
</script>

<style scoped>

</style>