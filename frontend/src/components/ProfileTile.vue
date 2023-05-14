<template>
  <RouterLink class="tile" :class="{'tile--disactive': tile.active==false}" :to="tile.link">
    <div class="tile__badge">
      <p v-if="tile.count > 0" class="tile__count">{{tile.count}}</p>
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

<!-- <style lang="scss">

</style> -->
