<template>
  <section class="application">
    <h2>Электронная форма для подачи заявки заявления на поступление</h2>
    <TheForm class="application__form">
      <template #fields>
        <TheInput
          :label="`ФИО заявителя`"
          class="application__input"
          :placeholder="undefined"
          :required="true"
        />
      </template>
      <template #buttons>
        <TheInput
          :label="`Согласие на обработку персональных данных`"
          class="application__input"
          :placeholder="undefined"
          :required="true"
        />
        <TheButton>Отправить заявление</TheButton>
      </template>
    </TheForm>
    <UIButton />
  </section>
</template>

<style lang="scss" scoped>
  .application {
    padding: 2rem;
  }

  .application__form {
    padding: 0;
  }

  .application__input {
    padding: 0;
  }

</style>

