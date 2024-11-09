import { useState } from "react";


export default function FormComponent() {
  const [formData, setFormData] = useState({
    steps: "",
    exercise: "",
    sedentary_time: "",
    resting_heart_rate: "",
    calories_burned: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://3.84.94.140:5000/predict-sleep-score', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const result = await response.json();
        const sleepScore = result.sleep_score;
        const outputContainer = document.getElementById("output");
        outputContainer.innerHTML = `
            <h2>Your sleep score is:</h2>
            <p>${sleepScore}</p>
        `;
        console.log('sleep score:', result.sleep_score);
      } else {
        console.error("Error:", response.statusText);
      }
    } catch (error) {
      console.error("Fetch error:", error);
    }
  }

  return (
    <>
      <div className="max-w-md mx-auto mt-10">
        <form
          onSubmit={handleSubmit}
          className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
        >
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Steps
            </label>
            <div className="flex items-center">
              <input 
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="number" 
                name="TotalSteps" 
                onChange={handleChange} 
                />
              <span className="ml-2 text-gray-700">steps</span>
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Sedentary Time
            </label>
            <div className="flex items-center">
              <input 
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="number" 
                name="SedentaryMinutes" 
                onChange={handleChange} 
                />
              <span className="ml-2 text-gray-700">minutes</span>
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Fairly Active Minutes
            </label>
            <div className="flex items-center">
              <input 
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="number" 
                name="FairlyActiveMinutes" 
                onChange={handleChange} 
                />
              <span className="ml-2 text-gray-700">minutes</span>
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Very Active Minutes
            </label>
            <div className="flex items-center">
              <input 
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="number" 
                name="VeryActiveMinutes" 
                onChange={handleChange} 
                />
              <span className="ml-2 text-gray-700">minutes</span>
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Resting Heart Rate
            </label>
            <div className="flex items-center">
              <input 
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="number" 
                name="resting_heart_rate" 
                onChange={handleChange} 
                />
              <span className="ml-2 text-gray-700">bpm</span>
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Calories
            </label>
            <div className="flex items-center">
              <input 
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="number" 
                name="Calories" 
                onChange={handleChange} 
                />
              <span className="ml-2 text-gray-700">calories burned</span>
            </div>
          </div>
          <div className="flex items-center justify-end">
            <input
              type="submit"
              value="Submit"
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            />
          </div>
        </form>
      </div>
    </>
  )
}