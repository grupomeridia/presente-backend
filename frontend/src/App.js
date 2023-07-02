import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import Home from './pages/Home/Home';
import CadastroAluno from './pages/CadastroAluno/cadastro-aluno';
import CadastroTurma from './pages/CadastroTurma/cadastro-turma';
import CadastroProjeto from './pages/CadastroProjeto/cadastro-projeto';
import CadastroProfessor from './pages/CadastroProfessor/cadastro-professor';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element = {<Home/>} />
        <Route path='/cadastrar' element = {<CadastroAluno/>} />
        <Route path='/cadastrar-turma' element = {<CadastroTurma/>} />
        <Route path='/cadastrar-projeto' element = {<CadastroProjeto/>} />
        <Route path='/cadastrar-professor' element = {<CadastroProfessor/>} />
      </Routes>
    </Router>
  );
}

export default App;
