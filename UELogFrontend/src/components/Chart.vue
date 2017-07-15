<template>
	<div>
		<highcharts ref="child" id="test" :option="options"></highcharts>
	</div>

</template>

<script>
	import highcharts from '@/components/HighCharts';
	import Highcharts from 'highcharts'
	export default {
		data() {
			return {
				isFullWidth: false,
				options: {
        			chart: {
			            zoomType: 'xy'
			        },
			        title: {
			            text: '东京月平均天气数据'
			        },
			        xAxis: [{
			            categories: [],
			            crosshair: true
			        }],
			        yAxis: [
			        { // Primary yAxis
			            labels: {
			                format: '{value}°C',
			                style: {
			                    color: Highcharts.getOptions().colors[2]
			                }
			            },
			            title: {
			                text: '温度',
			                style: {
			                    color: Highcharts.getOptions().colors[2]
			                }
			            },
			            opposite: true
			        }, 
			        { // Secondary yAxis
			            gridLineWidth: 0,
			            title: {
			                text: '降雨量',
			                style: {
			                    color: Highcharts.getOptions().colors[0]
			                }
			            },
			            labels: {
			                format: '{value} mm',
			                style: {
			                    color: Highcharts.getOptions().colors[0]
			                }
			            }
			        }, 
			        { // Tertiary yAxis
			            gridLineWidth: 0,
			            title: {
			                text: '海平面气压',
			                style: {
			                    color: Highcharts.getOptions().colors[1]
			                }
			            },
			            labels: {
			                format: '{value} mb',
			                style: {
			                    color: Highcharts.getOptions().colors[1]
			                }
			            },
			            opposite: true
			        }],
			        tooltip: {
			            shared: true
			        },
			        legend: {
			            layout: 'vertical',
			            align: 'left',
			            x: 80,
			            verticalAlign: 'top',
			            y: 55,
			            floating: true,
			            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
			        },
			        series: [{
			            name: '降雨量',
			            type: 'column',
			            yAxis: 1,
			            data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
			            tooltip: {
			                valueSuffix: ' mm'
			            }
			        },
			        {
			            name: '降雨量',
			            type: 'spline',
			            yAxis: 1,
			            data: [49, 71, 106, 129, 144, 176, 135, 148, 216, 194, 95, 54],
			            tooltip: {
			                valueSuffix: ' mm'
			            }
			        }, 
			        {
			            name: '海平面气压',
			            type: 'spline',
			            yAxis: 2,
			            data: [1016, 1016, 1015.9, 1015.5, 1012.3, 1009.5, 1009.6, 1010.2, 1013.1, 1016.9, 1018.2, 1016.7],
			            marker: {
			                enabled: false
			            },
			            dashStyle: 'shortdot',
			            tooltip: {
			                valueSuffix: ' mb'
			            }
			        }, {
			            name: '温度',
			            type: 'spline',
			            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
			            tooltip: {
			                valueSuffix: ' °C'
			            }
			        }]
			    },
			}
			
		},
		
		components:{
			highcharts,
		},

		beforeMount: function() {
			this.options.xAxis[0].categories = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']

			this.$http.get('api/user/wlx/test1/testCT3_result.json?op=OPEN&namenoderpcaddress=10.9.171.160:9000&offset=0').then(function(res){
					var data = JSON.parse(res.bodyText)
					for(var o in data){
						console.log(o)
						console.log(data[o])
					}
					var time1 = data["0XB0A4"]["DL_Pdcp_AM_Tput(kbps)"][0][1]
					console.log(time1)
					var time1U = new Date(time1.split('.')[0])
					console.log(time1U.setTime(time1U.getTime()+1000))
					console.log(time1U)
				}, function(){});
		}
	};


</script>

<style>

</style>
