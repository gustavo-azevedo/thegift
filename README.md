# Streamlit web app

## install

### 1. Create venv

```bash
python3 -m venv venv
```

### 2. Activate venv

on linux / mac

```bash
source venv/bin/activate
```

or Windows

```bash
venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run app

```bash
streamlit run app.py --client.showErrorDetails=false
```

## Pre-Deploy

Para ambiente de produção, é ncessário trocar no projeto as variaveis com valor "http://localhost:8501" pela URL do servidor de produção.
Além disso é necessário atualizar na conta [Google Cloud Platformn](https://console.cloud.google.com/apis/credentials?project=the-gift-425823&supportedpurview=project), na area das credenciais do projeto, as URLs autorizadas a utilizar. Atualmente esta a http://localhost:8501 mas tb deve ser trocada pelo endereço do servidor.

O App usa o [firestore](https://console.firebase.google.com/project/thegift-ad01d/firestore/databases/-default-/data/~2Fusers~2F108149051185534806503?view=panel-view&query=1%7CLIM%7C3%2F100&scopeType=collection&scopeName=%2Fusers) como database

A conta do google cloud e a conta do Firebase estao vinculadas ao mesmo email gmail (app.thegift@gmail.com)#   t h e g i f t  
 