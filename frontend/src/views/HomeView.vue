<script setup>
  import PokemonSearch from '../components/PokemonSearch.vue';
  import PopupBox from '../components/PopupBox.vue';
<<<<<<< HEAD
  import PokedexEntry from '../components/PokedexEntry.vue';
=======
  import PokedexImg from './../assets/pokedex.png'
>>>>>>> 7604c895d7bc961d65e9a9045bcb9160ba6522dd
</script>

<template>
  <div class = "Home">
    <h1>This is the home page</h1>
    <PokemonSearch @guess="guess()"></PokemonSearch>
    <br>
    <br>
    <PopupBox v-if="displaySharePopup" @close="toggleShare()">
      This is the popup box for sharing...
      <br>
      Create a new componenent file to put the share content in here
    </PopupBox>
<<<<<<< HEAD
    <PokedexEntry></PokedexEntry>
=======
    <img :src="PokedexImg" style="width:1000px; display: block; margin: 0 auto">
>>>>>>> 7604c895d7bc961d65e9a9045bcb9160ba6522dd
  </div>
</template>

<script>
export default {
    data(){
      return {
        displaySharePopup: false
      }
    },
    methods: {
      toggleShare(){
        //For now this is what it will do
        this.displaySharePopup = !this.displaySharePopup;
        return;
      },
      guess(){
        console.log("THis is a testy");
        //Call guesses here to check if they are correct
        this.toggleShare();
        return;
      }
    }
}
</script>

<style scoped>
  .Home {
    margin-left: auto;
    margin-right: auto;
    width: 50%
  }
</style>
