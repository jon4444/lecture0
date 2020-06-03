window.addEventListener("load", function(){

    var btn1 = document.querySelector("#btn1");
        btn1.addEventListener("click", function(){
            document.querySelector("#btn1").innerHTML = "PSYCH!!!";
        });
        //make button red on mouseover
        btn1.addEventListener("mousedown", e => {
            document.querySelector("#btn1").style.color = "red";
        });


});