
# 📊 Real-Time Machine Metrics Dashboard

A real-time dashboard for monitoring industrial machine metrics such as temperature, vibration, speed, and power consumption. Designed to help factories improve operational efficiency, enable predictive maintenance, and minimize downtime.
> 💻 Built using Python + Streamlit  
> 🌐 Hosted on Streamlit Cloud  
> 🔗 **Live App:** [Click to View](https://real-time-machine-metrics-jd9fzaqdo9f72wje4fbznn.streamlit.app/)

---

## 🚀 Project Features

- 📡 **Real-Time Data Streaming** via MQTT/WebSocket
- 📈 **Live Dashboard** with visualized metrics
- 🚨 **Alert System** for abnormal readings (email/SMS)
- 🧠 **Historical Data** storage and trend analysis
- 🧪 Optional: Predictive maintenance using machine learning

---

## 🛠️ Tech Stack

### Backend
- **Python (FastAPI / Flask)** or **Node.js (Express)**
- **MQTT Broker** (Mosquitto or EMQX)
- **Database:** MongoDB / InfluxDB (time-series)

### Frontend
- **Vue.js** or **React**
- **Chart.js**, **D3.js**, or **Grafana**
- **Tailwind CSS** or **Bootstrap**

---

## 📦 Project Structure

```

real-time-machine-metrics/
├── backend/
│   ├── app.py / index.js
│   ├── routes/
│   ├── models/
│   └── services/
├── frontend/
│   ├── components/
│   ├── views/
│   └── App.vue / App.jsx
├── database/
│   └── setup/
├── mqtt-broker/ (optional docker setup)
├── README.md

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/real-time-machine-metrics.git
cd real-time-machine-metrics
````

### 2. Backend Setup

#### Python (FastAPI/Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Node.js

```bash
cd backend
npm install
npm start
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 4. Run MQTT Broker (Optional)

Using Docker:

```bash
docker run -it -p 1883:1883 eclipse-mosquitto
```

---

## 🧪 Sample Metrics Monitored

| Metric      | Description                   |
| ----------- | ----------------------------- |
| Temperature | Machine operating temp (°C)   |
| Speed       | Motor or spindle RPM          |
| Power Load  | Current power consumption (W) |
| Vibration   | Abnormal vibration detection  |
| Runtime     | Time since last reset/start   |

---

## 📊 Screenshot (Example)

> *Insert a sample screenshot or dashboard mockup here*

---

## 📅 Future Enhancements

* [ ] Role-based authentication
* [ ] Predictive failure analysis with ML
* [ ] Mobile app version
* [ ] Slack/Teams integration for alerts

---

## 📜 License

MIT License. Free to use for personal and commercial projects.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📧 Contact

For support or queries, contact:
**Mosa Siva** — `mosasiva6@gmail.com`

