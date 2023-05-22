import styles from './cadastro-aluno.module.css'
import Footer from './Footer';

function cadastroAluno () { 
    return (
        <section class="grid">
			<div class= {styles.login_container}>
                <h1>Cadastro de Aluno</h1>
				<form>
				  <div class={styles.input_container}>
					<label for="login-username">Aluno:</label>
					    <input 
					    type="text" 
					    name="login" 
					    id="login" 
					    placeholder="Nome do Aluno" />
				    </div>
				    <div class={styles.input_container}>
					    <label for="login-username">RA:</label>
					    <input 
					    type="text" 
					    name="login" 
					    id="login" 
					    placeholder="RA do Aluno" />
				    </div>	
				    <div class={styles.input_container}>
					    <label for="login-username">Curso:</label>
					    <input 
					    type="text" 
					    name="login" 
					    id="login" 
					    placeholder="Curso do Aluno" />
				    </div>		  
				  <button class={styles.btn_login}>
					Cadastrar
				  </button>
				</form>
			  </div>
              <Footer/>
        </section>
        
    );
};

export default cadastroAluno;