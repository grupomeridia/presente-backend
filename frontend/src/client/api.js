import axios from "axios";

const httpClient = axios.create({
    baseURL: "http://localhost:5000",
});

const api = {
    aluno: {
        findById:(id) => httpClient.get('/api/aluno',id),
        listAll: () => httpClient.get('/api/aluno/listAll'),
        create: (alunoData) => httpClient.post('/api/aluno',alunoData),
        update: (id,alunoData) => httpClient.put('/api/aluno',id,alunoData),
        delete: (id) => httpClient.delete('/api/aluno',id),
     },
     chamada: {
        findById: (id) => httpClient.get('api/chamada',id),
        listAll: () => httpClient.get('/api/chamada/listAll'),
        create: (chamadaData) => httpClient.post('/api/chamada',chamadaData),
        update: (id, chamaData) =>httpClient.put('/api/chamada',id,chamaData),
        delete: (id) => httpClient.delete('/api/chamada',id),
     },
     configuracao:{
        findById: (id) => httpClient.get('api/configuracao',id),
        listAll: () => httpClient.get('api/configuracao/listAll'),
        create: (configuracaoData) => httpClient.post('/api/configuracao', configuracaoData),
        update: (id, configuracaoData) => httpClient.put('/api/configuracao/',id,configuracaoData),
        delete: (id) => httpClient.delete('/api/configuracao/', id ),
     },
     presenca:{
        findById: (id) => httpClient.get('api/presenca',id),
        listAll: () => httpClient.get('api/presenca/listAll'),
        create: (presencaData) => httpClient.post('/api/presenca',presencaData),
        update: (id, presencaData) => httpClient.put('/api/presenca',id,presencaData),
        delete: (id) => httpClient.delete('/api/presenca',id),
     },
     professor:{
        findById: (id) => httpClient.get('api/professor',id),
        listAll: () => httpClient.get('api/professor/listAll'),
        create: (professorData) => httpClient.post('/api/professor',professorData),
        update: (id, professorData) => httpClient.put('/api/professor',id,professorData),
        delete: (id) => httpClient.delete('/api/professor',id),
     },
     projeto:{
        findById: (id) => httpClient.get('api/projeto',id),
        listAll: () => httpClient.get('api/projeto/listAll'),
        create: (projetoData) => httpClient.post('/api/projeto',projetoData),
        update: (id, projetoData) => httpClient.put('/api/projeto',id,projetoData),
        delete: (id) => httpClient.delete('/api/projeto',id),
     },
     turma: {
        findById: (id) => httpClient.get('api/turma',id),
        listAll: () => httpClient.get('api/turma/listAll'),
        create: (turmaData) => httpClient.post('/api/turma',turmaData),
        update: (id, turmaData) => httpClient.put('/api/turma',id,turmaData),
        delete: (id) => httpClient.delete('/api/turma',id),
     }

};

export default api;