// from data.js
var tableData = data;

// YOUR CODE HERE!
d3.select("#filter-btn").on("click", function(){
   d3.select("#ufo-table").select("tbody").html("")
   var stuff = data.filter(function(x){
   return x.datetime === d3.select("#datetime").property("value")
   })
   stuff.forEach(function(y){
   var row = d3.select("#ufo-table").select("tbody").append("tr")
   Object.values(y).forEach(function(x){
   row.append("td").text(x)
           })
       })
   d3.select("#datetime").property("value","")
   })