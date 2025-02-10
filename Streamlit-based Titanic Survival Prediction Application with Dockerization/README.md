# Streamlit-based Titanic Survival Prediction Model with Docker

## 📌 Project Overview
The **Titanic Survival Prediction Model** is a machine learning application that predicts whether a passenger would have survived the Titanic disaster based on input parameters. The project is built using **Python, scikit-learn, pandas**, and features a **Streamlit web interface**. To ensure seamless deployment and portability, **Docker** is used to containerize the application.

---

## 📁 Project Structure

```
Titanic-Prediction-Model/
│── Dockerfile
│── requirements.txt
│── main.py
│── titanic_model.py
│── titanic_model.pkl
```

### 🔹 Description of Files:
- **main.py** – The Streamlit-based web application for user interaction.
- **titanic_model.py** – Script to train and save the Titanic survival prediction model.
- **titanic_model.pkl** – Serialized ML model for making predictions.
- **requirements.txt** – List of dependencies needed to run the application.
- **Dockerfile** – Configuration file for containerizing the application using Docker.

---

## 🤖 Training the AI: From Data to Predictions ('titanic_model.py')
The model is trained using a **Random Forest Classifier** from **scikit-learn** on Titanic dataset features. After training, it is saved as `titanic_model.pkl` using **joblib** for efficient storage and loading in the web application.

### 🔹 Steps in `titanic_model.py`:
1. Load the Titanic dataset.
2. Preprocess missing values and encode categorical data.
3. Train the Random Forest model.
4. Save the trained model as `titanic_model.pkl`.

---

## 🎨 Streamlit Application (`main.py`)
The **Streamlit app** provides an intuitive user interface where users can enter passenger details and get a survival prediction. Custom **CSS styles** enhance the UI/UX for a professional look.

---

## 🐳 Docker Setup
The application is containerized using **Docker** for easy deployment. The `Dockerfile` ensures that all dependencies are installed inside the container.

### 🔹 Steps to Run the Application with Docker:
1. Navigate to the project directory:
   ```sh
   cd Titanic-Prediction-Model
   ```
2. Build the Docker image:
   ```sh
   docker build -t titanic-prediction .
   ```
3. Run the container:
   ```sh
   docker run -p 8501:8501 titanic-prediction
   ```
4. Open a browser and access the application at:
   ```
   http://localhost:8501
   ```

---

## 🚀 Future Enhancements
- Deploy the **Dockerized app** to **AWS/GCP/Vercel**.
- Improve the UI with **interactive visualizations**.
- Enhance model accuracy using **feature engineering**.

---

## 🏆 Conclusion
This project showcases a **complete pipeline** for deploying a **machine learning model** using **Streamlit and Docker**. It provides an intuitive way for users to interact with the model, and containerization ensures easy portability and deployment.

---

## 📌 Author
**Tarak Katoch**

## 📜 License
**MIT**

## 🤝 Contributions
Feel free to fork and contribute!

---

🎉 **Happy Coding!** 🚀
