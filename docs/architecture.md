# Solar Panel Defect & Output Degradation Forecaster

## 1. Project Overview

The project aims to identify defects in solar panels using
drone-based infrared/thermal imagery and forecast potential
power-output degradation.

The system will combine computer vision, machine learning,
environmental data and a web-based dashboard to support
solar panel maintenance decisions.

## 2. Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Frontend | React + Vite | User interface |
| Backend | FastAPI | REST API services |
| Computer Vision | PyTorch | Image analysis |
| Defect Segmentation | AU-Net | Proposed defect localization |
| Forecasting | XGBoost | Power degradation prediction |
| Data Processing | NumPy, Pandas, OpenCV | Data preparation |
| Database | To be finalized | Store scan results |
| Experimentation | Google Colab | Model training |
| Version Control | Git + GitHub | Collaboration |
| Deployment | To be finalized | Cloud hosting |

## 3. High-Level System Architecture

```mermaid
flowchart TD
    A[User] --> B[React Frontend]
    B --> C[FastAPI Backend]
    C --> D[Image Validation]
    D --> E[Computer Vision Model]
    E --> F[Defect Features]
    F --> G[Forecasting Model]
    H[Irradiance and Weather Data] --> G
    G --> I[Power Degradation Forecast]
    I --> J[Results Dashboard]
    C --> K[(Database)]
    J --> B