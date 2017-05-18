$(document).ready(function() {

var lodedSize = 0;
 var number_of_media = $("main div ul table").length;

doProgress();

// function for the progress bar
 function doProgress() {
 $("table").load(function() {
 lodedSize++;
 var newWidthPercentage = (lodedSize / number_of_media) * 100;
 animateLoader(newWidthPercentage + '%');
 })
 }

//Animate the loader
 function animateLoader(newWidth) {
 $("#progressBar").width(newWidth);
 if(lodedSize>=number_of_media){
 setTimeout(function(){
 $("#progressBar").animate({opacity:0});
 },500);
 }
 }

});