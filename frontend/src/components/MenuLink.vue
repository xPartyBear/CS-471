<template>
    <div class="button">
        <img :src="icon"/>
        <div class="content">
            <slot></slot>
        </div>
    </div>
</template>

<script>
    export default {    
        name: 'MenuLink',
        props: ['icon'],
        data(){

        }

    }
</script>

<style scoped>
    .button {
        border: none;
        text-decoration: none;
        background-color: lightgray;
        width : 100%;
        height:64px;
        display: flex;
    }
    .button:hover {
        background-color: gray;
        transition : all 0.3s ease;
        cursor: pointer;
    }
    .content {
        display: inline-block;
        width:100%;
        height:64px;
    }

</style>

