<template>
  <a v-if="link" class="button" :class="{'button--light':light, 'button--outline':outline}" :href="href"><slot /></a>
  <button v-else class="button" :class="{'button--light':light, 'button--outline':outline}">
    <slot />
  </button>
</template>


<script setup>
const props = defineProps({
  link: {
    type: String,
    default: '/',
  },
  light: {
    type: Boolean,
    default: false,
  },
  outline: {
    type: Boolean,
    default: false,
  },
  disable: {
    type: Boolean,
    default: false,
  },
});
</script>

<script>
export default {
  name: 'UIButton',
};
</script>


<style lang="scss">
  .button {
    width: fit-content;
    padding: 14px 50px;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 1.4rem;
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

  .button--outline {
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
