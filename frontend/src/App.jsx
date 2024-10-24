import { useState } from 'react'
import './App.css'
import FormComponent from './FormComponent'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>OpenHealth</h1>
      <FormComponent />
    </>
  )
}

export default App
