import Navbar from './components/navbar';
import MyRanges from './Pages/myRanges';
import TrainRanges from './Pages/trainRanges';
import TrainHands from './Pages/trainHands';
import { Route, Routes } from 'react-router-dom';

function App() {
    return (
        <>
            <Navbar />

            <div className="container">
                <Routes>
                    <Route path="/" element={<MyRanges />} />
                    <Route path="/my-ranges" element={<MyRanges />} />
                    <Route path="/train-ranges" element={<TrainRanges />} />
                    <Route path="/train-hands" element={<TrainHands />} />
                </Routes>
            </div>
        </>
    )
}

export default App;