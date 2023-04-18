<template>
  <ul class="submenu">
    <li class="submenu__item">
      <RouterLink class="submenu__link" to="/">Главная</RouterLink>
    </li>
    <li class="submenu__item">
      <RouterLink class="submenu__link" to="/about">О&nbsp;школе</RouterLink>
    </li>
    <li class="submenu__item">
      <RouterLink class="submenu__link" to="/entrance">Поступление</RouterLink>
    </li>
    <li class="submenu__item">
      <RouterLink class="submenu__link" to="/news">Новости</RouterLink>
    </li>
    <li class="submenu__item">
      <RouterLink class="submenu__link" to="/school-life">Школьная жизнь</RouterLink>
    </li>
    <li class="submenu__item">
      <RouterLink class="submenu__link" to="/advances">Достижения</RouterLink>
    </li>
    <li class="submenu__item">
      <RouterLink class="submenu__link" to="/contacts">Контакты</RouterLink>
    </li>
  </ul>
</template>
<script>

</script>
<style lang="scss">
  .submenu {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 38px;
    max-height: 46px;
    padding: 14px 0;
    list-style: none;
    background-color: #FFFFFF;
    box-shadow: 0 1px 4px rgb(0 0 0 / 25%);

    @media screen and (width <= 892px) {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 1px;
      max-height: fit-content;
      padding: 0;
      overflow: hidden;

      & .submenu__item {
        padding: 10px;
        text-align: center;
        box-shadow: 0 0 0 1px #f0f0f0;
      }
    }
  }


  .submenu__link {
    color: #000000;
    font-size: 1.2rem;
    line-height: 1.2;
    text-decoration: none;
  }

</style>
