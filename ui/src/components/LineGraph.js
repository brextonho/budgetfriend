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
        data: data.map(item => item.TotalExpenditure), // parseFloat(item.TotalExpenditure))
        fill: false,
        backgroundColor: 'rgb(75, 192, 192)',
        borderColor: 'rgba(75, 192, 192, 0.2)',
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Monthly Expenditure Over Time'
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Expenditure ($)'
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
