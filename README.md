# AI Fish Health Monitoring System for Marine Cage Aquaculture Farms

## Project Overview

This project uses Artificial Intelligence and Computer Vision to monitor fish health in marine cage aquaculture farms.

The system classifies fish images into:

- Healthy
- Diseased

The goal is to support early disease detection and improve aquaculture management.

---

## Problem Statement

Manual fish health monitoring is difficult in large aquaculture farms. Disease symptoms may go unnoticed, resulting in delayed treatment and economic losses.

This project automates fish health monitoring using AI.

---

## Technologies Used

- Python
- Roboflow
- ResNet50 Classification Model
- Pandas
- Inference SDK
- Power BI

---

## Dataset

Original Dataset:

- Healthy Images: 479
- Diseased Images: 843

After Augmentation:

- Total Images: 2268

Classes:

1. Healthy
2. Diseased

---

## Model Training

Model Type:

- ResNet50 Classification

Performance:

- Precision: 98.1%
- Recall: 93.4%
- F1 Score: 95.6%

---

## System Workflow

Fish Images
↓
Roboflow Model
↓
Python Inference Pipeline
↓
CSV Output
↓
Power BI Dashboard

---

## Milestones Completed

### Milestone 1
System Architecture Design

### Milestone 2
Dataset Annotation and Model Training

### Milestone 3
Python Cage Inference Pipeline

### Milestone 4
Power BI Dashboard Development

### Milestone 5
Business Impact Evaluation

---

## Output

The system generates:

- Fish health predictions
- Confidence scores
- Cage-wise logs
- CSV datasets for Power BI visualization

---

## Future Scope

- Real-time underwater camera integration
- Fish behavior monitoring
- Mortality detection
- Automated alert generation
