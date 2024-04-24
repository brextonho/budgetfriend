import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import LineGraph from './components/LineGraph';
import StackedBarChart from './components/StackedBarChart';

function App() {
  const [lineChartData, setLineChartData] = useState(null);
  const [barChartData, setBarChartData] = useState(null);
  const egbarChartData = {
    labels: ['January 2019', 'February 2019', 'March 2019', 'April 2019', 'May 2019', 'June 2019'],
    datasets: [
        {
            label: 'Dining Out',
            data: [732.17, 800.34, 920.23, 678.45, 789.56, 654.32],
            backgroundColor: '#FF6384'
        },
        {
            label: 'Entertainment',
            data: [688.52, 612.34, 500.45, 312.67, 423.78, 734.89],
            backgroundColor: '#36A2EB'
        },
        {
            label: 'Groceries',
            data: [131.16, 240.55, 300.34, 450.76, 500.89, 600.12],
            backgroundColor: '#FFCE56'
        },
        {
            label: 'Health',
            data: [82.77, 120.11, 150.25, 130.34, 140.45, 160.56],
            backgroundColor: '#4BC0C0'
        },
        {
            label: 'Transportation',
            data: [487.84, 525.34, 600.21, 700.45, 800.34, 900.23],
            backgroundColor: '#9966FF'
        },
        {
            label: 'Utilities',
            data: [300.45, 350.67, 400.89, 450.23, 500.34, 550.45],
            backgroundColor: '#FF9F40'
        }
    ]
};

// do we need this?
  // const handleFileUploadSuccess = (uploadedData) => {
  //   // Set the graph data when the file upload is successful and data is received
  //   setlineGraphData(uploadedData);
  // };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-800 text-white">
      <header className="text-center p-4">
        <h3 className="text-3xl font-semibold">
          Welcome to <span className="text-yellow-500">BudgetFriend</span>
        </h3>
        <p className="text-gray-300 mt-3">
          Please upload your CSV by selecting or dragging your file below.
          <br />
          Make sure that your file only contains the <code className="italic text-green-500">Date</code>, <code className="italic text-green-500">Category</code>, and <code className="italic text-green-500">Amount</code> columns.
        </p>
      </header>
      <FileUpload
        onLineChartSuccess={setLineChartData}
        onBarChartSuccess={setBarChartData}
      />
      {lineChartData && <LineGraph data={lineChartData} />}
      {/* {barChartData && <StackedBarChart data={barChartData} />} */}
      {egbarChartData && <StackedBarChart data={egbarChartData} />}
    </div>
  );
}

export default App;
