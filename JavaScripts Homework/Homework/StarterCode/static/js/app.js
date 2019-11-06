// from data.js
var tableData = data;
// D3 Select
d3.select("#filter-btn").on("click", function(){
   d3.select("#ufo-table").select("tbody").html("") 
//Setting up x
   var xinput = data.filter(function(x){
   return x.datetime === d3.select("#datetime").property("value")
   })
//Foreach loop
   xinput.forEach(function(y){
   var row = d3.select("#ufo-table").select("tbody").append("tr")
   Object.values(y).forEach(function(x){
   row.append("td").text(x)
           })
       })
   d3.select("#datetime").property("value","")
   })
