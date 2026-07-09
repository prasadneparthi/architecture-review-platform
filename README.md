# AI Architecture Review Platform

## Overview

AI Architecture Review Platform is a web-based application that evaluates software architecture designs using a combination of rule-based analysis and AI-generated recommendations. Users can submit architecture details in JSON format and receive a comprehensive assessment covering multiple quality attributes, including scalability, security, reliability, performance, maintainability, and cost efficiency.

The platform combines deterministic evaluation through predefined architectural rules with AI-powered insights to generate professional architecture review reports.

---

## Features

- User authentication using JWT
- Architecture submission through JSON
- Rule-based architecture evaluation
- Multi-category scoring engine
- AI-generated architecture analysis
- Actionable recommendations
- Dashboard with review statistics
- Review history management
- PDF report generation

---

## Technology Stack

### Backend

- Python
- Django
- Django REST Framework
- MongoDB

### Frontend

- HTML
- Bootstrap 5
- JavaScript

### AI

- Google Gemini API

### Authentication

- JWT Authentication

---

## Architecture

```
User
   │
   ▼
Frontend
   │
   ▼
Django REST API
   │
   ├── Validation Engine
   ├── Rule Engine
   ├── Scoring Engine
   ├── AI Analysis Engine
   ├── PDF Generator
   │
   ▼
MongoDB
```

---

## Project Structure

```
AI-Architecture-Review-Platform/
│
├── architecture_review/
├── review_engine/
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/ai-architecture-review-platform.git

cd ai-architecture-review-platform
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key

DEBUG=True

MONGO_URI=your-mongodb-uri

GEMINI_API_KEY=your-api-key
```

### Run the development server

```bash
python manage.py runserver
```

---

## Workflow

1. Register or log in.
2. Submit architecture details.
3. Validate the submitted data.
4. Execute rule-based evaluation.
5. Generate architecture scores.
6. Obtain AI-generated analysis.
7. View results on the dashboard.
8. Download the review report as a PDF.

---

## Evaluation Categories

- Scalability
- Security
- Reliability
- Performance
- Maintainability
- Cost Efficiency

---

## Future Enhancements

- Architecture diagram upload
- Cloud cost estimation
- Architecture comparison
- Support for multiple cloud providers
- Admin dashboard and analytics
- Docker deployment
- CI/CD integration

---

## License

This project is intended for educational and portfolio purposes.
