// from data.js
var tableData = data;


// adding the data from the data.js file into the index.html
tableData.forEach(function(ufo){
    var row = d3.select("tbody").append("tr");
    Object.values(ufo).forEach(function(value) {
      row.append("td").text(value);
    });
  });
// function to put n a specific date 
function noargs(q){
   // To clear out the previous selection befor running a new one
  d3.select("tbody").html("");
  // var abc is a variable for the filtered version of data.js file filtering by datetime value 
  var abc=tableData.filter(function(z){
    return z.datetime===q;
  });

// we are using the filtered data and looping over the whole data set outputing in tbody every 
// appropriate row
  abc.forEach(function(ufo){
    var row = d3.select("tbody").append("tr");
    Object.values(ufo).forEach(function(value) {
      row.append("td").text(value);
    });
  });
};

function urg(){
  var xyza= d3.select(".form-control").node().value;
  noargs(xyza);
};

