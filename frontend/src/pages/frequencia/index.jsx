import React, { useState } from 'react';
import { Doughnut,Bar  } from 'react-chartjs-2';
import NavBar from '@/components/Navbar/navbar';
import { Fundo } from '@/components/Fundo/fundo';
import styles from './style.module.css';
import Chart from 'chart.js/auto';
import Cabecalho from '@/components/Cabecalho/cabecalho';
import ChartDataLabels from 'chartjs-plugin-datalabels';

Chart.register(ChartDataLabels);

export default function Frequencia() {
  const [attendanceData, setAttendanceData] = useState(null);
  const [chartData, setChartData] = useState({
    labels: ['Red', 'Green', 'Blue'],
    datasets: [
      {
        label: 'My First Dataset',
        data: [300, 50, 100],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 205, 86, 0.2)'
        ],
      }
    ]
  });

  const barChartData = {
    labels: ['Red', 'Green', 'Blue'],
    datasets: [
      {
        label: 'My Second Dataset',
        data: [200, 100, 50],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      }
    ]
  };

  const barChartOptions = {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      datalabels: {
        formatter: (value, context) => {
          let sum = 0;
          let dataArr = context.chart.data.datasets[0].data;
          dataArr.map((data) => {
            sum += data;
          });
          let percentage = (value * 100 / sum).toFixed(2) + "%";
          return percentage;
        },
        color: '#fff',
        anchor: 'center'
      },
      legend: {
        position: 'left',
      },
      title: {
        display: true,
        text: '',
      },
    },
  };

  if (!chartData) {
    return <div>Loading...</div>;
  }

 return (
  <>
    <NavBar />
    <Cabecalho/>
      <Fundo className={styles.Fundo}>
        <div className={styles.container_center}>
          <div className={styles.tituloGrafico}>
            <h2>Alunos Presentes</h2>
          <div className={styles.graficoCircular}>
            <Doughnut data={chartData} options={chartOptions} className={styles.Doughnut} />
          </div>
          </div>
        </div>
      </Fundo>
      <Fundo className={styles.Fundo}>
        <div className={styles.container_center}>
          <div className={styles.tituloGrafico}>
            <h2>Frequencia Semanal</h2>
          <div className={styles.graficoBar}>
          <Bar data={barChartData} options={barChartOptions} className={styles.Bar} />
          </div>
          </div>
        </div>
      </Fundo>
  </>
);
}

