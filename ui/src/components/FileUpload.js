import React, { useState } from 'react';
import axios from 'axios';
import LineGraph from './LineGraph';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [chartData, setChartData] = useState([]); // State to store chart data, null?

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setUploadStatus('Uploading...');
      // TODO { API_ENDPOINT } from "$env/static/private
      const uploadResponse  = await axios.post('http://localhost:5000/upload-csv', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      if (uploadResponse.data.success) {
        setUploadStatus('Upload successful! Fetching data...');
        const chartResponse = await axios.get('http://localhost:5000/linechart');
        setChartData(chartResponse.data);
        setUploadStatus('Data ready.');
      }
    } catch (error) {
        setUploadStatus('Upload failed. Please try again.');
        console.error(error);
    }
  };

  return (
    <div className="container mx-auto mt-5">
      <div className="flex flex-col items-center">
        <input type="file" onChange={handleFileChange} className="mb-6" />
        <button
          onClick={handleUpload}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Upload
        </button>
        {uploadStatus && <p className="mt-3">{uploadStatus}</p>}
        {chartData.length > 0 && <LineGraph data={chartData} />}
      </div>
    </div>
  );
};

export default FileUpload;
