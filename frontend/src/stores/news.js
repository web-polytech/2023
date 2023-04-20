import {defineStore} from 'pinia';
import axios from 'axios';

export const useNewsStore = defineStore('news', {
  state: ()=>{
    return {news: []};
  },
  actions: {
    async getNews() {
      try {
        const response = await axios.get(`https://mocki.io/v1/04c63688-0336-4ec6-92dc-09b1c3a2f0ab`);
        this.news = response.data;
      } catch (error) {
        alert(error);
      }
    },
  },
  getters: {
    allNews(state) {
      return state.news;
    },
  },
});
