
<script>
export default {
  name: 'UISelect',
  inheritAttrs: false,
};
</script>

<template>
  <!-- eslint-disable vue/no-deprecated-slot-attribute -->
  <label class="field">
    <selectmenu
      class="field__selectmenu"
      v-if="browserSupport"
      v-bind="$attrs"
    >
      <button class="field__button" type="button" slot="button" behavior="button">
        <span class="field__selected" behavior="selected-value" slot="selected-value" />
        <svg class="field__icon" width="16" height="16" viewBox="0 0 16 16">
          <path d="M1 5 l7 7 L15 5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </button>
      <option selected="selected" style="display: none;" v-for="option in options" :key="option">
        {{initial}}
      </option>
      <option class="field__option" v-for="option in options" :key="option">
        {{option}}
      </option>
    </selectmenu>
    <select
      v-else
      class="field__select"
      v-bind="$attrs"
    >
      <option selected disabled style="display: none;" value="">
        {{initial}}
      </option>
      <option class="field__option" :key="option" :value="option" v-for="option in options">
        {{option}}
      </option>
    </select>
    <span class="field__label">
      {{label}}
    </span>
  </label>
</template>

<script setup>
import {ref, computed} from 'vue';

const input = ref('');

const browserSupport = computed(() => {
  return window.HTMLSelectMenuElement !== undefined;
});

defineProps({
  label: {
    type: String,
    default: '',
    required: true,
  },
  options: {
    type: Array,
    default: () => [],
    required: true,
  },
  initial: {
    type: String,
    default: '',
  },
});
</script>


<style lang="scss" scoped>

  $accent-dark: #33475b;

  .field  {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem;
  }

  .field__selectmenu {
    position: relative;
    min-height: 3rem;

    &[required] ~ .field__label::after {
      content: ' *';
      color: red;
    }

  }

  .field__button {
    position: absolute;
    inset: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
    color: var(--accent-gray);
    text-align: start;
    background-color: #F5F8FA;
    border: 1px solid #cbd6e2;
    appearance: none;
  }

  .field__icon {
    z-index: 2;
    width: 1rem;
    height: 1rem;
    color: $accent-dark;
  }

  .field__selected {
    z-index: 1;
    color: $accent-dark;
    font-size: 1.5em;
  }

  .field__option {
    color: red;
  }

  .field__select {
    min-height: 3rem;
    padding: 0.5rem 1rem;
    color: $accent-dark;
    font-size: 1.3em;
    background-color: #F5F8FA;
    border: 1px solid #cbd6e2;
    border-radius: 4px;
    appearance: none;

    &[required] ~ .field__label::after {
      content: ' *';
      color: red;
    }
  }

  .field__label {
    order: -1;
    font-size: 1.5em;
  }

</style>
