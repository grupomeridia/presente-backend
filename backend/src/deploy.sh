#! /bin/bash

# Definindo as cores de texto que serão utilizadas
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
WHITE="\e[37m"
RESET="\e[0m"

#Variaveis de instação AWS

PROJECT_NAME="app-presente"
USERNAME="ubuntu"
INSTALLATION_FOLDER="/home/${USERNAME}/${PROJECT_NAME}"
FRONTEND_LINK="git@github.com:grupomeridia/presente-frontend.git"
BACKEND_LINK="git@github.com:grupomeridia/presente-backend.git"

# Inicio do Script
echo -e "${RED} [+] - - 4pp - pr3s3n7 d3pl0y3r - - [+] ${RESET} \n"

echo -e "${YELLOW} ~> Verificando dependencias Linux... ${RESET} \n"
sleep 1

echo -e "${GREEN}"
sudo apt install python3 python3-pip git -y
echo -e "${RESET}"
sleep 1

echo -e "\n ${YELLOW} ~> Criando pastas  ${RESET}"
mkdir -p ${INSTALLATION_FOLDER}
sleep 1

echo -e " \n ${YELLOW} ~> Clonando repositório GIT BACKEND  \n ${RESET}"
sleep 1
cd ${INSTALLATION_FOLDER} && git clone ${BACKEND_LINK}

echo -e "$\n ${YELLOW} ~> Iniciando ambiente virtual... ${RESET}"
sleep 1
python3 -m venv ${INSTALLATION_FOLDER}/venv

echo -e "\n ${YELLOW} ~> Iniciando ambiente virtual e instalando dependências ${RESET}"
sleep 1
source ${INSTALLATION_FOLDER}/venv/bin/activate && pip install -r ${INSTALLATION_FOLDER}/presente-backend/backend/docs/requirements.txt
