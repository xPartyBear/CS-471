<template>
  <div class="modal">
    <div @click="close()" class="bg"></div>
    <div class="window">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  methods: {
    close() {
      this.$emit('close')
    }
  }
}
</script>

<style scoped>
    .window {
        z-index: 3;
        width: 35%;
        height: auto;
        background-color: rgb(255, 220, 220);
        border: solid rgb(156,100,100) 4px;
        position: absolute;
        display: table;
        left: 30%;
        top: 30%;
        border-radius: 16px;
        box-shadow: 0px 4px 4px 0px gray;
    }
    .bg {
        background-color: gray;
        opacity: 50%;
        position: fixed;
        width: 100%;
        height: 100%;

      z-index: 3;
}
.modal {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 3;
}
</style>
