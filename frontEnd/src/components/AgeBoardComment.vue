<template>
  <div class="comments">
    <h5>댓글 목록</h5>
    <ul v-if="ageComments">
      <li v-for="comment in ageComments" :key="comment.id" class="comment-item">
        <p>{{ comment.user.username }} : {{ comment.content }}</p>
        <button v-if="comment.user.username === userStore.userId" @click="deleteComment(comment.id)">삭제</button>
      </li>
    </ul>
    <p v-else>댓글이 없습니다!</p>
    <CreateComment @comment-added="fetchComments" />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'
import { useRoute } from 'vue-router'
import CreateComment from '@/components/AgeBoardCreateComment.vue'

const userStore = userCheckStore()
const store = useBoardStore()
const route = useRoute()

const ageComments = ref(null)

const fetchComments = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/boards/age/${route.params.id}`,
    headers: {
      Authorization: `Token ${userStore.token}` 
    }
  })
    .then((res) => {
      // console.log(res.data.age_comment)
      ageComments.value = res.data.age_comment
    })
    .catch((err) => {
      console.log(err)
    })
}

onMounted(() => {
  fetchComments()
})

const deleteComment = (commentId) => {
  if (confirm('정말로 이 댓글을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/boards/age/comments/${commentId}`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then(() => {
        alert('댓글이 삭제되었습니다.')
        fetchComments()
      })
      .catch((err) => {
        console.log(err)
        alert('댓글 삭제에 실패했습니다.')
      })
  }
}
</script>

<style scoped>
.comments {
  margin-top: 20px;
}

.comment-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

button {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  /* background-color: #dc3545; */
  color: black;
  cursor: pointer;
}

button:hover {
  background-color: #e7707c;
}
</style>
