p<template>
	<div id="sidebar-nav" class="sidebar" v-bind:class="{'full-width': isFullWidth}">
		<div class="sidebar-scroll">
			<nav>
				<ul class="nav">
					<li><a href="#/missions" class=""><i class="lnr lnr-home"></i> <span>Missions</span></a></li>
					
					<li>
						<a href="#subPages" data-toggle="collapse" class="collapsed">
							<i class="lnr lnr-chart-bars"></i> 
							<span>Charts</span>
							<i class="icon-submenu lnr lnr-chevron-left"></i>
						</a>
						<div id="subPages" class="collapse">
							<ul class="nav">
								<li>
									<a class="" v-for="result in results">
										<router-link :to="{name:'Chart', params:{hdfsPath: result.HdfsResultPath}}">
											{{result.fileName}}
										</router-link>
									</a>
								</li>
							</ul>
							
						</div>
					</li>
				</ul>
			</nav>
		</div>
	</div>
</template>

<script>
	import bus from "@/assets/scripts/eventBus";
	export default{
		data() {
			return {
				isFullWidth: false,
				results: [],
			}
			
		},
		mounted: function(){
			let self = this
			self.results = []
			bus.$on("toggleFullWidth", function(msg){
				self.isFullWidth = ! self.isFullWidth;
			});
			self.$http.get('/uelog/querySuccessRecord').then(
				function(res){
					let successResults = JSON.parse(res.bodyText);
					for(let i in successResults){
						let dataSplit = successResults[i]['HdfsResultPath'].split('/')
						let fileName = dataSplit[dataSplit.length - 1].split('_result')[0]
						successResults[i]['fileName'] = fileName
						self.results.push(successResults[i])
					}
				}, function(err){
					console.log(err);
				});
		}
	};
	import '@/assets/vendor/jquery/jquery.js';
	import '@/assets/vendor/bootstrap/js/bootstrap.min.js';
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 @import '../assets/css/demo.css';
 @import '../assets/css/main.css';

 #sidebar-nav.full-width {
 	left: -260px;
 }
</style>
