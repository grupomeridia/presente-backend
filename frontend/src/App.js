import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import Home from './pages/Home/Home';
import CadastroAluno from './pages/CadastroAluno/cadastro-aluno';
import CadastroTurma from './pages/CadastroTurma/cadastro-turma'

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element = {<Home/>} />
        <Route path='/cadastrar' element = {<CadastroAluno/>} />
        <Route path='/cadastrar-turma' element = {<CadastroTurma/>} />
      </Routes>
    </Router>
  );
}

export default App;
