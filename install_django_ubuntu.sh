#!/bin/bash

# Installation d'un environnement de travail Python Django sur Ubuntu

# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation de Python et des outils nécessaires
sudo apt install python3 python3-pip python3-venv -y

# Création d'un environnement virtuel
python3 -m venv .venv
