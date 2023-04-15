<template>
  <body>
    <h1>Главные новости</h1>
  </body>
  <NewsCard
        imageSrc="./Rectangle 4.png"
        title="Наука & технологии"
        tagline="1 сентября прошла торжественная церемония, посвященная началу учебного года в Нашей школе"
        text="Более 1200 учащихся пошло в Нашу школу в 2022 году, среди которых 210 первоклассников посетили свой первый урок. Восьмые классы теперь начнут учебы по выбранным специальностям, а для 11 классов этот год станет решающим и определяющим их будущее. Мы спросили у учащихся о том, готовы ли они к новому учебному году."
      />

</template>


<script>
import NewsCard from "@/components/NewsCard.vue";

export default {
  name: "NewsPage",
  components: {
    NewsCard,
  },
};
</script>

<style lang="scss" scoped>
body {
  display: flex;
  justify-content: center;
  align-items: center;
}
h1 {
  font-family: 'PT Sans';
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 100%;
}

</style>
