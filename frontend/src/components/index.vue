<template>
  <div class="welcome">
    <h1>{{ msg }}</h1>
  </div>
</template>
 
<script>
export default {
  name: 'welcome',
  data () {
    return {
      msg: '欢迎来到深塔'
    }
  }
}
</script>