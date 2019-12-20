google.charts.load('current', {'packages':['corechart', 'table']});

            function visualiseBubbleChart(values) {
                console.log("visualising bubble chart")
                var data = google.visualization.arrayToDataTable(values);
        
                var options = {
                    title: 'Cluster-Results',
                    hAxis: {title: 'X'},
                    vAxis: {title: 'Y'},
                    bubble: {textStyle: {fontSize: 11}}
                };
        
                var chart = new google.visualization.BubbleChart(document.getElementById('bubble_chart_div'));
                chart.draw(data, options);
            }

            function visualiseMigMa(values) {
                console.log(values)
                console.log("visualising migma chart")
                var data = google.visualization.arrayToDataTable(values, false);
                console.log(data)

                var table = new google.visualization.Table(document.getElementById('migma_div'));
                table.draw(data, {showRowNumber: true, width: '80%', height: '80%'});
            }

            function visualiseScore(values){
                document.getElementById('ari_lbl').innerHTML = values["ari"]
                document.getElementById('purity_lbl').innerHTML = values["homo_score"]
                document.getElementById('comp_lbl').innerHTML = values["completness"]
                document.getElementById('v_lbl').innerHTML = values["v_measure"]
            }