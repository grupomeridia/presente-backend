import React, { useEffect, useState } from 'react';
import { Doughnut } from 'react-chartjs-2';
import NavBar from '@/components/Navbar/navbar';
import { Fundo } from '@/components/Fundo/fundo';
import Chart from 'chart.js/auto';
import styles from './style.module.css'

const Frequencia = () => {

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
        ]
      }
    ]
  });
  

  const chartOptions = {
    responsive: true,
     maintainAspectRatio: false, 
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Doughnut Chart',
      },
    },
  };

  if (!chartData) {
    return <div>Loading...</div>;
  }

  const randomizeData = (chart) => {

  };

  return (
    <>
      <NavBar />
      <h1>Cabeçalho</h1>
      <button onClick={() => randomizeData()}>Randomize</button>
      <div className={styles.container}>
        <Fundo>
          <Doughnut data={chartData} options={chartOptions} />
        </Fundo>
      </div>
    </>
  );
};

export default Frequencia;
