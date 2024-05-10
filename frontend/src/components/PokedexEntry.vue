<script setup>
    import PokedexImg from './../assets/pokedex.png' 
</script>


<template>
    <div class="container">
        <img class="bg" :src="PokedexImg" style="width:1000px; display: block; margin: 0 auto">
        <table class="table">
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
        background-color: lightblue;
        border-radius: 4px;
        position:relative;
        margin: auto;
    }
    th {
        border: 1px solid black;
    }
    .bg {
        position: absolute;
        z-index: -1;
    }
    
</style>

