import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import Home from './pages/Home/Home';
import CadastroAluno from './pages/CadastroAluno/cadastro-aluno';
import CadastroTurma from './pages/CadastroTurma/cadastro-turma';
import Options from './pages/Options/Options';
import CadastroProjeto from './pages/CadastroProjeto/cadastro-projeto';
import CadastroProfessor from './pages/CadastroProfessor/cadastro-professor';
import EditarAluno from './pages/editarAluno/editar-aluno';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element = {<Home/>} />
        <Route path='/cadastrar' element = {<CadastroAluno/>} />
        <Route path='/cadastrar-turma' element = {<CadastroTurma/>} />
        <Route path='/options' element = {<Options/>} />
        <Route path='/cadastrar-projeto' element = {<CadastroProjeto/>} />
        <Route path='/cadastrar-professor' element = {<CadastroProfessor/>} />
        <Route path='/editar-aluno' element = {<EditarAluno/>} />
      </Routes>
    </Router>
  );
}

export default App;
