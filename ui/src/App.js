import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import LineGraph from './components/LineGraph';

function App() {
  const [graphData, setGraphData] = useState(null);
  
  // TODO delete Mock data for the sake of demonstration
  // Replace this with the actual data received from the backend after successful file upload
  const exampleData = [
    { Month: 'January 2019', TotalExpenditure: 2457.76 },
    { Month: 'February 2019', TotalExpenditure: 3299.60 },
    { Month: 'March 2019', TotalExpenditure: 2457.76 },
    { Month: 'April 2019', TotalExpenditure: 3299.60 },
    { Month: 'May 2019', TotalExpenditure: 2457.76 },
    { Month: 'June 2019', TotalExpenditure: 3299.60 },
  ];

  const handleFileUploadSuccess = (uploadedData) => {
    // Set the graph data when the file upload is successful and data is received
    setGraphData(uploadedData);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-800 text-white">
      <header className="text-center p-4">
        <h3 className="text-3xl font-semibold">
          Welcome to <span className=" text-yellow-500">BudgetFriend</span>
        </h3>
        <p className="text-gray-300 mt-3">
          Please upload your CSV by selecting or dragging your file below.
          <br />
          Make sure that your file only contains the <code className="italic text-green-500">Date,Category</code>, and <code className="italic text-green-500">Amount</code> columns.
        </p>
      </header>
      <FileUpload onSuccess={handleFileUploadSuccess} />
      {graphData && <LineGraph data={graphData} />}




    </div>
  );
}

export default App;