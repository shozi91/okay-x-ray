var form = d3.select("form");
var aboutThisPage = d3.select("#about-this-page")
var ready = d3.select("#ready")
var probContainer = d3.select("#probability-container")
var imageContainer = d3.select("#image-container")
var uploadedImage = d3.select("#uploaded-image")

var button = document.getElementById("filter-btn").addEventListener("click", function(event){
    // only to stop the form from reloading the page
    // event.preventDefault();
    update();
});

function update() {
    // d3.event.preventDefault()
    aboutThisPage.classed('no-display',true)

    ready.classed('no-display',false)
    
    probContainer.classed('no-display',false)
    probContainer.classed('col',true)
    probContainer.classed('col-md-6',true)

    imageContainer.classed('col-md-6',true)
    uploadedImage.classed('no-display',false)

    
    
    console.log(aboutThisPage.attr("class"))
    console.log(ready.attr("class"))
    console.log(probContainer.attr("class"))
    console.log(imageContainer.attr("class"))
}

// form.on("submit", update())
// aLink.on("click", update())