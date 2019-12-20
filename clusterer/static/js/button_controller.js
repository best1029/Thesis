var loadRaw_btn = null;
var preprocess_btn = null;
var run_btn = null;

window.onload = function() {
    change_alert(false)
    loadRaw_btn = document.getElementById("loadData");
    preprocess_btn = document.getElementById("preProcessData");
    run_btn = document.getElementById("runAlgorithm");
}

function change_alert(value) {
    var x = document.getElementById("runAlg_div");
    if (value){
        x.style.display = "block";
    }
    else{
        x.style.display = "none";
    }
}

function change_btns(value){
    var btns = [loadRaw_btn, preprocess_btn, run_btn];
    for (var i = 0; i < btns.length; i++) {
        if (btns[i].value != "blocked"){
            btns[i].disabled = value;
        }
    }
}