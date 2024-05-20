<template>
  <main>
    <PopularDepositList />
    <PopularSavingList />
    <TodayLuck />
    <NaverNews />
    <FreeBoardList />
    <AgeBoardList />
    <CurrencyConverter />
  </main>
</template>

<script setup>
import PopularDepositList from '@/components/PopularDepositList.vue'
import PopularSavingList from '@/components/PopularSavingList.vue'
import TodayLuck from '@/components/TodayLuck.vue'
import NaverNews from '@/components/NaverNews.vue'
import FreeBoardList from '@/components/FreeBoardList.vue'
import AgeBoardList from '@/components/AgeBoardList.vue'
import CurrencyConverter from '@/components/CurrencyConverter.vue'

import axios from 'axios';
import { ref, onMounted } from 'vue';
import { userCheckStore } from '@/stores/usercheck';
import { useBoardStore } from '@/stores/board';

const userStore = userCheckStore()
const articles = ref(null)

const loadCrawlingData = function () {
    axios({
        method: 'get',
        url: `${userStore.API_URL}/api/v1/mainpage/`
    })
    .then((res) => {
        // console.log(res.data)
        articles.value = res.data.news_data
    })
    .catch((err) => {
        console.log(err)
    })
}


onMounted(() => {
    loadCrawlingData()
    // boardStore.getBoards('moneyMGMT')
    // boardStore.getBoards('local')
})

</script>

<style scoped>

</style>