<template>
  <div> 
    <Navigation></Navigation>
    <Sidebar></Sidebar>
    <div class="main" v-bind:class="{'full-width': isFullWidth}">
      <!-- <Chart></Chart> -->
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import Sidebar from '@/components/Sidebar'
  import Navigation from '@/components/Navigation'
  import Chart from '@/components/Chart'
  import bus from "@/assets/scripts/eventBus";
  export default {
    name: 'app',
    components: {
      Sidebar,
      Navigation,
      Chart,
    },
    data() {
      return {
        isFullWidth: false
      }
    },
    mounted: function(){
        let self = this
        bus.$on("toggleFullWidth", function(msg){
          self.isFullWidth = ! self.isFullWidth;
        });
      },
  }
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.main.full-width {
  width: 100%;
}
</style>
