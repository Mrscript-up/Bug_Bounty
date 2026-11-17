import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

function localPreferencesApi() {
  let preferences = {}

  return {
    name: 'local-preferences-api',
    configureServer(server) {
      server.middlewares.use((request, response, next) => {
        const pathname = new URL(request.url ?? '/', 'http://localhost').pathname
        if (pathname !== '/api/preferences') return next()

        response.setHeader('Content-Type', 'application/json')

        if (request.method === 'GET') {
          response.end(JSON.stringify(preferences))
          return
        }

        if (request.method !== 'PUT') {
          response.statusCode = 405
          response.setHeader('Allow', 'GET, PUT')
          response.end(JSON.stringify({ error: 'Method not allowed' }))
          return
        }

        let body = ''
        request.setEncoding('utf8')
        request.on('data', (chunk) => { body += chunk })
        request.on('end', () => {
          try {
            // INTENTIONAL LAB VULNERABILITY: store the parsed JSON as-is with no key restrictions.
            preferences = JSON.parse(body)
            response.end(JSON.stringify(preferences))
          } catch {
            response.statusCode = 400
            response.end(JSON.stringify({ error: 'Request body must be valid JSON' }))
          }
        })
      })
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), localPreferencesApi()],
  server: {
    host: '127.0.0.1',
    port: 5173
  }
})
