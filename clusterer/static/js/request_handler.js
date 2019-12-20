$(document).ready(function(){

    var score_div = document.getElementById("score_div")
    score_div.style.display = "none";
    
    var stopwords_cv = document.getElementById("stopwords_cv")
    var depth_dd = document.getElementById("dd_depth");
    var loadRaw_btn = document.getElementById("loadData");
    var preprocess_btn = document.getElementById("preProcessData");
    var run_btn = document.getElementById("runAlgorithm");

    var repres_dd = document.getElementById("dd_representation"); 
    var algo_dd = document.getElementById("dd_algo");
    var similarity_dd = document.getElementById("dd_sim");

    var no_ppo_cb = document.getElementById("ppo_cb");
    var only_noun_cb = document.getElementById("noun_cb");
    var lem_cb = document.getElementById("lem_cb");
    var stem_cb = document.getElementById("stem_cb");
    var split_cb = document.getElementById("split_cb");
    var min_ngrams_tb = document.getElementById("n_ngrams_min");
    var max_ngrams_tb = document.getElementById("n_ngrams_max");
    var clu_tb = document.getElementById("n_cluster");
    var dim_tb = document.getElementById("n_dim");

    $("#loadData").click(function(){
        stopwords = stopwords_cv.checked
        depth = depth_dd.options[depth_dd.selectedIndex].value;
        change_btns(true);
        path = ""
        console.log("calc stopwords: " + stopwords)
        console.log("asking for data")
        $.ajax({
            type: "POST",
            url: "http://localhost:5000/rawdata",
            data: {path:path, depth:depth, cal_stopwords:stopwords},
            success: function(data){
                console.log(data)
                preprocess_btn.value = "unblocked"
                change_btns(false)
            }
        })
    })
    $("#preProcessData").click(function(){
        change_btns(true);

        var no_ppo = no_ppo_cb.checked;
        var only_nouns = only_noun_cb.checked;
        var lem = lem_cb.checked;
        var stem = stem_cb.checked;
        var split = split_cb.checked;

        console.log("asking for data-processing");
        console.log(" - no place/person/organisation: " + no_ppo);
        console.log(" - only nouns: " + only_nouns);
        console.log(" - lemmatization: " + lem);
        console.log(" - stemming: " + stem);
        console.log(" - split: " + split);
    
        $.ajax({
            type: "POST",
            url: "http://localhost:5000/preprocess",
            data: {no_ppo:no_ppo, only_nouns:only_nouns, lemmatization:lem, stemming:stem, split:split},
            success: function(data){
                console.log(data)                            
                run_btn.value = "unblocked"
                change_btns(false)
            }
        })
    })
    $("#runAlgorithm").click(function(){
        change_alert(false)
        change_btns(true);

        var repr = repres_dd.options[repres_dd.selectedIndex].value;
        var algo = algo_dd.options[algo_dd.selectedIndex].value;
        var simi = similarity_dd.options[similarity_dd.selectedIndex].value;
        var ngrams_min = min_ngrams_tb.value;
        var ngrams_max = max_ngrams_tb.value;
        var n_cluster = clu_tb.value;
        var n_dim = dim_tb.value;
        if (repr == "none" || algo == "none" || simi == "none"){
            change_alert(true)
            change_btns(false)
        }

        console.log("request to run algorithm");
        console.log(" - representation: " + repr);
        console.log(" - algorithm: " + algo);
        console.log(" - similarity: " + simi);
        console.log(" - min n-grams: " + ngrams_min);
        console.log(" - max n-grams: " + ngrams_max);
        console.log(" - number of clusters: " + n_cluster);
        console.log(" - vector dimensions: " + n_dim);
        $.ajax({
            type: "POST",
            url: "http://localhost:5000/res",
            data: {representation:repr, algorithm:algo, similarity:simi, min_ngram:ngrams_min, max_ngram:ngrams_max, n_cluster:n_cluster, n_dim:n_dim},
            success: function(data){
                console.log(data)
                json_data = JSON.parse(data)

                score_div.style.display = "block";

                visualiseBubbleChart(json_data["bubbleChart"])
                visualiseMigMa(json_data["migMa"])
                visualiseScore(json_data["scores"])
                
                change_btns(false)
            }
        })
    })    
})