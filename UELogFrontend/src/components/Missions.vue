<template>
	<div>
		<div v-for="value in datas">
			<missioncontrol style="margin:20px" :missionName="value['missionName']"></missioncontrol>
		</div>
	</div>
</template>

<script type="text/javascript" scoped>
	import missioncontrol from '@/components/MissionControl' 
	export default{
		data(){
			return{
				datas:[],
			}
		},
		components:{
			missioncontrol,
		},
		mounted: function(){
			let self = this;
			this.$http.post('/qcat/getIsfFiles/D:%5CqcatLogFile').then(
				function(res){
					let allIsfFile = JSON.parse(res.bodyText);
					this.$http.get('/uelog/queryOverRecord').then(
						function(res){
							let data = JSON.parse(res.bodyText);
							for(let i=0; i< data.length; i++){
								if(allIsfFile.includes(data[i]['IsfFilePath'])){
									allIsfFile.splice(allIsfFile.indexOf(data[i]['IsfFilePath']))
								};
							};
							for(let i=0; i<allIsfFile.length; i++){
								let dataCell = {}
								dataCell['missionName'] = allIsfFile[i]
								self.datas.push(dataCell)
							};
						},function(err){
							console.log(err)
						});
				},function(err){
					console.log(err)
				})
		},
	};
</script>

<style type="text/css" scoped>
	missioncontrol {
		margin:15px; 
	}
</style>