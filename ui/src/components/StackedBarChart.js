import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

// const processData = (data) => {
//     const categories = [...new Set(data.map(item => item.Category))];
//     const months = [...new Set(data.map(item => item.YearMonth))];
//     const datasets = categories.map(category => ({
//       label: category,
//       data: months.map(month =>
//         data.find(item => item.YearMonth === month && item.Category === category)?.Amount || 0
//       ),
//       backgroundColor: getRandomColor(), // Function to get random color for each category
//     }));
  
//     return {
//       labels: months,
//       datasets,
//     };
//   };
  


const StackedBarChart = ({ data }) => {
  const chartData = data // processData(data);

  const options = {
    plugins: {
      legend: {
        labels: {
          color: 'white'
        }
      },
      title: {
        display: true,
        color: 'white',
        text: 'Monthly Expenditure by Category',
      },
    },
    responsive: true,
    scales: {
      x: {
        stacked: true,
        ticks: {
          color: 'white'
        },
        grid: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      },
      y: {
        stacked: true,
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

  return <div style={{ width: '70rem' , marginTop: '2rem', marginBottom: '2rem'}}> 
    <Bar data={chartData} options={options} />
  </div>;
};

export default StackedBarChart;
