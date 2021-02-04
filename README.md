# Gerenciador de produtos

Obs: Dependendo da configuração do docker e docker-compose, será necessário rodar os seguintes comandos como super usuário.

Rodar projeto: `docker-compose up`

Criar usuário root:
 - Abrir segundo terminal enquanto docker é executado, ou utilizar o parâmetro `-d` ao rodar projeto.
 - Rodar comando `docker exec -it {produtos_web_1_conteiner_id} bash`. Obs: o conteiner id da aplicação pode ser visualizado através do comando `docker ps`
 - Rodar comando para criar super usuário: `python manage.py createsuperuser`
 - Preencher dados conforme solicitado.


Rotas:
 - Aplicação: `/`
 - API: `/api`
    - `/api/users/`
    - `/api/products/`
