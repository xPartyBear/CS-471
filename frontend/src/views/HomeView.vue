<script setup>
  import PokemonSearch from '../components/PokemonSearch.vue';
  import PopupBox from '../components/PopupBox.vue';
  import PokedexEntry from '../components/PokedexEntry.vue';
</script>

<template>
  <div class = "Home">
    <h1>This is the home page</h1>
    <PokemonSearch @guess=""></PokemonSearch>
    <br>
    <p>This is just a test to see how this looks</p>
    <PopupBox v-if="displaySharePopup" @close="toggleShare()">
      This is the popup box for sharing...
      <br>
      Create a new componenent file to put the share content in here
    </PopupBox>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
  .Home {
    margin-left: auto;
    margin-right: auto;
    width: 50%
  }
</style>
