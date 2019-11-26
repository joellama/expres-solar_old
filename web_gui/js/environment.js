Highcharts.chart('environment', {
    chart: {
        type: 'spline',
        animation: Highcharts.svg, // don't animate in old IE
        // marginRight: 0,
        events: {
            load: function () {
                // set up the updating of the chart each second
                var series_T = this.series[0];
                var series_H = this.series[1];
                maxSamples = 30;
                count_T = 0;
                count_H = 0;
                socket.on('updateEnv', function(data){
                    var x = Date.parse(data['Time'])
                        y = data['Temp']
                        z = data['Humidity'];
                    series_T.addPoint([x, y], true, (++count_T >= maxSamples));
                    series_H.addPoint([x, z], true, (++count_H >= maxSamples));

                });
            }
        }
    },

    time: {
        useUTC: false
    },

    title: {
        text: ''
    },
 legend: {
        layout: 'vertical',
        align: 'left',
        x: 120,
        verticalAlign: 'top',
        y: 100,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || // theme
            'rgba(255,255,255,0.25)'
    },    
    xAxis: {
        type: 'datetime',
        tickPixelInterval: 10,
        labels: {
            rotation: 0,
        },
        dateTimeLabelFormats: {
              second: '%H:%M<br/>%S', 
        }       
    },
    yAxis: [{
        labels: {
            format: '{value}°C',
            style: {
                color: '#D3322E'
            }
        }, 
        min: -20.0,
        max: 50.0,
        title: {
            text: 'Dome Temperature',
            style: {
                color: '#D3322E'
            }
        },

    }, { // Secondary yAxis
        title: {
            text: 'Humidity',
            style: {
                color: '#03A2D9',
            }
        },
        labels: {
            format: '{value} %',
            style: {
                color: '#03A2D9',
            }
        },
        min: 0,
        max: 100,
        opposite: true
    }],
    tooltip: {
        shared: true
    },

    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x:%Y-%m-%d %H:%M<br%S}<br/>{point.y:.2f}'
    },
    legend: {
        enabled: true
    },
    exporting: {
        enabled: false
    },
    series: [{
        name: 'Temperature',
        type: 'spline',
        data: [],
        color: '#D3322E',
        tooltip: {
            valueSuffix: '°C'
        }

    }, {
        name: 'Humidity',
        type: 'spline',
        yAxis: 1,
        data: [],
        color: '#03A2D9',
        tooltip: {
            valueSuffix: ' %'
        }
    }]
});