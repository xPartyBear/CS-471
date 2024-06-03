<script setup>
import Leaderboard from "../components/Leaderboard.vue";

</script>

<template>
    <div>
        <br>
        <div class="header">
            <button @click="swapView(1)">Daily</button>
            <button @click="swapView(2)">Weekly</button>
            <button @click="swapView(3)">Yearly</button>
            <button @click="swapView(4)">Lifetime</button>
            <button @click="swapView(5)">Streak</button>
        </div>


        <div class="content" v-if="leaderboardType==1">
            <h1>Daily</h1>
            <div class="box-container">
                <div class="box" v-text="daily.first"></div>
                <div class="box" v-text="daily.second"></div>
                <div class="box" v-text="daily.third"></div>
                <div class="box" v-text="daily.fourth"></div>
                <div class="box" v-text="daily.fifth"></div>
            </div>
        </div>
        <div class="content" v-if="leaderboardType==2">
            <h1>Weekly</h1>
            <div class="box-container">
                <div class="box" v-text="weekly.first"></div>
                <div class="box" v-text="weekly.second"></div>
                <div class="box" v-text="weekly.third"></div>
                <div class="box" v-text="weekly.fourth"></div>
                <div class="box" v-text="weekly.fifth"></div>
            </div>
        </div>
        <div class="content" v-if="leaderboardType==3">
            <h1>Yearly</h1>
            <div class="box-container">
                <div class="box" v-text="yearly.first"></div>
                <div class="box" v-text="yearly.second"></div>
                <div class="box" v-text="yearly.third"></div>
                <div class="box" v-text="yearly.fourth"></div>
                <div class="box" v-text="yearly.fifth"></div>
            </div>
        </div>
        <div class="content" v-if="leaderboardType==4">
            <h1>Lifetime</h1>
            <div class="box-container">
                <div class="box" v-text="lifetime.first"></div>
                <div class="box" v-text="lifetime.second"></div>
                <div class="box" v-text="lifetime.third"></div>
                <div class="box" v-text="lifetime.fourth"></div>
                <div class="box" v-text="lifetime.fifth"></div>
            </div>
        </div>
        <div class="content" v-if="leaderboardType==5">
            <Leaderboard category="streaks"></Leaderboard>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            leaderboardType: 1,
            daily: {
                first: 1,
                second: 2,
                third: 3,
                fourth: 4,
                fifth: 5
            },
            weekly: {
                first: 1,
                second: 2,
                third: 3,
                fourth: 4,
                fifth: 5
            },
            yearly: {
                first: 1,
                second: 2,
                third: 3,
                fourth: 4,
                fifth: 5
            },
            lifetime: {
                first: 1,
                second: 2,
                third: 3,
                fourth: 4,
                fifth: 5
            },
            streak: {
                first: 1,
                second: 2,
                third: 3,
                fourth: 4,
                fifth: 5
            }
        }
    },
    methods: {
        swapView(type) {
            this.leaderboardType=type;
        }
    }
}
</script>

<style scoped>
    body {
        font-family: Arial, sans-serif;
    }
    .header {
        display: flex;
        justify-content: center;
        padding: 10px;
        background-color: #f8f8f8;
        border-bottom: 1px solid #ddd;
    }
    .header button {
        margin: 0 10px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        border: none;
        background-color: #007bff;
        color: white;
        border-radius: 5px;
    }
    .header button:hover {
        background-color: #0056b3;
    }
    .content {
        text-align: center;
    }
    .box {
        border: 1px solid #ddd;
        padding: 20px;
        margin: 5px;
        border-radius: 5px;
        background-color: #f9f9f9;
        cursor: pointer;
        user-select: none;
    }
    .box-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>