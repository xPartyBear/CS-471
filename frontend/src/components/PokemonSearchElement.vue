<template>
  <div class="container">
    <img class="icon" :src="iconSrc" />
    <div class="content"><slot></slot></div>
  </div>
</template>

<script>
export default {
  props: ['pokemonImg'],
  name: 'PokemonSearchElement',
  computed: {
    iconSrc() {
      return this.pokemonImg != null ? this.pokemonImg : '../../public/favicon.ico'
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  .icon {
    width: 32px;
    height: 32px;
  }
  .content {
    padding-left: 10%;
  }
}
</style>
