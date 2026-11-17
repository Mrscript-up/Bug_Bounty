# Mini Shop React Labs

Mini Shop is a small React storefront for practicing components, props, state, Redux Toolkit, and React Router. It also includes local security exercises that demonstrate unsafe HTML rendering, URL handling, and server-rendered state serialization.

## Requirements

- Node.js and npm

## Install and run

From the project directory, install dependencies and start the React app:

```sh
npm install
npm run dev
```

Open the local address printed by Vite (normally <http://127.0.0.1:5173>).

The server-rendering security exercises run as a separate process. In a second terminal, from the same project directory, run:

```sh
npm run lab
```

Open <http://127.0.0.1:3000/profile>. Both servers bind to loopback for local use. Keep these intentionally vulnerable exercises on your own machine; do not expose them to a public or shared network.

Stop either server with **Ctrl+C**. Preferences and profile data are held in memory, so restarting the relevant server clears them.

## React app pages

| Path | What to explore |
| --- | --- |
| `/` | Product highlights, a local-state click counter, and the unsafe HTML preview lab |
| `/products` | Product search, reusable product cards, and adding items to the cart |
| `/product/:id` | Dynamic route parameters and a product detail page |
| `/cart` | Shared Redux cart state, quantity controls, and the demo checkout |
| `/preferences` | JSON editing, a local API, and the intentionally unsafe props injection exercise |
| `/about` | A second product-listing page |

Unknown paths show a not-found page. The checkout is only a demo: it clears the cart and returns to the product list; it does not place a real order.

## Security labs

These examples are intentionally vulnerable. Use the payloads only on the local app or lab server described above.

### 1. HTML preview on the home page

On `/`, enter this in the **Your text** field:

```html
<img src=x onerror=alert(1)>
```

The preview assigns the text to `innerHTML`, so the browser interprets it as markup and runs the event handler. This is a client-side HTML injection / XSS example. Compare it with rendering user text as ordinary React text, which treats the input as text rather than markup. The relevant code is in `RefPreviewLab` in `src/pages/Home.jsx`.

### 2. Preferences props injection

Open `/preferences`, replace the editor contents with this JSON, and save:

```json
{"dangerouslySetInnerHTML":{"__html":"<img src=x onerror=alert(1)>"}}
```

The local API accepts the JSON object and the page spreads its properties onto a DOM element. React's `dangerouslySetInnerHTML` prop causes the supplied HTML to be interpreted. This demonstrates why API data should be validated and should not be spread directly onto DOM elements. The page is in `src/pages/Preferences.jsx`; the local in-memory API is configured in `vite.config.js`.

### 3. Stored profile link and server-rendered state

The profile lab has vulnerable and safer versions at `/profile` and `/profile-safe`.

- **Link scheme:** On `/profile`, enter `javascript:alert(document.domain)` as the website link, save, then click **Visit my website**. The link is rendered without checking its URL scheme. `/profile-safe` accepts only absolute `http:` and `https:` links and blocks other schemes. Both pages share the same in-memory profile, so the safe page also refuses to render an unsafe link saved through the vulnerable page.
- **State serialization:** On `/profile`, enter this as the bio and save:

  ```html
  </script><script>alert(document.domain)</script>
  ```

  Reload the page to see how inserting `JSON.stringify()` output directly into a script element can let a bio terminate that element. `/profile-safe` escapes characters that could close the script element before embedding the state.

### 4. Redirect URL handling

The profile pages include a redirect form. Enter `javascript:alert(document.domain)` and submit it to compare the routes:

- `/redirect` assigns the supplied query parameter to `window.location` without checking its scheme.
- `/redirect-safe` allows only absolute `http:` and `https:` URLs and displays a blocked message for other schemes or malformed URLs.

The profile form links to the matching vulnerable or safe redirect route. The implementation is in `server.js`.

## Learning guide

| Topic | Files to read |
| --- | --- |
| Reusable components and props | `src/components/ProductCard.jsx`, `src/components/CartItem.jsx` |
| Parent state and callback props | `src/pages/Products.jsx`, `src/components/SearchBox.jsx` |
| Local state and re-rendering | `src/pages/Home.jsx` |
| Redux actions, reducers, and store | `src/store/cartSlice.js`, `src/store/store.js`, `src/main.jsx` |
| Routing and dynamic route parameters | `src/App.jsx`, `src/components/Navbar.jsx`, `src/pages/ProductDetails.jsx` |
| Product sample data | `src/data/products.js` |
| Preferences API and props exercise | `vite.config.js`, `src/pages/Preferences.jsx` |
| Server-rendered security exercises | `server.js` |

## Available commands

```sh
npm run dev      # Start the React app and local preferences API
npm run lab      # Start the profile and redirect security lab on port 3000
npm run build    # Build the React app for production
npm run preview  # Preview the production build
npm run lint     # Run ESLint
```
