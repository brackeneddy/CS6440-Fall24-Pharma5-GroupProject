import { useState } from "react";


export default function FormComponent() {
  const [formData, setFormData] = useState({
    heart_rate: "",
    oxygen: "",
    activity_level: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const heartRate = formData.heart_rate;
    const oxygen = formData.oxygen;
    const activityLevel = formData.activity_level;

    console.log(`Heart rate: ${heartRate} bpm /// Oxygen: ${oxygen} /// Activity level: ${activityLevel}`);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Heart Rate</label>
          <input type="number" name="heart_rate" onChange={handleChange} /> bpm
        </div>
        <div>
          <label>Oxygen</label>
          <input type="number" name="oxygen" onChange={handleChange} />
        </div>
        <div>
          <label>Activity Level</label>
          <input type="number" name="activity_level" onChange={handleChange} />
        </div>

        <input type="submit" value="Submit" />
      </form>
    </>
  )
}