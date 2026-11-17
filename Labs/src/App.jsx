import { Route, Routes } from 'react-router-dom'
import Navbar from './components/Navbar.jsx'
import Hgome from './pages/Home.jsx'
import Products from './pages/Products.jsx'
import ProductDetails from './pages/ProductDetails.jsx'
import Cart from './pages/Cart.jsx'
import NotFound from './pages/NotFound.jsx'
import About from './pages/about.jsx'
import Preferences from './pages/Preferences.jsx'
import './App.css'

function App() {
  return (
    <div className="app-shell">
      <Navbar />

      <main className="page-container">
        {/* این مسیرها با React Router صفحه متناسب با نشانی مرورگر را نمایش می‌دهند. */}
        <Routes>
          <Route path="/" element={<Hgome />} />
          <Route path="/products" element={<Products />} />
          <Route path="/product/:id" element={<ProductDetails />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/preferences" element={<Preferences />} />
          <Route path="*" element={<NotFound />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </main>

      <footer className="site-footer">
        <p>Mini Shop · A small app for learning React</p>
      </footer>
    </div>
  )
}

export default App
