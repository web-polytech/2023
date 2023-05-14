<template>
  <section class="cover-block">
    <div class="cover-block__wrapper">
      <div class="cover-block__badge">
        <p class="cover-block__badge-text cover-block__class">
          10 А класс
        </p>
      </div>
      <div class="cover-block__badge">
        <p class="cover-block__badge-text cover-block__status">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="8" cy="8" r="8" fill="#1CCD18" />
            <circle cx="8" cy="8" r="5" fill="#1CCD18" stroke="white" stroke-width="2" />
          </svg>
          В сети
        </p>
      </div>
      <div class="cover-block__avatar">
        <img src="/src/assets/images/profile-avatar01.webp" alt="" class="cover-block__image">
      </div>
    </div>
  </section>
</template>

<script>

export default {
  components: {
  },
  data() {
    return {

    };
  },
  methods: {
    replaceString(text) {
      let unionsAndPrepositions = ['так что', 'дабы', 'с тем чтобы', 'несмотря на то', 'хоть', 'пускай', 'хотя', 'если', 'если бы', 'коли', 'ежели', 'так как', 'потому что',
        'как будто', 'словно', 'точно', 'как', 'как бы', 'до такой степени', 'настолько', 'до того', 'такой', 'где', 'куда', 'откуда', 'когда', 'что', 'то есть',
        'а именно', 'и', 'да', 'не только', 'но и', 'также', 'тоже', 'и', 'ни', 'как', 'так', 'сколько', 'столько', 'или', 'либо', 'то', 'ли', 'не', 'то', 'а',
        'зато', 'однако', 'же', 'все же', 'чтобы', 'чтоб', 'притом', 'причём', 'в', 'без', 'до', 'из', 'к', 'на', 'по', 'о', 'от', 'перед', 'при', 'через', 'с', 'со', 'у',
        'и', 'нет', 'за', 'над', 'для', 'об', 'под', 'про'];

      for (let str of unionsAndPrepositions) {
        if (text.includes(' ' + str + ' ')) {
          text = text.replace(' ' + str + ' ', ' ' + str + String.fromCharCode(160));
        }
      }
      return text;
    },
  },
};
</script>

<style lang="scss">

  .cover-block__wrapper {
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 0 0 40px;

    @media screen and (width <= 786px){
      display: flex;
      flex-direction: column;
      padding: 0;
    }
  }

  .cover-block__title {
    font-weight: 700;
    font-size: 3.2rem;
    font-family: 'PT Serif', sans-serif;
    line-height: 1;
  }
</style>
