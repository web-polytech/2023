<template>
  <section class="application">
    <h2>Электронная форма для подачи заявки заявления на поступление</h2>
    <TheForm action="/entrance" id="#form" class="application__form">
      <template #fields>
        <div class="application__form">
          <UIInput
            :label="`ФИО заявителя`"
            name="applicant"
            required
          />
          <UIInput
            :label="`ФИО ребенка`"
            name="child"
            required
          />
          <UISelect
            :label="`Страна`"
            :initial="`Выберите страну из списка`"
            :options="[
              `Россия`, `Белорусь`, `Казахстан`
            ]"
            name="country"
            required
          />
          <UISelect
            :label="`Город проживания`"
            :initial="`Выберите город из списка`"
            :options="[
              `Москва`, `Санкт-Петербург`, `Сочи`
            ]"
            name="city"
            required
          />
          <UIInput
            :label="`Дата рождения ребенка`"
            type="date"
            name="birth"
            required
          />
          <UIInput
            :label="`Свидетельство о рождении или паспорт ребенка`"
            type="file"
            name="birth-certificate"
            required
          />
          <UIInput
            :label="`Справка о состоянии здоровья формы 086у`"
            type="file"
            name="health-certificate"
            required
          />
          <UIInput
            :label="`Справка о группе здоровья`"
            type="file"
            accept="image/*,.pdf"
            name="health-group"
            required
          />
          <UISelect
            :label="`Класс для поступления`"
            :options="[
              `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`
            ]"
            placeholder="Выберите класс из списка"
            required="true"
            name="class"
          />

          <UISelect
            :label="`Специализация ребенка (с 8 класса)`"
            :placeholder="`Выберите специализацию из списка`"
            :options="[
              `Естественно-Научная`, `Гуманитарная`
            ]"
            name="specialization"
          />
          <UIInput
            :label="`Эссе ребенка о своих увлечениях (от 240 слов)`"
            type="file"
            name="essay"
            required
          />
          <UIInput
            :label="`Результаты тестирования`"
            type="file"
            name="testing-result"
            required
          />
          <UIInput
            :label="`Результаты вступительных экзаменов`"
            type="file"
            name="exams-result"
            required
          />
          <UITextarea
            :label="`Дополнительная информация`"
            placeholder="Введите дополнительную информацию"
            name="additional"
            rows="8"
          />
        </div>
      </template>
      <template #buttons>
        <div class="application__buttons">
          <UIInput
            :label="`Согласие на обработку персональных данных`"
            type="checkbox"
            name="data-processing"
            required
          />
          <UIButton type="submit">
            Отправить заявление
          </UIButton>
        </div>
      </template>
    </TheForm>
  </section>
</template>

<script setup>
import TheForm from '@/components/TheForm.vue';
import UITextarea from '../../../components/UI/UITextarea.vue';
</script>

<style lang="scss" scoped>
  .application {
    padding: 2rem;

    & > * {
      break-inside: avoid;
    }
  }

  .application__form {
    column-count: 2;
    column-gap: 3.2rem;
  }

  .application__buttons {
    display: flex;
    flex-direction: column;
    align-items: center;
  }


</style>

