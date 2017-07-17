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
	    bus.$on("updateChart", function(msg){
	    	this.redraw();
	    });
	  },
	  methods:{
	  	redraw: function() {
	  		console.log("redraw");
	  		this.chart.update(this.option);
	  	},

	  	setSeries: function(seriesData) {
	  		for (let i=0; i< seriesData.length; i++) {
	  			this.chart.series[0].addData(seriesData[i])
	  		}
	  	}
	  }
	}
</script>

<style type="text/css">
	
</style>