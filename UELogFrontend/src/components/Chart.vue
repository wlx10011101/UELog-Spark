<template>
	<div>
		<div v-show="isLoading==1">
			<highcharts ref="chartView" v-for="value, index in chartMap" :options="option"></highcharts>
		</div>

		<div v-show="isLoading==0">
			loading
		</div>

		<div v-show="isLoading==-1">
			404
		</div>
	</div>

</template>

<script>
	import highcharts from '@/components/VueHighcharts';
	import {chartMap} from '@/assets/scripts/chartMap.js';
	export default {
		data() {
			return {
				isLoading: 0,
				chartMap: chartMap,
				isFullWidth: false,
				option: {
			        chart: {
			            type: 'spline',
			            zoomType: 'xy',
			        },
		         	credits:{
		         		enabled: false
		         	},
			        title: {
			            text: null
			        },
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
				},
			}
		},
		components:{
			highcharts,
		},
		mounted: function() {
			this.getData()
		},
		watch:{
			$route(curVal, oldVal){
				if(curVal.params.hdfsPath != oldVal.params.hdfsPath){
					this.getData()
				}
			}
		},
		methods:{
			getData(){
				let self = this;
				self.isLoading = 0;
				console.log('time1', new Date().getTime())
				this.$http.get('hdfs'+ self.$route.params.hdfsPath +'?op=OPEN&namenoderpcaddress=10.9.171.160:9000&offset=0').then(function(res){
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
							console.log('time2', new Date().getTime())

							let lintcharts = self.$refs.chartView[index];
							lintcharts.setTitle({text: key});
							lintcharts.removeSeries()
							for (let i=0;  i < dataSerial.length; i++){
								lintcharts.addSeries(dataSerial[i])
							}
							index ++;
							console.log('time3', new Date().getTime())
						}
						self.isLoading=1
					}, function(err){
						console.log(err)
						console.log(err.ok==false)
						if(err.ok==false){
							self.isLoading=-1
						}
					});
			}
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
