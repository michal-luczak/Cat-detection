#inzynieriaOprogramowania #semestr3 

# Faza 1 - ogólna architektura projektu
Aplikacja oparta na micro-frameworku Flask, w której użytkownik przesyła zdjęcie na serwer i w odpowiedzi dostaje na ile % na zdjęciu znajduje się kot (poszczególne przedziały będą miały inną informację typu 100%-95%: "to *prawie* na pewno jest kot" itd.).

Wyniki oceny będą przechowywane w sesji - będą zapisane do momentu wyłączenia przeglądarki, przez co nie ma potrzeby stawiania bazy danych.