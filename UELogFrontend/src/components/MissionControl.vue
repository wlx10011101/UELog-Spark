<template>
	<div>
		<button style="margin-top: 1%; margin-left:1%" v-on:click="startMission" :disabled="isDisable">
			{{missionName}}
		</button>
		<div class="slider">
			<div class="slider-handle" style="left: 0%;"></div>
			<div class="slider-handle" style="left: 50%;" 
				:class="{'fail': parserStatus==-1, 'success': parserStatus==1, 'not-complete': parserStatus==0}">
				</div>
			<div class="slider-handle" style="left: 100%;"
				:class="{'fail': calcStatus==-1, 'success': calcStatus==1, 'not-complete': calcStatus==0}">
			</div>
			<div class='progress'>
				
				<div id="progressParser" class="progress-bar progress-bar-striped" 
				:class="{'parsering': parserStatus!=null, 'calcing': calcStatus!=null, 'active': parserStatus==0||calcStatus==0}"
				role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"><span class="sr-only"></span></div>
				<!-- <button type="button" class="btn btn-default bs-docs-activate-animated-progressbar active" data-toggle="button" aria-pressed="true" autocomplete="off"></button> -->
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	export default{
		data(){
			return {
				parserStatus: 1,
				calcStatus: 0,
			}
		},
		props: ['missionName'],
		computed:{
			isDisable: function() {
				console.log(self.parserStatus!==null || self.calcStatus!==null)
				return self.parserStatus!==null || self.calcStatus!==null
			}
		},
		mounted:function(){
			},
		methods:{
			startMission: function(){
				console.log("startMission", this.missionName)
			},
			isNull:function(data){
				if(data==null){
					return true;
				}
				else{
					return false;
				}
			},
		}
	}

</script>

<style type="text/css" scoped>
	@import '../assets/vendor/bootstrap/css/bootstrap.css';
	.slider-host{
		height: 100%;
	    width: 100%;
	    display: inline-block;
	    -webkit-user-select: none;
	    -moz-user-select: none;
	    -ms-user-select: none;
	    user-select: none;
	}
	.slider{
		display: block;
	    position: relative;
	    margin: 10px 6px;
	    height: 12px;
	    border-radius: 4px;
	    /*cursor: pointer;*/
	    background-color: #e9e9e9;
	    border-top: 4px solid #fff;
	    border-bottom: 4px solid #fff;
	    -webkit-user-select: none;
	    -moz-user-select: none;
	    -ms-user-select: none;
	    user-select: none;
	    transition: background-color .3s ease;
	}
	.slider .slider-track {
    position: absolute;
    left: 0;
    height: 4px;
    border-radius: 4px;
    background-color: #9fd2f6;
    z-index: 1;
    transition: background-color .3s ease;
	}
	.slider .slider-step {
    position: absolute;
    width: 100%;
    height: 4px;
    background: transparent;
    z-index: 1;
	}
	.slider .slider-handle{
		position: absolute;
	    margin-left: -8px;
	    margin-top: -2px;
	    width: 20px;
	    height: 20px;
	    border-radius: 50%;
	    border: 3px solid #337ab7;
	    background-color: #fff;
	    z-index: 2;
	    transition: border-color .3s ease,-webkit-transform .3s cubic-bezier(.18,.89,.32,1.28);
	    transition: border-color .3s ease,transform .3s cubic-bezier(.18,.89,.32,1.28);
	    transition: border-color .3s ease,transform .3s cubic-bezier(.18,.89,.32,1.28),-webkit-transform .3s cubic-bezier(.18,.89,.32,1.28);
	}

	.slider .slider-handle.fail {
		border-color: red;
	}

	.slider .slider-handle.success {
		border-color: green;
	}
	.slider .slider-handle.not-complete {
		-webkit-animation: shine 0.8s infinite;
	}
	.progress{
		height: 15px !important;
	}
	.progress .progress-bar.idle{
		width: 0%
	}
	.progress .progress-bar.parsering{
		width: 50%
	}
	.progress .progress-bar.calcing{
		width: 100%
	}
	@keyframes twinkling{
		0% {
			opacity: 0
			},
		100% {
			opacity: 1
		};
	}
	@keyframes shine{
		0% {
			background-color: #88c7f4;
			},
		100% {
			background-color: #337ab7;
		};
	}
</style> 