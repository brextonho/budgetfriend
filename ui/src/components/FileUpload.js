import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');

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
      const response = await axios.post('/upload-csv', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setUploadStatus('Upload successful!');
      console.log(response.data);
      // Handle the response data here, like setting it to state or context
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
      </div>
    </div>
  );
};

export default FileUpload;
