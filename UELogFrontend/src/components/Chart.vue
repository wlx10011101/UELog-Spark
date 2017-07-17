<template>
	<div id="test">
		<!-- <highcharts ref="DL_Peak_Throughput" :options="option"></highcharts>
		<highcharts ref="UL_Peak_Throughput" :options="option"></highcharts>
		<highcharts ref="UL_Attenuation" :options="option"></highcharts> -->
		<!-- <highcharts ref="1" :options="options"></highcharts>
		<highcharts ref="2" :options="options"></highcharts> -->
		<!-- <highcharts v-for="map in chartMap" ref="index" :options="option"></highcharts> -->

		<highcharts ref="chartView" v-for="value, index in chartMap" :options="option"></highcharts>
		 
	</div>

</template>

<script>
	import bus from '@/assets/scripts/eventBus';
	import highcharts from '@/components/VueHighcharts';
	import {chartMap} from '@/assets/scripts/chartMap.js';
	import $ from 'jquery';
	export default {
		data() {
			return {
				chartMap: chartMap,
				isFullWidth: false,
				option: {
			        chart: {
			            type: 'spline',
			            zoomType: 'xy'
			        },
			        title: {
			            text: null
			        },
			        // subtitle: {
			        //     text: '非规律性时间内的变化'
			        // },
			        xAxis: {
			            type: 'datetime',
			            title: {
			                text: null
			            }
			        },
			        yAxis: [
				        {
				        	labels: {
				        		format: '{value}'
				        	},
				            title: {
				                text: null
				            },
				        },
				        {
				        	labels: {
				        		format: '{value} kbps'
				        	},
				        	title:{
				        		text: 'Throughput'
				        	},
				        	opposite: true

				        }
			        ],

			        tooltip: {
			            headerFormat: '<b>{series.name}</b><br>',
			            pointFormat: '{point.x:%e. %b}: {point.y:.2f}',
			        },
			        plotOptions: {
			            spline: {
			                marker: {
			                    enabled: true
			                }
			            }
			        },
			        series:[]
			     //    series: [{
			     //        name: '2007-2008 冬',
			     //        // Define the data points. All series have a dummy year
			     //        // of 1970/71 in order to be compared on the same x axis. Note
			     //        // that in JavaScript, months start at 0 for January, 1 for February etc.
			     //        data: []
			    	// },]
				},
			}
		},
		
		components:{
			highcharts,
		},
		mounted: function() {
			let self = this;
			
			this.$http.get('api/user/wlx/test1/testCT3_result.json?op=OPEN&namenoderpcaddress=10.9.171.160:9000&offset=0').then(function(res){
					let data = JSON.parse(res.bodyText);
					let result = format(data);
					let index = 0
					for(let key in chartMap){
						let dataSerial = [];
						for(let i=0; i<chartMap[key].length; i++)
						{
							let chartMapKey = chartMap[key][i];
							dataSerial.push({
								name: chartMapKey,
								data: result[chartMapKey],
								yAxis: 0
							})
							if(chartMapKey.match(/.*\(kbps\)$/g)){
								dataSerial[dataSerial.length-1]['yAxis'] = 1;
							}
						}
						// console.log(self.$refs )
						// console.log(key)
						// console.log(self.$refs[key])
						let lintcharts = self.$refs.chartView[index];
						lintcharts.setTitle({text: key});
						console.log(dataSerial)
						for (let i=0;  i < dataSerial.length; i++){
							lintcharts.addSeries(dataSerial[i])
						}
						index ++;
					}
					bus.$emit("updateChart", "updateChart");
					// for(let key in result) {
					// 	dataSerial.push({
					// 		name: key,
					// 		data: result[key],
					// 		yAxis: 0
					// 	})
						
					// 	if(key.match(/.*\(kbps\)$/g)){
					// 		dataSerial[dataSerial.length-1]['yAxis'] = 1;
					// 	}
					// }

					// let lintcharts = this.$refs.child;
					// for (let i=0; i<3; i++) {
					// 	lintcharts.addSeries(dataSerial[i])
					// }

				}, function(){});
			// format();
		}
	};
function format(data){
	var resultDict = {}
	for(let code in data){
		for(let yKey in data[code]){
			var ydatalist = []
			for(let yIndex in data[code][yKey]){
				ydatalist.push(
					[new Date(data[code][yKey][yIndex][1].split('.')[0]).getTime(), 
					data[code][yKey][yIndex][0]]);
			}
		resultDict[yKey] = ydatalist;
		}
	}
	return resultDict;
}
</script>

<style>

</style>
