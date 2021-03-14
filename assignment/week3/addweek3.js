var src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json";

fetch (src).then(function (response){
    return response.json();

}).then(function (data){
    var length = Object.keys(data.result.results).length;
    var main = document.querySelector (".main");
      
    for ( var i=0; i < length ; i++) {

        var stitle = data.result.results[i].stitle;
        var imageFile = data.result.results[i].file;
        var splitFile = imageFile.split("http",50);
        var file = "http"+splitFile[1];

            if (i%4==0){
                var container= document.createElement("div");
                container.setAttribute ("class","container");
                main.appendChild(container);
            }

            var figureElement = document.createElement("figure");
            var imgElement = document.createElement("img");
                imgElement.setAttribute ("src",file);
            var figcaptionElement = document.createElement("figcaption");
            var spots = document.createTextNode (stitle);
                figcaptionElement.appendChild(spots);
            figureElement.appendChild(imgElement);
            figureElement.appendChild(figcaptionElement);

            if (i%4==0){
                
                container.appendChild(figureElement);

            }else {
                container.appendChild(figureElement)
            }
                
        };
       
})

