<script setup>
import pokemon from '../../services/pokemon.js'
</script>

<template>
    <div class="content">
        <h1>This is the Past Puzzles page</h1>
        <div class="box-container" v-for="puzzle in puzzles">
            <div class="box"><RouterLink class="link" :to="'/'+puzzle.month+'/'+puzzle.day+'/'+puzzle.year"> Day: {{puzzle.date}}</RouterLink></div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                puzzles: []
            }
        },
        mounted(){
            const earliest = new Date(2024,4,30);
            let curDate = new Date();
            console.log(curDate + "\n" + earliest);
            while(curDate.getTime() >= earliest.getTime()){
                this.puzzles.push(
                    {
                        year: curDate.getFullYear(),
                        month: curDate.getMonth() + 1,
                        day: curDate.getDate(),
                        date: `${curDate.getMonth()+1}-${curDate.getDate()}-${curDate.getFullYear()}`
                    }
                );
                curDate.setDate(curDate.getDate()-1);
            }
        }

    }   
</script>


<style scoped>
    .content {
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        text-align: center;
    }
    .box {
        border: 1px solid #ddd;
        padding: 20px;
        margin: 5px;
        border-radius: 5px;
        background-color: #f9f9f9;
        min-width: 100%;
        cursor: pointer;
        user-select: none;
    }
    .box:hover {
        background-color: #cacaca;
    }
    .box-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .link {
        display: block; 
        text-decoration: none;
        user-select:none;
        color: black;
        margin: 0;
        height: 100%;
    }
</style>

