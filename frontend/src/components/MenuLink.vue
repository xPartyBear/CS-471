<template>
  <div class="button">
    <img :src="icon" />
    <div class="content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuLink',
  props: ['icon'],
  data() {}
}
</script>

<style scoped>
    .button {
        border: none;
        text-decoration: none;
        background-color: rgb(255, 220, 220);
        font-family: 'Arial', 'Franklin Gothic Medium', 'Arial Narrow', sans-serif;
        font-weight: bold;
        font-size: 20px;
        width : 100%;
        height: 64px;
        display: flex;
    }
    .button:hover {
        background-color: white;
        transition : all 0.3s ease;
        cursor: pointer;
    }
    .content {
        position: relative;
        padding: 21px 0;
        width:100%;
        height:64px;
        float: right;
    }

</style>
