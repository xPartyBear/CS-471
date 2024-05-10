<script setup>
  import PokemonSearch from '../components/PokemonSearch.vue';
  import PopupBox from '../components/PopupBox.vue';
  import PokedexEntry from '../components/PokedexEntry.vue';
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
    
    <PokedexEntry></PokedexEntry>
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
        console.log("TEST");
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
