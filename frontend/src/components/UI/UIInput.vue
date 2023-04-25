<script>
export default {
  name: 'UIInput',
  inheritAttrs: false,
};
</script>

<template>
  <label class="field" :class="`field--${$attrs.type}`">
    <input
      v-bind="$attrs"
      class="field__input"
      :class="`field__input--` + type"
    >
    <span
      class="field__label"
      :class="[`field__label--${$attrs.type}`, {'visually-hidden': !label}]"
    >
      {{label}}
    </span>
  </label>
</template>

<script setup>
defineProps({
  label: {
    type: String,
    default: '',
    required: true,
  },
  modalValue: {
    type: String,
    default: '',
  },
});
</script>


<style lang="scss" scoped>
  .field  {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem;

    &--checkbox, &--radio {
      flex-direction: row;
      gap: 1rem;
      margin-top: 1rem;
    }

  }

  .field__input {
    min-height: 3rem;
    padding: 0.5rem;
    font-size: 1.3em;
    background-color: #F5F8FA;
    border: 1px solid #cbd6e2;
    border-radius: 4px;

    &--checkbox, &--radio {
      min-height: initial;
      accent-color: var(--accent-gray);
      border: 0;
    }

    &--file::file-selector-button {
      border: none;
      border-radius: 4px;
    }

    &--file::-webkit-file-upload-button:hover {
      max-width: 50px;
      background-color: #81ecec;
      border: 2px solid #00cec9;
    }

    &[required] ~ .field__label::after {
      content: ' *';
      color: red;
    }
  }

  .field__label {
    order: -1;
    font-size: 1.5em;

    &--checkbox, &--radio {
      order: 0;
    }

  }

</style>

