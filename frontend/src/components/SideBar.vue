<template>
  <div class="SideBarContainer">
    <transition>
      <div class="sideBar" v-if="openedTab">
        <div v-if="openedTab" class="tab open" @click="toggleTab">
          <img :src="imgSrc" />
        </div>
        <div style="display: block">
          <div class="title">
            {{ title }}
          </div>
          <br />
          <br />
          <br />
          <br />
          <div class="content">
            <!--This is the interior content of the side bar-->
            <slot></slot>
          </div>
        </div>
      </div>
    </transition>
    <div class="tab" @click="toggleTab">
      <img :src="imgSrc" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
  props: ['imgSrc', 'title'],
  data() {
    return {
      openedTab: false,
      sideBarState: ''
    }
  },
  methods: {
    toggleTab() {
      this.openedTab = !this.openedTab
      this.sideBarState = this.openedTab ? 'open' : ''
    }
  }
}
</script>

<style scoped>
    .tab{
        float : right;
        background: rgb(255, 220, 220);
        border-left: solid rgb(156,100,100) 4px;
        border-top: solid rgb(156,100,100) 4px;
        border-bottom: solid rgb(156,100,100) 4px;
        box-shadow: 5px 5px 5px rgb(156,100,100);
        width: 64px;
        height: 64px;
        top:0px;
        right:0px;

        position: fixed;
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
    }
    .tab:hover {
        cursor: pointer;
    }
    .sideBar {
        display: flex;
        direction: column;
        height: 100%;
        background-color: rgb(255, 220, 220);
        border-left: solid rgb(156,100,100) 4px;
        border-bottom: solid rgb(156,100,100) 4px;
        position: fixed;
        right:0;
        top: 0;
        z-index: 1;
        width: 25%;
        border-bottom-left-radius: 16px;
    }
    .open {
        right: 100%;
        position: absolute;
    }
    .content {
        margin: 0;
        position: absolute;
        width: 100%;
    }
    .title {
        position: absolute;
        width: 100%;
        height: 64px;
        background-color: rgb(255, 220, 220);
        border-top: solid rgb(156,100,100) 4px;
        border-right: solid rgb(156,100,100) 4px;
        border-bottom-right-radius: 16px;
        font-family: 'Arial', 'Franklin Gothic Medium', 'Arial Narrow', sans-serif;
        font-weight: bold;
        font-size: 20px;
        padding: 21px 0;
    }
    .footer {
        bottom: 0;
        position: fixed;
        padding: 8px;
        width: 100%;
        background-color: lightgray;
        border-bottom-left-radius: 8px;
        height:64px
    }

.v-enter-active,
.v-leave-active {
  transition: right 0.5s ease-in-out;
}
.v-enter-from {
  right: -25%;
}
.v-leave-to {
  right: -25%;
}

img {
  padding: 8px;
}
</style>
