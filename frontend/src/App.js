import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import Home from './pages/Home/Home';
import CadastroAluno from './pages/CadastroAluno/cadastro-aluno';
import CadastroTurma from './pages/CadastroTurma/cadastro-turma';
<<<<<<< HEAD
import Options from './pages/Options/Options';
=======
import CadastroProjeto from './pages/CadastroProjeto/cadastro-projeto';
import CadastroProfessor from './pages/CadastroProfessor/cadastro-professor';
>>>>>>> 56121d9fd626aed56c231e786965910f18a2df48

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element = {<Home/>} />
        <Route path='/cadastrar' element = {<CadastroAluno/>} />
        <Route path='/cadastrar-turma' element = {<CadastroTurma/>} />
<<<<<<< HEAD
        <Route path='/options' element = {<Options/>} />
=======
        <Route path='/cadastrar-projeto' element = {<CadastroProjeto/>} />
        <Route path='/cadastrar-professor' element = {<CadastroProfessor/>} />
>>>>>>> 56121d9fd626aed56c231e786965910f18a2df48
      </Routes>
    </Router>
  );
}

export default App;
