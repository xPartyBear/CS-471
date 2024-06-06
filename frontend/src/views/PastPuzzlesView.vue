<script setup>
import pastPuzzles from '../../services/pastPuzzles.js'
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
      data() {
        return {
          puzzles: []
        }
      },
      mounted() {
        pastPuzzles.get_PastPuzzles().then(data => {
          data.data.forEach(puzzle => {
            const date = new Date(Date.parse(puzzle[0]));
            this.puzzles.push({
              year: date.getFullYear(),
              month: date.getMonth() + 1,
              day: date.getDate() + 1,
              date: `${date.getMonth() + 1}-${date.getDate() + 1}-${date.getFullYear()}`
            });
          });
        });
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

