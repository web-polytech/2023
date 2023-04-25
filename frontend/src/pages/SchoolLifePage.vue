<template>
  <section class="promo">
    <h1 class="promo__heading">Школьная жизнь</h1>
    <p class="promo__decsription">Создаем условия для активного и здорового образа жизни, способствуем культурному и творческому развитию и позволяем преобретать навыки</p>
  </section>
  <section class="section">
    <h2 class="section__heading">Школьные объединения</h2>
    <ul class="section__list">
      <li class="section__card">
        <div class="clubs-card">
          <div class="clubs-card__content">
            <img src="../assets/images/SchoolLifeClubsCard1.webp" alt="Image for clubs">
            <h3 class="clubs-card__name">Юношеско-подростковый клуб волонтеров “Юный активист”</h3>
            <p class="clubs-card__text">Мы занимаемся волонтерством, экоактивизмом, помогаем детям и животным, а так же участвуем в различных мероприятиях.</p>
          </div>
        </div>
      </li>
    </ul>
  </section>
  <section class="section">
    <h2 class="section__heading">Спортивные секции</h2>
    <ul class="section__list">
      <li class="section__card">

      </li>
    </ul>
  </section>
  <section class="section">
    <h2 class="section__heading">Лекции и курсы в Нашей школе <span class="section__heading_blue">(new)</span></h2>
    <ul class="section__list">
      <li class="section__card">

      </li>
    </ul>
  </section>
</template>

<script>

</script>

<style lang="scss">
  .promo {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 100%;
    max-height: 100%;
    padding: 0;
    background-image: url("../assets/images/SchoolLifePagePromo.webp");
  }

  .promo__heading {
    margin: 20px auto;
    color: #ffffff;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
  }

  .promo__decsription {

  }

  .section {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .section__heading {
    margin: 60px auto;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .section__heading_blue {
    color: #1333AB;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
  }

  .section__list {
    list-style: none;
  }
</style>
