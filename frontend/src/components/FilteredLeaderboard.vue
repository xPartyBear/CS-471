<script setup>
    import leaderboard from '../../services/leaderboard.js';
</script>

<template>
    <div>
        <h1>{{category}} Leaderboard</h1>
        <div v-if="failed">Leaderboard failed to load correctly</div>
        <div class="box-container" v-for="(element, index) in leaderboardData" :key="element">
            <div class="box"> {{index+1}}. {{element[0]}} - {{element[1]}} </div>
        </div>
    </div> 
</template>

<script>
    export default {
        props: ['category'],
        data(){
            return {
                failed: false,
                leaderboardData: []
            }
        },
        mounted(){
            this.get_leaderboard();
        },
        methods: {
            async get_leaderboard(){
                const res = await leaderboard.get_leaderboard(this.category);
                //console.log(res.data);
                if(res.data == null) {
                    this.failed=true;
                    this.leaderboardData = [];
                }
                this.failed = false;
                this.leaderboardData = res.data;   
            }
        },
    }
</script>

<style scoped>
    .box {
        border: 1px solid #ddd;
        padding: 20px;
        margin: 5px;
        border-radius: 5px;
        background-color: #f9f9f9;
        user-select: none;
        width: 50%;
    }
    .box-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>