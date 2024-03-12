import React from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import './Dictaphone.css';

const Dictaphone = ({ onVoiceInput }) => {
  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition,
  } = useSpeechRecognition();

  if (!browserSupportsSpeechRecognition) {
    return <span>Browser doesn't support speech recognition.</span>;
  }

  const handleVoiceEnd = () => {
    // Process the transcript or send it to the parent component
    onVoiceInput(transcript);
    resetTranscript(); // Reset the transcript after processing
  };

  return (
    <div className="dictaphone-container">
      <p>Micrófono: {listening ? 'Escuchando...' : 'Apagado'}</p>
      <button onClick={() => SpeechRecognition.startListening({ language: 'es-MX' })}>Hablar</button>
      <button onClick={() => { SpeechRecognition.stopListening(); handleVoiceEnd(); }}>Listo</button>
      {/* <button onClick={resetTranscript}>Reset</button> */}
      <p>{transcript}</p>
    </div>
  );
};

export default Dictaphone;
