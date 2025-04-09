# 🐍 python_automacao

Este é um projeto de automação desenvolvido em **Python**, utilizando as bibliotecas **PyAutoGUI** e **pandas**.

O objetivo deste projeto é **automatizar o cadastro de produtos** em um sistema, a partir de uma **lista de dados em formato CSV** (`produtos.csv`).

---

## 💡 Como funciona?

O script realiza as seguintes etapas automaticamente:

1. Acessa o site de testes (criado para fins de estudo):  
   🔗 [https://dlp.hashtagtreinamentos.com/python/intensivao/login](https://dlp.hashtagtreinamentos.com/python/intensivao/login)
2. Realiza o login no sistema.
3. Lê os dados dos produtos no arquivo `produtos.csv`.
4. Cadastra cada produto no sistema, preenchendo os campos um a um.

---

## 🧩 Tecnologias utilizadas

- Python 3
- PyAutoGUI
- pandas

---

## ⚠️ Observações importantes

- Este projeto foi desenvolvido e testado no **macOS**.
- Para rodar em outros sistemas operacionais (Windows, Linux), é necessário:
  - **Adaptar os atalhos de teclado** conforme o seu sistema.
  - **Redefinir as posições do cursor de mouse** utilizadas no código.

Para isso, utilize o script `posicao_cursos.py` para capturar e ajustar as coordenadas de clique da sua máquina.

---

## 🚀 Como rodar o projeto

1. Instale as dependências necessárias:
   ```bash
   pip install pyautogui pandas

