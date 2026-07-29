# API YOLO avec FastAPI

## Description

Ce projet expose un modèle YOLOv8 à travers une API FastAPI permettant de détecter des objets dans une image.

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn app:app --reload
```

Le serveur est accessible sur :

```
http://127.0.0.1:8000
```

## Endpoint

**POST** `/predict`

Retourne un JSON contenant les objets détectés dans l'image.

## Exemple avec cURL

```bash
curl.exe -X POST "http://127.0.0.1:8000/predict" -F "file=@C:\Users\plava\Downloads\IMG_5251.jpg"
```