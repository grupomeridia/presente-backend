import logo from '../img/logo-removebg.png';
import styles from './Home.module.css';

function Home () {
    return (
        <body onload="tabela(lista)">
	    <section class={styles.page_content}>
            <section class={styles.search_and_user}>
                <div class={styles.admin_profile }>
                    <span class={styles.greeting}>Hello admin</span>
                    <i class="fa-solid fa-circle-user"></i>
                </div>
            </section>
            <section class={styles.grid}>
                <table id="example">
                    <thead>
                        <tr>
                            <th>Aluno</th>
                            <th>Ra</th>
                            <th>Cursos</th>
                            <th>Ações</th>
                        </tr>
                    </thead>
                    <tbody id="tbody">  
                    </tbody>
                </table>
            </section>
	    </section>
	    <script src="https://kit.fontawesome.com/a146d88807.js" crossorigin="anonymous"></script>
	    <script src="//code.jquery.com/jquery-3.3.1.js"></script>
	    <script src="//cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
	    <script src="{{ url_for('static', filename='js/home-table.js') }}"></script> 
	    <script src="{{ url_for('static', filename='js/toggle-menu.js') }}"></script>
        </body>
    );
}

export default Home;