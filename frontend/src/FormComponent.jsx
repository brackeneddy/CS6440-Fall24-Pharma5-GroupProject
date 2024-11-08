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
      <div className="max-w-md mx-auto mt-10">
        <form
          onSubmit={handleSubmit}
          className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
        >
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Heart Rate
            </label>
            <div className="flex items-center">
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="number"
                name="heart_rate"
                onChange={handleChange}
              />
              <span className="ml-2 text-gray-700">bpm</span>
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Oxygen
            </label>
            <input
              className="shadow appearance-none border rounded flex-1 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              type="number"
              name="oxygen"
              onChange={handleChange}
            />
            <span className="ml-2 text-gray-700">%</span>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Activity Level
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              type="number"
              name="activity_level"
              onChange={handleChange}
            />
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