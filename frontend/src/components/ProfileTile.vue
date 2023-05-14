<template>
  <RouterLink class="tile" :class="{'tile--disactive': tile.active==false}" :to="tile.link">
    <div v-if="tile.count > 0" class="tile__badge">
      <p class="tile__count">{{tile.count}}</p>
    </div>
    <img class="tile__icon" :src="'src/assets/icons/'+tile.icon+'.svg'">
    <p class="tile__title">{{tile.title}}</p>
  </RouterLink>
</template>
<script setup>

defineProps({
  tile: {
    type: Object,
    default: NaN,
  },
});
</script>

<style lang="scss">
  .tile {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 12px;
    width: 140px;
    height: 140px;
    padding-top: 34px;
    padding-bottom: 14px;
    background-color: #F5F8FA;
    border-radius: 6px;
  }

  .tile__icon {
    height: 49px;
  }

  .tile__badge {
    position: absolute;
    top: 8px;
    right: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 24px;
    height: 24px;
    background-color: #1333AB;
    border-radius: 50%;
  }

  .tile__count {
    color: #FFFFFF;
    font-weight: 700;
    font-size: 0.9rem;
    line-height: 1;
    text-decoration: none;
  }

  .tile__title {
    color: #000000;
    font-weight: 400;
    font-size: 1.2rem;
    line-height: 1;
    text-align: center;
    text-decoration: none;
  }
</style>
