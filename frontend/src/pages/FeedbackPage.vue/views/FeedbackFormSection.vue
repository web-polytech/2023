<template>
  <section class="feedback">
    <h2 class="visually-hidden">
      Форма обратной связи
    </h2>
    <TheForm class="feedback__form" action="/feedback">
      <template #fields>
        <UIInput
          :label="`Имя`"
          name="name"
          required
        />
        <UIInput
          :label="`Фамилия`"
          name="surname"
          required
        />
        <UISelect
          :label="`Тема сообщения`"
          :initial="`Выберите тему из списка`"
          :options="['Вопросы поступление', 'world']"
          name="topic"
        />
        <UITextarea
          :label="`Сообщение`"
          name="message"
          rows="10"
          required
        />
      </template>
      <template #buttons>
        <UIButton class="feedback__button">
          Отправить сообщение
        </UIButton>
      </template>
    </TheForm>
  </section>
</template>

<script setup>
import TheForm from '@/components/TheForm.vue';

</script>

<style lang="scss" scoped>
  .feedback {
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  .feedback__button {
    margin-block-start: 1rem;
    margin-inline-start: auto;
  }

  .feedback__form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
</style>
