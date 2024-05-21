import { ref } from 'vue'
import { defineStore } from 'pinia'
import { userCheckStore } from '@/stores/usercheck.js'
import axios from 'axios'
import { Colors } from 'chart.js'

export const useFinanceStore = defineStore('Finance', () => {
  const API_URL = 'http://127.0.0.1:8000'
  
  const store = userCheckStore()
  const depositList = ref([])
  const savingList = ref([])
  const depositOption = ref([])
  const savingOption = ref([])
  const recommendSavingList = ref([])
  const recommendDepositList = ref([])

  const getDepositList = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/deposit_products/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(res => {
        // console.log(res.data)
        depositList.value = res.data
      })
      .catch(err => console.log(err))
  }

  const getSavingList = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/saving_products/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(res => {
        // console.log(res)
        savingList.value = res.data
      })
      .catch(err => console.log(err))
  }

  const getDepositOption = function (fin_prdt_cd) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/deposit_product_options/${fin_prdt_cd}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        // console.log(res)
        depositOption.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getSavingOption = function (fin_prdt_cd) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/saving_product_options/${fin_prdt_cd}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        // console.log(res)
        savingOption.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const bankLink = ref([
    {
      "bank_name": "신한은행",
      "bank_url": "https://bank.shinhan.com/index.jsp#020105020000",
    },
    {
      "bank_name": "우리은행",
      "bank_url": "https://spot.wooribank.com/pot/Dream?withyou=PODEP0001",
    },
    {
      "bank_name": "대구은행",
      "bank_url": "https://www.dgb.co.kr/com_ebz_fpm_sub_main.jsp",
    },
    {
      "bank_name": "광주은행",
      "bank_url": "https://www.kjbank.com/ib20/mnu/FPMDPTR030000",
    },
    {
      "bank_name": "제주은행",
      "bank_url": "https://www.e-jejubank.com/HomeFinanceMallDeposit.do",
    },
    {
      "bank_name": "한국스탠다드차타드은행",
      "bank_url": "https://www.standardchartered.co.kr/np/kr/pl/se/SavingList.jsp?ptfrm=HIN.KOR.INTRO.mega.korPerA1_1&id=list1",
    },
    {
      "bank_name": "부산은행",
      "bank_url": "https://www.busanbank.co.kr/ib20/mnu/FPM00001",
    },
    {
      "bank_name": "전북은행",
      "bank_url": "https://www.jbbank.co.kr/",
    },
    {
      "bank_name": "경남은행",
      "bank_url": "https://www.knbank.co.kr/ib20/mnu/BHPFIS000000000",
    },
    {
      "bank_name": "중소기업은행",
      "bank_url": "https://mybank.ibk.co.kr/uib/jsp/index.jsp",
    },
    {
      "bank_name": "한국산업은행",
      "bank_url": "https://banking.kdb.co.kr/bp/index.jsp",
    },
    {
      "bank_name": "국민은행",
      "bank_url": "https://obank.kbstar.com/quics?page=C030037&QSL=F&_ga=2.196160940.1629055220.1700470410-794371171.1700030088#loading",
    },
    {
      "bank_name": "농협은행주식회사",
      "bank_url": "https://smartmarket.nonghyup.com/servlet/SFMN0001R.view",
    },
    {
      "bank_name": "하나은행",
      "bank_url": "https://www.kebhana.com/cont/mall/index.jsp",
    },
    {
      "bank_name": "수협은행",
      "bank_url": "https://www.suhyup-bank.com/",
    },
    {
      "bank_name": "주식회사 케이뱅크",
      "bank_url": "https://www.kbanknow.com/ib20/mnu/FPMDPT130000",
    },
    {
      "bank_name": "주식회사 카카오뱅크",
      "bank_url": "https://www.kakaobank.com/products/withdrawal",
    },
    {
      "bank_name": "토스뱅크 주식회사",
      "bank_url": "https://www.tossbank.com/product-service/savings/time-deposit",
    },
    {
      "bank_name": "MG새마을금고",
      "bank_url": "https://www.skhybank.com/deposit/depositList.do",
    },
  ])

  const searchBankLink = (bankname) => {
    const bank = bankLink.value.filter(bank => bank.bank_name.includes(bankname))
    return bank.length > 0 ? bank[0].bank_url : ''
  }

  const mapSearchBankLink = (bankname) => {
    // console.log(bankname);
    const nameParts = [];
    for (let i = 0; i < bankname.length - 2; i++) {
      nameParts.push(bankname.substring(i, i + 3));
    }
    // console.log(nameParts);
    const bank = bankLink.value.filter(bank => {
      // console.log(bank.bank_name);
      return nameParts.some(part => bank.bank_name.includes(part));
    });
    // console.log(bank.length);
    // console.log(bank[0].bank_url);
    return bank.length > 0 ? bank[0].bank_url : '';
  }


  const getSavingRecommendation = (amountData) => {
    const { inputAmount, targetAmount } = amountData
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/recommend_saving_products/?monthlyAmount=${inputAmount}&targetAmount=${targetAmount}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(res => {
        recommendSavingList.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }

  const getDepositRecommendation = (amountData) => {
    const { inputAmount, targetAmount } = amountData
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/recommend_deposit_products/?depositAmount=${inputAmount}&targetAmount=${targetAmount}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(res => {
        console.log(res.data)
        recommendDepositList.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { API_URL, depositList, savingList, depositOption, savingOption, recommendSavingList, recommendDepositList, getDepositRecommendation,
    getDepositList, getSavingList, getDepositOption, getSavingOption, bankLink, searchBankLink, mapSearchBankLink, getSavingRecommendation }
}, {persist: true})
