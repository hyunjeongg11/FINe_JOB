<template>
  <div class="create-comment">
    <form @submit.prevent="submitComment">
      <div class="form-group">
        <label for="content">내용</label>
        <textarea id="content" v-model.trim="content" required></textarea>
      </div>
      <div class="form-actions">
        <button class="submit-btn" type="submit">작성</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'
import { useRoute } from 'vue-router'

const userStore = userCheckStore()
const store = useBoardStore()
const route = useRoute()
const content = ref('')

const emits = defineEmits(['comment-added'])

const submitComment = () => {
  const data = {
    content: content.value
  }

  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/boards/age/${route.params.id}/comments/`,
    data: data,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then((res) => {
      alert('댓글이 작성되었습니다.')
      content.value = ''
      emits('comment-added', res.data) // 부모 컴포넌트에 이벤트 발생, 작성된 댓글 데이터를 함께 전달
    })
    .catch((err) => {
      console.log(err)
      alert('댓글 작성에 실패했습니다.')
    })
}
</script>

<style scoped>
.create-comment {
  margin-top: 20px;
  border: #ccc solid 1px;
  padding: 10px;
  background-color: #f0f0f080;
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}


#content {
  height: 100px;
}
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-actions {
  text-align: right;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: rgb(45, 101, 119);
}

.submit-btn {
  background-color: rgb(59, 130, 153);
  color: white;
}
</style>
