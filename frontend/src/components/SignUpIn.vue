<template>
    <div class="modal">
        <div @click="close()" class ="bg"></div>
        <div class="window">
            <h2 style="text-align: center;">Sign Up</h2>
        </div>
    </div>
</template>

<script>
    export default {
        methods: {
            close(){
                this.$emit('close');
            }
        }
    }
</script>

<style scoped>
    .modal {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        
    }
    .bg {
        background-color: gray;
        opacity: 50%;
        position: fixed;
        width: 100%;
        height: 100%;

        z-index: 2;

    }
    .window {
        z-index: 2;
        width: 35%;
        height: 35%;
        background-color: lightgray;
        position: absolute;
        left: 30%;
        top: 30%;
        border-radius: 16px;

    }
    .form {
        display: block;
    }
</style>