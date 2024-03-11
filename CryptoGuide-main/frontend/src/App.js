import './App.css';
import Dashboard from './components/dashboard.component';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from './components/navbar.component';
import "bootstrap/dist/css/bootstrap.min.css";
import Footer from './components/footer.component';
import Summarizer from './components/investmentSum.component';
import Home from './components/home.component';
import Trending from './components/trending.component';

function App() {
  return (
    <Router>
    <div className="App" >
    <Navbar />

    <Routes>
      <Route path='/home' element={<Home />}/> 
      {/* this is new */}
      <Route path='/' element={<Dashboard />}/>
      <Route path='/summary' element={<Summarizer />}/>
      <Route path='/trending' element={<Trending />}/>
    </Routes>
    <Footer />
    </div>
    </Router>
  );
}

export default App;