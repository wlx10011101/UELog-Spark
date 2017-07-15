<template>
  <div class="x-bar">
    <div :id="id" :option="option"></div>
  </div>
</template>

<script>
	import HighCharts from 'highcharts'
	import bus from '@/assets/scripts/eventBus'
	export default {
	  data(){
	  	return {
	  		chart: null
	  	}
	  },
	  // 验证类型
	  props: {
	    id: {
	      type: String
	    },
	    option: {
	      type: Object
	    }
	  },
	  mounted() {
	    this.chart = HighCharts.chart(this.id,this.option);
	    let self = this
	    bus.$on("toggleFullWidth", function(msg){
	    	setTimeout(function(){
	    		self.chart.reflow()
	    	},410)
	    });
	  },
	}
</script>

<style type="text/css">
	
</style>