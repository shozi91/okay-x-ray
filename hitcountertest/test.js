(function()
{
    // Define a Counter class.
    var counter = {};           // Prototype object for Counter.

    counter.__init__ = function(name){

        this.name = name;
        this.count = 0;
    };

    counter.onclick = function(event){

        this.count ++;
    };

    counter.html = function(){

        return this.name + ' ' + this.count;
    };

    Counter = SimpleClass(counter);


    // Make explicit use of global variables.
    var global = (function(){return this;})();


    // Interaction.
    var onclick_factory = function(models){

        var onclick = function(event){

	    event = event || global.event; // For IE event handling.
	    var target = event.target || event.srcElement;
            var id = target.id;
            if (id) {
                var id_num = +id.slice(1);
                var model = models[id_num];
                model.onclick();
                var html = model.html();
                if (html){
                    global.document.getElementById(id).innerHTML = html;
                }
            }
        };
        return onclick;
    };


    // Set up the web page.
    global.onload = function(){

        var models = [
            Counter('apple'),
            Counter('banana'),
            Counter('cherry'),
            Counter('date')
        ];

        var element = document.getElementById('example');

        element.innerHTML = (
            '<span id="a0">apple 0</span>'
            + '<span id="a1">banana 0</span>'
            + '<span id="a2">cherry 0</span>'
            + '<span id="a3">date 0</span>'
        );

        element.onclick = onclick_factory(models);
        element = undefined;    // Avoid IE memory leak.
    };

})();