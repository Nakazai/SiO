    var endpoint = '/api/chart/data/';
    var defaultData = [];
    var labels = [];

    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            labels = data.labels;
            defaultData = data.default;
            setChart()
            },
            error: function (error_data) {
                console.log("error");
                console.log(error_data)
            }
        });

    function setChart(){
         var ctx = document.getElementById("myChart1");
            var myChart1 = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Total',
                        // label: 'Board',
                        // label2: 'Members',
                        data: defaultData,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true,
                                callback: function(value) {if (value % 1 === 0) {return value;}}
                            }
                        }]
                    }
                }
            });

          var ctx2 = document.getElementById("myChart2");
            var myChart2 = new Chart(ctx2, {
                type: 'polarArea',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Total',
                        data: defaultData,
                        backgroundColor: [
                                "#FF6384",
                                "#4BC0C0",
                                "#FFCE56",
                                "#E7E9ED",
                                "#36A2EB"
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ]
                        // scaleShowLabels: false
                    }]
                },
                options:{
                    scale: {
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            });


        var ctx3 = document.getElementById("myChart3");
            var myChart3 = new Chart(ctx3, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Total',
                        data: defaultData,
                        backgroundColor: [
                            "#FF6384",
                            "#36A2EB",
                            "#FFCE56"
                        ],
                        hoverBackgroundColor: [
                            "#FF6384",
                            "#36A2EB",
                            "#FFCE56"
                        ]
                        // borderWidth: 1
                    }]
                }
            });


          // var ctx4 = document.getElementById("myChart4");
          //   var myChart4 = new Chart(ctx4, {
          //       type: 'pie',
          //       data: {
          //           labels: labels,
          //            datasets: [{
          //               label: 'Total',
          //               data: defaultData,
          //               backgroundColor: [
          //                   "#FF6384",
          //                   "#36A2EB",
          //                   "#FFCE56"
          //               ],
          //               hoverBackgroundColor: [
          //                   "#FF6384",
          //                   "#36A2EB",
          //                   "#FFCE56"
          //               ]
          //               // borderWidth: 1
          //           }]
          //       }
          //   });

        var dataHoriz = {
            labels: labels,
            datasets: [
                {
                    label: "Total",
                    backgroundColor: "rgba(255,99,132,0.2)",
                    borderColor: "rgba(255,99,132,1)",
                    borderWidth: 1,
                    hoverBackgroundColor: "rgba(255,99,132,0.4)",
                    hoverBorderColor: "rgba(255,99,132,1)",
                    data: defaultData,
                    scaleOverride:true,
                    scaleSteps:4,
                    scaleStartValue:0,
                    scaleStepWidth:1
                }
            ]
        };

        // var ctx4 = document.getElementById("myChart4");
        var myChart4 = new Chart($("#myChart4"), {
            type: 'horizontalBar',
            data: dataHoriz,
             options: {
                scales: {
                 yAxes: [{
                            scaleLabel: {
                                display: true
                            }
                        }],
                        xAxes: [{
                          ticks: {
                            beginAtZero:true,
                            callback: function(value) {if (value % 1 === 0) {return value;}}
                          },
                            scaleLabel: {
                                display: true
                            }
                        }]

                 }
            }
        });
    }

