// get unique value of array

window.onload = function () {
var data = [numTaskDone.value,incomplete ];
var labels = ['Compelete','Incomplete' ];

var config = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                data: data,
                label: "Alberta",
                borderColor: "#3e95cd",
                fill: false
            }, 
            {
                data: data,
                label: "BC",
                borderColor: "#8e5ea2",
                fill: false
            }, 
            {
                data: data,
                label: "Manitoba",
                borderColor: "#3cba9f",
                fill: false
            }, 
            {
                data: data,
                label: "New Brunswick",
                borderColor: "#e8c3b9",
                fill: false
            }, 
            {
                data: data,
                label: "NL",
                borderColor: "#c45850",
                fill: false
            }
        ]
        },
        options: {
            title: {
                display: true,
                text: 'Positive Cases of COVID in provinces of Canada'
            },
            hover: {
                mode: 'index',
                intersect: true
            },
        }
};



const ctx = document.getElementById('myChart').getContext('2d');
window.myLine = new Chart(ctx, config);
        