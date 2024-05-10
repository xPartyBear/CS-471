<script setup>
    import PokedexImg from './../assets/pokedex.png' 
</script>


<template>
    <div class="container">
        <img :src="PokedexImg" style="width:1000px; display: block; margin: 0 auto">
        <table>
            <tr>
                <th :value="Type1">Type 1: ???</th>
                <th :value="Type2">Type 2: ???</th>
                <th>Abilities: ???/???</th>
            </tr>
            <tr>
                <th>Evolution Method: ???</th>
                <th>Evolution Stage: ???</th>
                <th>Height and Weight: ???/???</th>
            </tr>
            <tr>
                <th>Egg Type: ???</th>
                <th>Region Origin: ???</th>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                pokemonInfo: {
                    "Type1": "Electric",
                    "Type2": "None",
                    
                }
            }
        } 
    }
</script>

<style scoped>
    .container {
        max-width: 820px;
        width: 100%;
        background-color: lightblue;
        height: 320px;
        border-radius: 4px;
        position:relative;
        margin: auto;
        background-image: url('./../assets/pokedex.png' );
    }
    th {
        border: 1px solid black;
    }
</style>

