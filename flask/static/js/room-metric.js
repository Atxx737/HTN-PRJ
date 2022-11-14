window.onload = function () {
  //                    var labels ='{{ date|length }}';  // date
                      var labels = '{{ date }}'.split("|")
                      var name = 1;
                      var config = {
                          data: {
                              labels: labels,
                              datasets: [
                                  {
                                      type: 'bar',
  
                                      label: 'Temperature',
                                      // data: '{{ temp }}',
                                      data: '{{ temp }}'.split("|"),
                                      backgroundColor: [
                                      'rgba(255, 99, 132, 0.2)',
                                      ],
                                      borderColor: [
                                      'rgb(255, 99, 132)',
                                      ],
                                      borderWidth: 1
                                  },
                                
                                  {
                                      type: 'bar',
                                      label: 'Humidity',
                                      data: '{{ hum }}'.split("|"),
                                      backgroundColor: [
                                      'rgba(54, 162, 235, 0.2)',
                                      ],
                                      borderColor: [
                                      'rgb(54, 162, 235)'
                                      ],
                                      borderWidth: 2
                                  },
                                  ]
                            
                              },
                              options: {
                                  scales: {
                                    y: {
                                      beginAtZero: true
                                    }
                                  },
                                  plugins: {
                                    autocolors: true,
                                    annotation: {
                                      annotations: {
                                        line1: {
                                          type: 'line',
                                          yMin: 65,
                                          yMax: 65,
                                          borderColor: 'rgb(255, 255, 255)',
                                          borderWidth: 20,
                                        }
                                      }
                                    }
                                  }
                              }
                      };
                      
                      
                      
                      const ctx = document.getElementById('myChart').getContext('2d');
                      window.myLine = new Chart(ctx, config);
                      };