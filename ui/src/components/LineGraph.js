import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const LineGraph = ({ data }) => {
  const chartData = {
    labels: data.map(item => item.Month),
    datasets: [
      {
        label: 'Total Expenditure',
        data: data.map(item => item.Amount),
        fill: false,
        backgroundColor: 'rgb(75, 192, 192)',
        borderColor: 'rgba(75, 192, 192, 0.2)',
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        labels: {
          color: 'white' 
        }
      },
      title: {
        display: true,
        color: 'white',
        text: 'Monthly Expenditure Over Time'
      }
    },
    scales: {
      x: {
        ticks: {
          color: 'white'
        },
        grid: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      },
      y: {
        beginAtZero: true,
        ticks: {
          color: 'white'
        },
        grid: {
          color: 'rgba(255, 255, 255, 0.1)'
        },
        title: {
          display: true,
          text: 'Expenditure ($)',
          color: 'white'
        }
      }
    }
  };

// height: '300px'
  return <div style={{ width: '1000px' }}>
    <Line data={chartData} options={options} />
  </div>;
};

export default LineGraph;
