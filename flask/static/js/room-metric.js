// get unique value of array

var numHum= document.querySelector(".nu-hum");
var numTem= document.querySelector(".nu-tem");
var numDate= document.querySelector(".nu-date");
console.log("numHum",numHum.value);
console.log("numTem",numHum.value);
console.log("numDate",numHum.value);


// var numTaskDone= document.querySelector(".nu-taskdone");
// console.log("numTaskDone",numTaskDone.value);
    

// var incomplete= numTask.value - numTaskDone.value;
// console.log("incomplete",incomplete);

window.onload = function () {
    var data = [numTem ]; // temp
    var labels = [numDate ];  // date
    
    var config = {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: data,
                    data: data,
                    backgroundColor: [
                      'rgba(255, 99, 132, 0.2)',
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                    ],
                    borderWidth: 1
                }]
            //     {
            //         data: data,
            //         label: "Alberta", //name of line
            //         borderColor: "#3e95cd",
            //         fill: false
            //     }, 
            //     {
            //         data: data,
            //         label: "BC",
            //         borderColor: "#8e5ea2",
            //         fill: false
            //     }, 
            //     {
            //         data: data,
            //         label: "Manitoba",
            //         borderColor: "#3cba9f",
            //         fill: false
            //     }, 
            //     {
            //         data: data,
            //         label: "New Brunswick",
            //         borderColor: "#e8c3b9",
            //         fill: false
            //     }, 
            //     {
            //         data: data,
            //         label: "NL",
            //         borderColor: "#c45850",
            //         fill: false
            //     }
            // ]
            },
            options: {
                scales: {
                  y: {
                    beginAtZero: true
                  }
                }
            }
    };
    
    
    
    const ctx = document.getElementById('myChart_temp').getContext('2d');
    window.myLine = new Chart(ctx, config);
    };