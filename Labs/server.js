import { createServer } from 'node:http'
import { createElement as h } from 'react'
import { renderToString } from 'react-dom/server'

const profile = {
  bio: 'Hello! Edit this bio to try the lab.',
  websiteUrl: '',
}
const port = Number(process.env.PORT || 3000)

function getAllowedWebUrl(value) {
  try {
    const parsed = new URL(value)
    return parsed.protocol === 'http:' || parsed.protocol === 'https:' ? parsed.href : null
  } catch {
    return null
  }
}

function escapeHtmlAttribute(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
}

function ProfilePage({ bio, websiteUrl, safe, error }) {
  const pageName = safe ? 'Safe profile' : 'Vulnerable profile'
  const safeWebsiteUrl = safe ? getAllowedWebUrl(websiteUrl) : null

  return h(
    'main',
    { className: 'card' },
    h('p', { className: 'eyebrow' }, 'LOCAL SSR SECURITY LAB'),
    h('h1', null, pageName),
    h(
      'p',
      { className: 'description' },
      safe
        ? 'The website link only renders for absolute HTTP(S) URLs. Profile state is also safely serialized.'
        : 'The website URL is stored and rendered into an href without checking its scheme. The bio also demonstrates unsafe state serialization.',
    ),
    error
      ? h('p', { className: 'error', role: 'alert' }, 'That URL was not saved. Enter an absolute http:// or https:// URL.')
      : null,
    h(
      'form',
      { method: 'post' },
      h('label', { htmlFor: 'bio' }, 'Bio'),
      h('textarea', { id: 'bio', name: 'bio', rows: 5, defaultValue: bio }),
      h('label', { htmlFor: 'websiteUrl' }, 'Website or profile link'),
      h('input', {
        id: 'websiteUrl',
        name: 'websiteUrl',
        type: 'text',
        autoComplete: 'url',
        placeholder: 'https://example.com or javascript:alert(document.domain)',
        defaultValue: websiteUrl,
      }),
      h('button', { type: 'submit' }, 'Save bio and link'),
    ),
    h(
      'section',
      { className: 'preview' },
      h('h2', null, 'Rendered profile'),
      h('p', null, bio),
      safe
        ? safeWebsiteUrl
          ? h('a', { href: safeWebsiteUrl }, 'Visit my website')
          : h('p', { className: 'muted' }, websiteUrl ? 'Blocked: safe links require an absolute HTTP(S) URL.' : 'No website link saved yet.')
        : websiteUrl
          // VULNERABLE: no scheme validation, allows javascript: URI XSS.
          ? h('span', {
              dangerouslySetInnerHTML: {
                __html: `<a href="${escapeHtmlAttribute(websiteUrl)}">Visit my website</a>`,
              },
            })
          : h('p', { className: 'muted' }, 'No website link saved yet.'),
    ),
    h(
      'section',
      { className: 'preview' },
      h('h2', null, safe ? 'Safe redirect demo' : 'Vulnerable redirect demo'),
      h(
        'form',
        { method: 'get', action: safe ? '/redirect-safe' : '/redirect' },
        h('label', { htmlFor: 'redirectUrl' }, 'URL to redirect to'),
        h('input', {
          id: 'redirectUrl',
          name: 'url',
          type: 'text',
          placeholder: 'https://example.com or javascript:alert(document.domain)',
        }),
        h('button', { type: 'submit' }, 'Try redirect'),
      ),
    ),
    h(
      'nav',
      null,
      h('a', { href: '/profile' }, 'Vulnerable page'),
      h('span', { 'aria-hidden': true }, ' · '),
      h('a', { href: '/profile-safe' }, 'Safe page'),
    ),
    h('p', { className: 'muted' }, 'Redirect routes: /redirect and /redirect-safe.'),
  )
}

