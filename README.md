# 🎬 Sistema de Locadora

Este projeto simula um sistema de **locadora de filmes e jogos**.
O sistema permite cadastrar clientes, registrar itens (filmes e jogos) e gerenciar o processo de aluguel e devolução.

---

## ⚙️ Funcionalidades principais
<img width="776" height="457" alt="image" src="https://github.com/user-attachments/assets/e1964a9e-e089-4d95-a3b8-15cbf15b71bb" />

- **Cadastrar Cliente** → Adiciona um novo cliente à locadora.  
- **Cadastrar Filme / Jogo** → Registra novos itens.  
- **Listar Itens** → Exibe todos os filmes e jogos cadastrados, mostrando se estão disponíveis ou alugados.  
- **Alugar / Devolver** → Permite controlar quais itens estão em posse dos clientes.  
- **Listar Itens de um Cliente** → Mostra tudo que o cliente tem alugado no momento.  

---

## 📂 Estrutura das Classes

### 🔹 Classe `Locadora`
<img width="953" height="639" alt="image" src="https://github.com/user-attachments/assets/c511b79c-b214-4741-87ec-bd12015869a2" />

- Responsável por gerenciar **clientes** e **itens** (filmes/jogos).
- Principais métodos:
  - `cadastrarCliente(cliente)` → adiciona um cliente.  
  - `cadastrarItem(item)` → registra um filme ou jogo.  
  - `listarItens()` → mostra os itens disponíveis e alugados.  

---

### 🔹 Classe `Item` (classe base)
<img width="1009" height="543" alt="image" src="https://github.com/user-attachments/assets/6e0d1f65-248d-4ca3-92ca-259bafbd8e64" />

- Classe que representa qualquer item alugável.  
- Atributos principais:
  - `codigo` → identificador único.  
  - `titulo` → nome do item.  
  - `disponivel` → controla se está alugado ou não.  
- Métodos:
  - `alugar()` → altera o status para “alugado”.  
  - `devolver()` → altera o status para “disponível”.  

---

### 🔹 Classe `Filme` (herda de `Item`)
<img width="655" height="323" alt="image" src="https://github.com/user-attachments/assets/4fab1ec5-5907-4025-9895-0fe13ffa2a56" />

- Representa um filme.
- Atributos extras:
  - `genero` → gênero do filme (ex.: Ação, Drama).  
  - `duracao` → tempo de duração em minutos.  

---

### 🔹 Classe `Jogo` (herda de `Item`)
<img width="743" height="327" alt="image" src="https://github.com/user-attachments/assets/2a3f218d-e7e7-477e-ac40-bd34d6fcb303" />

- Representa um jogo disponível para aluguel.  
- Atributos extras:
  - `plataforma` → console ou sistema do jogo (ex.: PS5, PC).  
  - `faixaEtaria` → classificação indicativa.  

---

### 🔹 Classe `Cliente`
<img width="1068" height="742" alt="image" src="https://github.com/user-attachments/assets/ab4868f0-349c-4d13-982d-b491d6b69bb5" />

- Representa o cliente que utiliza a locadora.  
- Atributos:
  - `nome` → nome do cliente.  
  - `cpf` → identificação única.  
  - `itensLocados` → lista com os itens atualmente alugados.  
- Métodos:
  - `locar(item)` → cliente aluga um item disponível.  
  - `devolver(item)` → cliente devolve um item que estava alugado.  
  - `listarItens()` → lista todos os itens alugados pelo cliente.  

---

