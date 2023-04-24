<template>
  <RouterLink class="button" :class="{'button--light': type=='light', 'button--border': type=='border'}" :to="path">{{label}}</RouterLink>
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
    width: fit-content;
    padding: 14px 50px;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 1.5rem;
    text-decoration: none;
    background-color: #1C52A2;
    box-shadow: 0 0 10px rgb(0 0 0 / 10%), 0 0 5px rgb(0 0 0 / 10%);
    transition: background-color 150ms ease-in-out;


    &:hover {
      background-color: #0C3777;
    }
  }

  .button--light {
    color: #1C52A2;
    background-color: #FFFFFF;
    transition: all 150ms ease-in-out;

    &:hover {
      color: #FFFFFF;
      background-color: #0C3777;
    }
  }

  .button--border {
    padding: 11px 50px;
    color: #1C52A2;
    background-color: transparent;
    border: 3px solid #1C52A2;
    transition: all 150ms ease-in-out;

    &:hover {
      color: #FFFFFF;
      background-color: #1C52A2;
    }
  }
</style>
