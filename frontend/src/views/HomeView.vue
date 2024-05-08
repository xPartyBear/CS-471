<script setup>
  import PokemonSearch from '../components/PokemonSearch.vue';
</script>

<template>
  <div class = "Home">
    <h1>This is the home page</h1>
    <PokemonSearch @guess=""></PokemonSearch>
    <br>
    <p>This is just a test to see how this looks</p>
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
