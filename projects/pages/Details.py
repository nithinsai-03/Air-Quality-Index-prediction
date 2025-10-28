import streamlit as st

st.set_page_config(page_title="Air Pollution Details", page_icon="📘")

st.title("📘 Details About Air Pollution")
st.markdown("---")

st.markdown("""
### 🌫️ What is Air Pollution?
Air pollution occurs when harmful substances such as gases, dust, and smoke enter the atmosphere, affecting human health and the environment.  
The Air Quality Index (AQI) helps quantify this pollution in a standardized way.

---

## 🧪 Key Air Quality Parameters Explained
Below are the main pollutants used in AQI calculation and their significance:

---

### 🧬 1. **CO (Carbon Monoxide)**
- **Source:** Vehicle emissions, burning of fuel, industrial processes.  
- **Effect:** Reduces oxygen delivery in the body; harmful at high levels.  
- **Typical Safe Limit:** ≤ 1 ppm (good air quality).

---

### 🌞 2. **O₃ (Ozone)**
- **Source:** Formed by reaction between sunlight and vehicle/industrial pollutants.  
- **Effect:** Irritates lungs, aggravates asthma, reduces lung function.  
- **Typical Safe Limit:** ≤ 50 ppb (good air quality).

---

### 🧫 3. **NO₂ (Nitrogen Dioxide)**
- **Source:** Combustion of fossil fuels, vehicles, power plants.  
- **Effect:** Causes respiratory problems and contributes to smog formation.  
- **Typical Safe Limit:** ≤ 40 µg/m³ (annual mean).

---

### 🌪️ 4. **PM2.5 (Particulate Matter ≤ 2.5µm)**
- **Source:** Construction dust, vehicle exhaust, burning of coal and wood.  
- **Effect:** Penetrates deep into lungs, causes cardiovascular and respiratory diseases.  
- **Typical Safe Limit:** ≤ 35 µg/m³ (24-hour mean).

---

## 🌈 AQI Classification
| AQI Range | Category | Health Impact |
|------------|-----------|----------------|
| 0 - 50     | Good | Air quality is considered satisfactory. |
| 51 - 100   | Moderate | Acceptable, but may affect sensitive groups. |
| 101 - 150  | Unhealthy for Sensitive Groups | May cause breathing discomfort. |
| 151 - 200  | Unhealthy | Everyone may begin to experience health effects. |
| 201 - 300  | Very Unhealthy | Health warnings of emergency conditions. |
| 301+       | Hazardous | Serious health effects for everyone. |

---

### 🌍 Tips to Reduce Air Pollution
- Use public transport or carpool.
- Switch to renewable energy.
- Plant trees and maintain green spaces.
- Avoid burning waste.
- Maintain vehicles properly.

---

🩵 *A cleaner environment begins with awareness. Together, we can breathe better.*
""")
