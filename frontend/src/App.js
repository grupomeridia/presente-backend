import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import Home from './pages/Home/Home';
import CadastroAluno from './pages/CadastroAluno/cadastro-aluno';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element = {<Home/>} />
        <Route path='/cadastrar' element = {<CadastroAluno/>} />
      </Routes>
    </Router>
  );
}

export default App;