function serializeSafely(value) {
  return JSON.stringify(value)
    .replace(/</g, '\\u003c')
    .replace(/>/g, '\\u003e')
    .replace(/\//g, '\\u002f')
}

function renderProfile(safe, error = false) {
  const state = { bio: profile.bio, websiteUrl: profile.websiteUrl }
  const page = renderToString(
    h(ProfilePage, {
      bio: profile.bio,
      websiteUrl: profile.websiteUrl,
      safe,
      error,
    }),
  )

  let stateScript
  if (safe) {
    stateScript = `<script>window.__INITIAL_STATE__ = ${serializeSafely(state)};</script>`
  } else {
    // VULNERABLE: JSON.stringify() does not escape </script>, allowing stored XSS via the bio field.
    stateScript = `<script>window.__INITIAL_STATE__ = ${JSON.stringify(state)};</script>`
  }

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>${safe ? 'Safe' : 'Vulnerable'} SSR profile lab</title>
    <style>
      :root { color-scheme: light; font-family: system-ui, sans-serif; color: #20251f; background: #f3f5f1; }
      body { margin: 0; padding: 40px 18px; }
      .card { max-width: 620px; margin: 0 auto; padding: 32px; background: white; border: 1px solid #dce3da; border-radius: 16px; box-shadow: 0 12px 32px #26362612; }
      .eyebrow { color: #52734d; font-size: .75rem; font-weight: 700; letter-spacing: .12em; }
      h1 { margin: 8px 0; }
      .description { color: #5f685e; }
      label { display: block; margin: 24px 0 8px; font-weight: 600; }
      textarea, input { box-sizing: border-box; width: 100%; padding: 12px; border: 1px solid #bdc8ba; border-radius: 8px; font: inherit; }
      button { margin-top: 12px; padding: 10px 16px; border: 0; border-radius: 8px; background: #42683c; color: white; font: inherit; cursor: pointer; }
      .preview { margin: 28px 0; padding: 16px; background: #f6f8f5; border-radius: 8px; overflow-wrap: anywhere; }
      .preview h2 { margin-top: 0; font-size: 1rem; }
      .preview p { white-space: pre-wrap; }
      .error { padding: 10px 12px; border-radius: 8px; background: #fff0ed; color: #9a392b; }
      .muted { color: #687066; }
    </style>
  </head>
  <body>
    ${stateScript}
    <div id="root">${page}</div>
  </body>
</html>`
}

function renderRedirectPage(safe) {
  const redirectScript = safe
    ? `
      const candidate = new URLSearchParams(window.location.search).get('url') || '';
      const status = document.getElementById('status');
      try {
        const parsed = new URL(candidate);
        if (parsed.protocol === 'http:' || parsed.protocol === 'https:') {
          window.location = parsed.href;
        } else {
          status.textContent = 'Blocked: only absolute HTTP(S) URLs are allowed.';
        }
      } catch {
        status.textContent = 'Blocked: only absolute HTTP(S) URLs are allowed.';
      }
    `
    : `
      // VULNERABLE: no scheme validation, allows javascript: and data: URI execution.
      const userSuppliedUrl = new URLSearchParams(window.location.search).get('url');
      window.location = userSuppliedUrl;
    `

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>${safe ? 'Safe' : 'Vulnerable'} redirect lab</title>
    <style>
      :root { color-scheme: light; font-family: system-ui, sans-serif; color: #20251f; background: #f3f5f1; }
      body { margin: 0; padding: 40px 18px; }
      main { max-width: 620px; margin: 0 auto; padding: 32px; background: white; border: 1px solid #dce3da; border-radius: 16px; }
    </style>
  </head>
  <body>
    <main>
      <h1>${safe ? 'Safe' : 'Vulnerable'} redirect</h1>
      <p id="status">${safe ? 'Checking the URL…' : 'Redirecting…'}</p>
      <p><a href="/profile${safe ? '-safe' : ''}">Back to profile</a></p>
    </main>
    <script>${redirectScript}</script>
  </body>
</html>`
}

const server = createServer(async (request, response) => {
  const url = new URL(request.url, 'http://127.0.0.1')
  const safe = url.pathname === '/profile-safe'
  const isProfilePath = safe || url.pathname === '/profile'

  if (request.method === 'GET' && url.pathname === '/') {
    response.writeHead(302, { Location: '/profile' }).end()
    return
  }

  if (request.method === 'POST' && isProfilePath) {
    let body = ''
    for await (const chunk of request) body += chunk
    const form = new URLSearchParams(body)
    const websiteUrl = form.get('websiteUrl') ?? ''

    if (safe && websiteUrl && !getAllowedWebUrl(websiteUrl)) {
      response.writeHead(303, { Location: `${url.pathname}?error=invalid-url` }).end()
      return
    }

    profile.bio = form.get('bio') ?? ''
    profile.websiteUrl = websiteUrl
    response.writeHead(303, { Location: url.pathname }).end()
    return
  }

  if (request.method === 'GET' && isProfilePath) {
    response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' })
    response.end(renderProfile(safe, url.searchParams.get('error') === 'invalid-url'))
    return
  }

  if (request.method === 'GET' && url.pathname === '/redirect') {
    response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' })
    response.end(renderRedirectPage(false))
    return
  }

  if (request.method === 'GET' && url.pathname === '/redirect-safe') {
    response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' })
    response.end(renderRedirectPage(true))
    return
  }

  response.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }).end('Not found')
})

server.listen(port, '127.0.0.1', () => {
  console.log(`SSR profile lab running at http://127.0.0.1:${port}`)
})
