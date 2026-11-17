import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { Provider } from 'react-redux'
import { BrowserRouter } from 'react-router-dom'
import { store } from './store/store.js'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* Provider فروشگاه Redux را برای همه کامپوننت‌های فرزند در دسترس می‌گذارد. */}
    <Provider store={store}>
      {/* BrowserRouter مسیر صفحه را با نشانی مرورگر هماهنگ می‌کند. */}
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </StrictMode>,
)
