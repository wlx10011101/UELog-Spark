<template>
	<div id="sidebar-nav" class="sidebar" v-bind:class="{'full-width': isFullWidth}">
		<div class="sidebar-scroll">
			<nav>
				<ul class="nav">
					<li><a href="#" class=""><i class="lnr lnr-home"></i> <span>Dashboard</span></a></li>
					
					<li>
						<a href="#subPages" data-toggle="collapse" class="collapsed">
							<i class="lnr lnr-chart-bars"></i> 
							<span>Charts</span>
							<i class="icon-submenu lnr lnr-chevron-left"></i>
						</a>
						<div id="subPages" class="collapse">
							<ul class="nav">
								<li><a href="#/Chart" class="">file1</a></li>
							</ul>
							
						</div>
					</li>
					
				<!-- 	<li>
						<a href="#subPages1" data-toggle="collapse" class="collapsed">
							<i class="lnr lnr-file-empty"></i>
							<span>Pages</span> 
							<i class="icon-submenu lnr lnr-chevron-left"></i>
						</a>
						<div id="subPages1" class="collapse">
							<ul class="nav">
								<li><a href="#" class="">Profile</a></li>
								<li><a href="#" class="">Login</a></li>
								<li><a href="#" class="">Lockscreen</a></li>
							</ul>
						</div>
					</li> -->
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
				isFullWidth: false
			}
			
		},
		mounted: function(){
			let self = this
			bus.$on("toggleFullWidth", function(msg){
				self.isFullWidth = ! self.isFullWidth;
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
