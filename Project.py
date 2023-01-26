Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import streamlit as st
... 
... login_secreto = 'Pedro.miquelino'
... senha_secreta = '1234567'
... 
... login = st.text_input("Digite seu login: ")
... if (login == login_secreto):
... senha = st.text_input("Digite a senha: ", type='password')
... if (senha == senha_secreta):
... st.success("Login foi feito com sucesso!")
... else:
... st.error("Sua senha está incorreta")
... else:
