import { ChangeEvent, useState } from 'react';

const Detector = () => {
  const [file, setFile] = useState<File | undefined>();
  const [result, setResult] = useState<string | undefined>();

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = async () => {
    try {
      if (file) {
        const formData = new FormData();
        formData.append('image', file);

        const response = await fetch('http://127.0.0.1:5000/detect-cat', {
          method: 'POST',
          body: formData,
          mode: 'cors'
        });

        const resultFromServer = await response.text();
        console.log('Wynik:', resultFromServer);
        setResult(resultFromServer);

        console.log('File send.');
      } else {
        console.error('No file to send.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange}></input>
      <button className='px-4 py-2 border-[1px] text-orange-500 border-orange-500 rounded-lg shadow-lg hover:scale-125 hover:text-white hover:bg-orange-500 duration-500 font-bold' onClick={handleSubmit}>IS IT?</button>
      {result && <div>Wynik: {result}</div>}
    </div>
  );
};

export default Detector;
