import React from 'react'

const sampleKeys = ["user:1:name", "user:1:email", "post:5:title"]

function buildTree(keys: string[]) {
  const tree: Record<string, any> = {}
  keys.forEach(key => {
    const parts = key.split(':')
    let current = tree
    parts.forEach(part => {
      if (!current[part]) {
        current[part] = {}
      }
      current = current[part]
    })
  })
  return tree
}

function renderTree(node: Record<string, any>) {
  return (
    <ul>
      {Object.entries(node).map(([key, value]) => (
        <li key={key}>
          {key}
          {value && Object.keys(value).length > 0 && renderTree(value)}
        </li>
      ))}
    </ul>
  )
}

export default function Dashboard() {
  const tree = buildTree(sampleKeys)
  return (
    <div>
      <h1>Dashboard</h1>
      {renderTree(tree)}
    </div>
  )
}
