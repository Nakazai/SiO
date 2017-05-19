    var endpoint = '/api/chart/data/';
    // var defaultData = [];
    // var labels = [];
    var labels2 = [];
    var defaultData2 = [];
    // var defaultData3 = [];
    // var labels3 = [];
// window.location.reload(true);
    $.ajax({
        method: "GET",
        url: endpoint,
        // /**
        //  * @param data
        //  * @param data.labels   indicates ajax code ran successfully
        //  * @param data.default
        //  * @param data.default2
        //  * @param data.labels2
        //  * @param data.dif
        //  */
        success: function (data) {
                labels = data.labels;
                defaultData = data.default;
            // labels3 = data.labels3;
            // defaultData3 = data.genderDif;
                                    // console.log(data);

                labels2 = data.labels2;
                defaultData2 = data.default2;
            // console.log(data);
            // labels3 = data.labels3;
            // defaultData3 = data.genderDif;
                setChart()
            },
            error: function (error_data) {
                console.log("error");
                console.log(error_data)
            }
        });

    // $.ajax({
    //     method: "GET",
    //     url: endpoint,
        // /**
        //  * @param data
        //  * @param data.labels2
        //  * @param data.default2
        //  */
        // success: function (data) {
                // data = JSON.parse(data);

            // labels = data.labels;
            // defaultData = data.default;

            // labels2 = data.labels2;
            // defaultData2 = data.default2;

        //     setChart2()
        //     },
        //     error: function (error_data) {
        //         console.log("error");
        //         console.log(error_data)
        //     }
        // });

    // function setChart2(){
    //      var ctx = document.getElementById("myChart5");
    //         var myChart5 = new Chart(ctx, {
    //             type: 'bar',
    //             data: {
    //                 labels3: labels3,
    //                 datasets: [{
    //                     label: 'Total',
    //                     // label: 'Board',
    //                     // label2: 'Members',
    //                     data3: defaultData3,
    //                     backgroundColor: [
    //                         'rgba(255, 99, 132, 0.2)',
    //                         'rgba(54, 162, 235, 0.2)',
    //                         'rgba(255, 206, 86, 0.2)',
    //                         'rgba(75, 192, 192, 0.2)',
    //                         'rgba(153, 102, 255, 0.2)',
    //                         'rgba(255, 159, 64, 0.2)'
    //                     ],
    //                     borderColor: [
    //                         'rgba(255,99,132,1)',
    //                         'rgba(54, 162, 235, 1)',
    //                         'rgba(255, 206, 86, 1)',
    //                         'rgba(75, 192, 192, 1)',
    //                         'rgba(153, 102, 255, 1)',
    //                         'rgba(255, 159, 64, 1)'
    //                     ],
    //                     borderWidth: 1
    //                 }]
    //             },
    //             options: {
    //                 scales: {
    //                     yAxes: [{
    //                         ticks: {
    //                             beginAtZero:true,
    //                             callback: function(value) {if (value % 1 === 0) {return value;}}
    //                         }
    //                     }]
    //                 }
    //             }
    //         });
    // }


    function setChart(){

         var ctx1 = document.getElementById("myChart1");
            var myChart1 = new Chart(ctx1, {
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
                type: 'bar',
                data: {
                    labels2: labels2,
                    datasets: [{
                        label: 'Total',
                        // label: 'Board',
                        // label2: 'Members',
                        data: defaultData2,
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



//                 $(document).ready(function () {
//     var ctx = document.getElementById("myChart1");
//     window.myLine = new Chart(ctx).Line(myChart1, {
//         responsive: true
//     });
//     $('#download').click(function () {
//         html2canvas($("#myChart1"), {
//             onrendered: function (canvas) {
//                 var imgData = canvas.toDataURL('image/png');
//                 var doc = new jsPDF('p', 'mm');
//                 doc.addImage(imgData, 'PNG', 10, 10);
//                 doc.save('sample-file.pdf');
//             }
//         });
//     });
// });




          // var ctx2 = document.getElementById("myChart2");
          //   var myChart2 = new Chart(ctx2, {
          //       type: 'polarArea',
          //       data: {
          //           labels: labels,
          //           datasets: [{
          //               label: 'Total',
          //               data: defaultData,
          //               backgroundColor: [
          //                       "#FF6384",
          //                       "#4BC0C0",
          //                       "#FFCE56",
          //                       "#E7E9ED",
          //                       "#36A2EB"
          //               ],
          //               borderColor: [
          //                   'rgba(255,99,132,1)',
          //                   'rgba(54, 162, 235, 1)',
          //                   'rgba(255, 206, 86, 1)',
          //                   'rgba(75, 192, 192, 1)',
          //                   'rgba(153, 102, 255, 1)',
          //                   'rgba(255, 159, 64, 1)'
          //               ]
          //           }]
          //       },
          //       options:{
          //           scale: {
          //               ticks: {
          //                   stepSize: 1
          //               }
          //           }
          //       }
          //   });


         // var ctx3 = document.getElementById("myChart3");
         //    var myChart3 = new Chart(ctx3, {
         //        type: 'doughnut',
         //        data: {
         //            labels: labels,
         //            datasets: [{
         //                label: 'Total',
         //                data: defaultData,
         //                backgroundColor: [
         //                    "#FF6384",
         //                    "#36A2EB",
         //                    "#FFCE56"
         //                ],
         //                hoverBackgroundColor: [
         //                    "#FF6384",
         //                    "#36A2EB",
         //                    "#FFCE56"
         //                ]
         //                // borderWidth: 1
         //            }]
         //        }
         //    });


        //     var dataHoriz = {
        //     labels: labels,
        //     datasets: [
        //         {
        //             label: "Total",
        //             backgroundColor: "rgba(255,99,132,0.2)",
        //             borderColor: "rgba(255,99,132,1)",
        //             borderWidth: 1,
        //             hoverBackgroundColor: "rgba(255,99,132,0.4)",
        //             hoverBorderColor: "rgba(255,99,132,1)",
        //             data: defaultData,
        //             scaleOverride:true,
        //             scaleSteps:4,
        //             scaleStartValue:0,
        //             scaleStepWidth:1
        //         }
        //     ]
        // };

        // /////////////////////var ctx4 = document.getElementById("myChart4");


        // var myChart4 = new Chart($("#myChart4"), {
        //     type: 'horizontalBar',
        //     data: dataHoriz,
        //      options: {
        //         scales: {
        //          yAxes: [{
        //                     scaleLabel: {
        //                         display: true
        //                     }
        //                 }],
        //                 xAxes: [{
        //                   ticks: {
        //                     beginAtZero:true,
        //                     callback: function(value) {if (value % 1 === 0) {return value;}}
        //                   },
        //                     scaleLabel: {
        //                         display: true
        //                     }
        //                 }]
        //
        //          }
        //     }
        // });


         // var ctx5 = document.getElementById("myChart5");
         //    var myChart5 = new Chart(ctx5, {
         //        type: 'bar',
         //        data: {
         //            labels2: labels2,
         //            datasets: [{
         //                label: 'Total',
         //                // label: 'Board',
         //                // label2: 'Members',
         //                data: defaultData2,
         //                backgroundColor: [
         //                    'rgba(255, 99, 132, 0.2)',
         //                    'rgba(54, 162, 235, 0.2)',
         //                    'rgba(255, 206, 86, 0.2)',
         //                    'rgba(75, 192, 192, 0.2)',
         //                    'rgba(153, 102, 255, 0.2)',
         //                    'rgba(255, 159, 64, 0.2)'
         //                ],
         //                borderColor: [
         //                    'rgba(255,99,132,1)',
         //                    'rgba(54, 162, 235, 1)',
         //                    'rgba(255, 206, 86, 1)',
         //                    'rgba(75, 192, 192, 1)',
         //                    'rgba(153, 102, 255, 1)',
         //                    'rgba(255, 159, 64, 1)'
         //                ],
         //                borderWidth: 1
         //            }]
         //        },
         //        options: {
         //            scales: {
         //                yAxes: [{
         //                    ticks: {
         //                        beginAtZero:true,
         //                        callback: function(value) {if (value % 1 === 0) {return value;}}
         //                    }
         //                }]
         //            }
         //        }
         //    });






        // var ctx6 = document.getElementById("myChart6");
        //     var myChart6 = new Chart(ctx6, {
        //         type: 'polarArea',
        //         data: {
        //             labels2: labels2,
        //             datasets: [{
        //                 label: 'Total',
        //                 data: defaultData2,
        //                 backgroundColor: [
        //                         "#FF6384",
        //                         "#4BC0C0",
        //                         "#FFCE56",
        //                         "#E7E9ED",
        //                         "#36A2EB"
        //                 ],
        //                 borderColor: [
        //                     'rgba(255,99,132,1)',
        //                     'rgba(54, 162, 235, 1)',
        //                     'rgba(255, 206, 86, 1)',
        //                     'rgba(75, 192, 192, 1)',
        //                     'rgba(153, 102, 255, 1)',
        //                     'rgba(255, 159, 64, 1)'
        //                 ]
        //             }]
        //         },
        //         options:{
        //             scale: {
        //                 ticks: {
        //                     stepSize: 1
        //                 }
        //             }
        //         }
        //     });
        //
        //
        //
        //         var ctx7 = document.getElementById("myChart7");
        //     var myChart7 = new Chart(ctx7, {
        //         type: 'doughnut',
        //         data: {
        //             labels2: labels2,
        //             datasets: [{
        //                 label: 'Total',
        //                 data: defaultData2,
        //                 backgroundColor: [
        //                     "#FF6384",
        //                     "#36A2EB",
        //                     "#FFCE56"
        //                 ],
        //                 hoverBackgroundColor: [
        //                     "#FF6384",
        //                     "#36A2EB",
        //                     "#FFCE56"
        //                 ]
        //             }]
        //         }
        //     });



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






        //  var dataHorizMonth = {
        //     labels2: labels2,
        //     datasets: [
        //         {
        //             label: "Total",
        //             backgroundColor: "rgba(255,99,132,0.2)",
        //             borderColor: "rgba(255,99,132,1)",
        //             borderWidth: 1,
        //             hoverBackgroundColor: "rgba(255,99,132,0.4)",
        //             hoverBorderColor: "rgba(255,99,132,1)",
        //             data: defaultData2,
        //             scaleOverride:true,
        //             scaleSteps:4,
        //             scaleStartValue:0,
        //             scaleStepWidth:1
        //         }
        //     ]
        // };
        //
        // var myChart8 = new Chart($("#myChart8"), {
        //     type: 'horizontalBar',
        //     data: dataHorizMonth,
        //      options: {
        //         scales: {
        //          yAxes: [{
        //                     scaleLabel: {
        //                         display: true
        //                     }
        //                 }],
        //                 xAxes: [{
        //                   ticks: {
        //                     beginAtZero:true,
        //                     callback: function(value) {if (value % 1 === 0) {return value;}}
        //                   },
        //                     scaleLabel: {
        //                         display: true
        //                     }
        //                 }]
        //
        //          }
        //     }
        // });


    }

