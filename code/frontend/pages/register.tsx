import { useState } from 'react'
import { API_BASE_URL } from '../lib/api'

export default function Register() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    await fetch(`${API_BASE_URL}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    })
  }
  return (
    <form onSubmit={handleSubmit}>
      <h1>Register</h1>
      <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <button type="submit">Register</button>
    </form>
  )
}
