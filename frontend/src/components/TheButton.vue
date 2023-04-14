<template>
  <RouterLink class="button" :to="path">{{label}}</RouterLink>
</template>
<script setup>
defineProps({
  label: {
    type: String,
    default: '',
  },
  path: {
    type: String,
    default: '#',
  },
  type: {
    type: String,
    default: 'default',
  },
  disable: {
    type: Boolean,
    default: false,
  },
});
</script>

<style land="scss">
  .button {
    padding: 14px 50px;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 1.4rem;
    text-decoration: none;
    background-color: #1C52A2;
    box-shadow: 0 0 10px rgb(0 0 0 / 10%), 0 0 5px rgb(0 0 0 / 10%);
    transition: background-color 150ms ease-in-out;

    &:hover {
      background-color: #0C3777;;
    }
  }
</style>
