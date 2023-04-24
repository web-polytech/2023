<template>
  <section class="dates">
    <h2 class="dates__heading">
      График подачи и рассмотрения заявок
    </h2>
    <ul class="dates__list">
      <li class="dates__item">
        <img class="dates__icon" src="@/assets/images/EntranceIcon1.svg" alt="">
        <div class="dates__text-info">
          <span class="dates__text">
            форма для подачи заявления на&nbsp;поступление открыта
          </span>
          <h3 class="dates__date">
            до 30 сентября
          </h3>
        </div>
      </li>
      <li class="dates__item">
        <img class="dates__icon" src="@/assets/images/EntranceIcon2.svg" alt="">
        <div class="dates__text-info">
          <span class="dates__text">
            анализ заявок на&nbsp;поступление и&nbsp;отбор претендентов
          </span>
          <h3 class="dates__date">
            до 21 ноября
          </h3>
        </div>
      </li>
      <li class="dates__item">
        <img class="dates__icon" src="@/assets/images/EntranceIcon3.svg" alt="">
        <div class="dates__text-info">
          <span class="dates__text">
            проверка документов и&nbsp;рассылка ответов с&nbsp;результатами отбора
          </span>
          <h3 class="dates__date">
            до 1 февраля
          </h3>
        </div>
      </li>
    </ul>
  </section>
</template>
<style scoped lang="scss">

  .dates {
    max-width: 1650px;
    inline-size: 100vw;
    margin-inline-start: 50%;
    transform: translateX(-50%);
  }

  .dates__list {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    list-style: none;
  }

  .dates__item {
    display: flex;
    align-items: center;
    padding: 0.63em 1.25rem;
    background-color: var(--accent-gray);
  }

  .dates__icon {
    padding: 0;
  }

  .dates__text-info {
    margin-bottom: -.8rem;
    padding-block: 1rem;
    text-align: center;
  }

  .dates__text {
    font-size: 1.5em;
    line-height: 1;
  }

  .dates__date {
    padding: 0;
    color: var(--accent-blue);
    font-size: 2.25em;
    text-justify: bottom;
  }

</style>
