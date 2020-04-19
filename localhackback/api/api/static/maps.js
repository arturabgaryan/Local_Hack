async function main() {
    google.charts.load('current', {
        'packages': ['geochart'],
        'mapsApiKey': 'AIzaSyDTV2pQVHP1h8wjp5Kqj_xNInbQ4zl0dWE'
    });


    google.charts.setOnLoadCallback(drawRegionsMap);

    function drawRegionsMap() {
        const data = google.visualization.arrayToDataTable([['Country', 'fefe']]);
        const options = {
            colorAxis: {colors: ['red']},
            animation: {
                duration: 1000,
                easing: 'out',
            },
        };

        const chart = new google.visualization.GeoChart(document.getElementById('chart'));
        chart.clearChart()
        button = document.getElementById('1')
        button.onclick = async function () {
            cases = await getdata()
            let i = 0;
            let a = setInterval(async function () {
                if (i < 87) {
                    console.log(i)
                    chart.clearChart()
                    const dat = await getday(cases, i, 'fdfef')
                    const data = await google.visualization.arrayToDataTable(dat);
                    chart.draw(data, options)
                    i++
                }
            }, 15)
        }


        chart.draw(data, options);
    }
}

async function getday(cases, i, str) {
    let dat = [['Country', str]]
    for (let key in cases) {
        dat.push([key, cases[key][i]['cases']])
    }
    return dat
}

async function getdata() {
    const cases = await (await fetch('http://127.0.0.1:8000/cases')).json()
    const deaths = await (await fetch('http://127.0.0.1:8000/deaths')).json()
    const recoveries = await (await fetch('http://127.0.0.1:8000/recoveries')).json()
    return [cases, deaths, recoveries]
}

function getdate(i) {
    if (i < 31) {
        if (i > 9) {
            return `2020-01-${i}`
        } else {
            return `2020-01-0${i}`
        }
    } else if (i < 60) {
        if (i > 40) {
            return `2020-02-${i}`
        } else {
            return `2020-02-0${i - 31}`
        }
    } else {
        if (i > 69) {
            return `2020-03-${i}`
        } else {
            return `2020-03-0${i-60}`
        }
    }
}

