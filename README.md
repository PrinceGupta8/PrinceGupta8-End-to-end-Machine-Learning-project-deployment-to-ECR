

---

```markdown
# 🚀 End-to-End Machine Learning Project: Deployment to AWS ECR

This repository demonstrates a complete end-to-end pipeline for deploying a Machine Learning model using **Docker** and **AWS Elastic Container Registry (ECR)**.

🔗 **Project Link**: [GitHub Repository](https://github.com/PrinceGupta8/PrinceGupta8-End-to-end-Machine-Learning-project-deployment-to-ECR)

---

## 🧠 Project Objective

Build a full Machine Learning pipeline — from data preprocessing, training, and model evaluation to packaging and **containerized deployment** using AWS ECR.

---

## 🔨 Technologies Used

- **Python 3.8+**
- **Pandas**, **Scikit-learn**
- **Docker**
- **AWS ECR**
- **Flask** (for API deployment)
- **MLflow / DVC / CI-CD (optional extension)**

---

## 📁 Repository Structure

```

├── src/
│   ├── Pipeline/
│   │   └── predict\_pipeline.py      # Prediction logic
│   ├── Exception.py                 # Custom exception class
│   ├── logger.py                    # Logging utility
├── templates/
│   ├── index.html                   # Landing page
│   └── home.html                    # Prediction form page
├── Dockerfile                       # Container definition
├── requirements.txt                 # Python dependencies
├── app.py                           # Flask app
├── .gitignore
└── README.md                        # Project documentation

````

---

## 📦 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/PrinceGupta8/PrinceGupta8-End-to-end-Machine-Learning-project-deployment-to-ECR.git
cd PrinceGupta8-End-to-end-Machine-Learning-project-deployment-to-ECR
````

### 2. Create Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python app.py
```

Visit `http://localhost:8080` in your browser.

---

## 🐳 Docker Integration

### Build Docker Image

```bash
docker build -t student-performance .
```

### Run Docker Container

```bash
docker run -p 8080:8080 student-performance
```

---

## ☁️ AWS ECR Deployment

### 1. Authenticate with ECR

```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com
```

### 2. Tag Your Image

```bash
docker tag student-performance:latest <ecr_repo_url>:latest
```

### 3. Push to ECR

```bash
docker push <ecr_repo_url>:latest
```

Now your ML app is ready for deployment using ECS, EC2, or AWS Fargate.

---

## 📊 Prediction Pipeline Flow

```text
User Input Form → CustomData class → DataFrame → PredictionPipeline → Trained ML Model → Result Display
```

---

## 🌐 Web UI Screens

* `/` → Welcome page (`index.html`)
* `/predictdata` → Form to enter student data and view prediction (`home.html`)

---

## 📈 Sample Input

* Gender: male / female
* Race/Ethnicity: Group A, B, C, D, E
* Parental Level of Education: some college, associate’s degree, etc.
* Lunch: standard / free-reduced
* Test Preparation Course: none / completed
* Math Score: float
* Reading Score: float

---

## 🧠 Author

**Prince Gupta**
AI Engineer | ML Developer | Tech Visionary
📧 [princegupta995643@gmail.com](mailto:princegupta995643@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/prince-gupta-a8129a209/)

---

## 🏷️ License

This project is licensed under the MIT License.
Feel free to use and contribute 🤝

---

## 🙌 Acknowledgements

* [UCI ML Repository – Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/student+performance)
* Flask, Docker, and AWS Documentation
* Open-source community ❤️

---

## 📌 Future Improvements

* Integrate CI/CD using GitHub Actions
* Store model artifacts with DVC
* Use MLflow for experiment tracking
* Deploy on AWS Fargate with load balancer
* Add API endpoints for mobile or third-party integration

---

