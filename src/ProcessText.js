import React, { useState } from 'react';
import Dictaphone from './Dictaphone';
import './App.css'; // Import the CSS file

const App = () => {
  const [result, setResult] = useState('');

  const handleVoiceInput = async (voiceText) => {
    try {
      const response = await fetch('http://localhost:5000/process_text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text_input: voiceText }),
      });

      const data = await response.json();
      setResult(data.processed_text);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="app-container"> {/* Add a class to the main container */}
      <Dictaphone onVoiceInput={handleVoiceInput} />
      <p className="result-text">Recomendaciones:</p>
      <p className="result-text">{result}</p>
    </div>
  );
};

export default App;
