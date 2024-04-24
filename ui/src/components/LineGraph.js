import React from 'react';
import { Line } from 'react-chartjs-2';

const LineGraph = ({ data }) => {
  const chartData = {
    labels: data.map(item => item.Month),
    datasets: [
      {
        label: 'Total Expenditure',
        data: data.map(item => item.TotalExpenditure),
        fill: false,
        backgroundColor: 'rgb(75, 192, 192)',
        borderColor: 'rgba(75, 192, 192, 0.2)',
      }
    ]
  };

  const options = {
    scales: {
      y: {
        beginAtZero: true
      }
    },
    maintainAspectRatio: false
  };

  return <div style={{ height: '300px' }}>
    <Line data={chartData} options={options} />
  </div>;
};

export default LineGraph;
