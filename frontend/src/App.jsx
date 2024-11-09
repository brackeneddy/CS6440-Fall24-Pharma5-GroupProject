import { useState } from 'react'
import './App.css'
import FormComponent from './FormComponent'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div className='bg-gray-100 min-h-screen min-w-screen p-16'>
      <h1 className="text-6xl font-extrabold text-blue-600">
        OpenHealth
      </h1>
      <FormComponent />
      <div id="output"></div>
    </div>
    </>
  )
}

export default App
