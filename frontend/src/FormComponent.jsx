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

    //TODO: We might need to enable CORS for flask
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        //TODO: Decide on what to do with the response
        const result = await response.json();
        prediction.value = result.prediction;
      } else {
        console.error("Error:", response.statusText);
      }
    } catch (error) {
      console.error("Fetch error:", error);
    }
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Steps</label>
          <input type="number" name="steps" onChange={handleChange} /> steps
        </div>
        <div>
          <label>Exercise</label>
          <input type="number" name="exercise" onChange={handleChange} /> minutes
        </div>
        <div>
          <label>Sedentary Time</label>
          <input type="number" name="sedentary_time" onChange={handleChange} /> hours
        </div>
        <div>
          <label>Heart Rate</label>
          <input type="number" name="resting_heart_rate" onChange={handleChange} /> bpm
        </div>
        <div>
          <label>Calories</label>
          <input type="number" name="calories_burned" onChange={handleChange} /> calories burned
        </div>
        <input type="submit" value="View My Sleep" />
      </form>
    </>
  )
}