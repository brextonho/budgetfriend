import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import LineGraph from './components/LineGraph';
import StackedBarChart from './components/StackedBarChart';

function App() {
  const [lineChartData, setLineChartData] = useState(null);
  const [barChartData, setBarChartData] = useState(null);

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
      {barChartData && <StackedBarChart data={barChartData} />}
    </div>
  )
}

export default App;
