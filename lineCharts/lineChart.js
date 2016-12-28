function init(option){
	var id = option.id;
	var innerDivs = option.innerDivs;
	var height = 40;
	if(option.height){
		height = option.height;
	}
	var lineChartStr = '#'+id;
	var lineChart = $(lineChartStr);
	lineChart.css('line-height',height+'px');
	lineChart.attr("class",'chartLine');
	
	var innerHtml="";
	for(var index = 0; index <innerDivs.length; index++){
		var tempObj = innerDivs[index];
		if(innerDivs.length == 1 && index == 0){
			innerHtml += '<div id="'+tempObj.id+'" style="text-align:center; float :left;width:'+tempObj.width+'%; height:100%; background:'+tempObj.color+'; -moz-border-radius:10px;-webkit-border-radius:10px;border-radius: 10px;"><span class="innerChartSpan">'+tempObj.text+'</span></div>';
		}
		else if(index == innerDivs.length-1){
			innerHtml += '<div id="'+tempObj.id+'" class="innerDiv-r" style="text-align:center; float :left;width:'+tempObj.width+'%; height:100%;background:'+tempObj.color+'; "><span class="innerChartSpan">'+tempObj.text+'</span></div>';	
		}
		else if(index == 0){
			innerHtml += '<div id="'+tempObj.id+'" class="innerDiv-l" style="text-align:center; float :left;width:'+tempObj.width+'%; height:100% ;background:'+tempObj.color+';"><span class="innerChartSpan">'+tempObj.text+'</span></div>';		
		}
		else{
			innerHtml += '<div id="'+tempObj.id+'" style="text-align:center; float :left;width:'+tempObj.width+'%; height:100%; background:'+tempObj.color+';"><span class="innerChartSpan">'+tempObj.text+'</span></div>';			
		}
	}
	lineChart.append(innerHtml);
}