<script setup>
import leaderboard from '../../services/leaderboard.js'
</script>

<template>
    <div>
        <h1>{{category}} Leaderboard</h1>
        <div v-if="failed">Leaderboard failed to load correctly</div>
        <div class="box-container" v-for="element in leaderboard">
            <div class="box"> {{element}} </div>
        </div>
    </div> 
</template>

<script>
    export default {
        props: ['category'],
        data(){
            return {
                failed: false
            }
        },
        methods: {
            async leaderboard(){
                const res = await leaderboard.get_leaderboard(this.category);
                if(res.data == null) {
                    this.failed=true;
                    return []
                }
                this.failed = false;
                return res.data;   
            }
        },
    }
</script>