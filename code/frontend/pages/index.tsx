import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Redis Supreme</h1>
      <ul>
        <li><Link href="/register">Register</Link></li>
        <li><Link href="/login">Login</Link></li>
      </ul>
    </div>
  )
}
