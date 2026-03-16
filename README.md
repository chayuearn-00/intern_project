# Monitoring Platform (Intern Project)

A full‑stack monitoring platform for collecting, storing, and visualizing device data. This project was developed during an internship to learn how modern monitoring systems are built using a backend API, databases, and a web dashboard.

## Overview

The system collects device data through MQTT, processes it using a FastAPI backend, stores it in databases, and displays the information on a web dashboard built with Vue and Vite.

## Features

* Device data ingestion using MQTT
* Backend API built with FastAPI
* Storage using PostgreSQL and InfluxDB
* Dashboard interface for monitoring data
* Chart visualization for telemetry data

## Tech Stack

Frontend

* Vue
* Vite
* JavaScript
* Axios

Backend

* FastAPI
* Python

Database

* PostgreSQL
* InfluxDB

Communication

* MQTT
* REST API

## Project Structure

```
intern_project
│
├── backend
│   ├── api
│   ├── models
│   └── services
│
├── frontend
│   ├── components
│   ├── views
│   └── assets
│
└── README.md
```

## Getting Started

### Clone the repository

```
git clone https://github.com/chayuearn-00/intern_project.git
cd intern_project
```

### Backend

Install dependencies

```
pip install -r requirements.txt
```

Run server

```
uvicorn main:app --reload
```

### Frontend

Install dependencies

```
npm install
```

Run development server

```
npm run dev
```

## Learning Outcomes

* Understanding full‑stack system architecture
* Developing APIs using FastAPI
* Working with MQTT for device communication
* Working with time‑series databases
* Building dashboards using Vue

## Author

Chayuda Sukkasem
Kasetsart University
