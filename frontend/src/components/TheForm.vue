<script setup>
import TheButton from '../components/UI/UIButton.vue';

</script>

<template>
  <form action="">
    <slot name="fields" />
  </form>
  <slot name="button" />
</template>


<style lang="scss" scoped>
  form {
    color: red;
  }
</style>
