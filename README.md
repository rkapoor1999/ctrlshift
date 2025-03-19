# CTRL+SHIFT

CTRL+SHIFT is a Python-based tool that allows users to analyze Google search interest trends over time. The name "CTRL+SHIFT" symbolizes a quick shift in focus, just like how trends in online searches rapidly evolve. It represents the ability to "control the shift" in digital culture, enabling users to analyze and adapt to changing trends efficiently. Inspired by the keyboard shortcut that allows users to switch tasks efficiently, this project enables seamless trend analysis for businesses, creators, and researchers. 

This tool can be beneficial in various industries. For example:
- **Fashion Industry**: Brands can use it to predict upcoming fashion trends based on search volume.
- **Marketing & Advertising**: Helps marketers gauge consumer interest in products and services.
- **Investors & Businesses**: Can track interest in companies, stocks, and emerging markets.
- **Tech Industry**: Helps product managers analyze public interest in emerging technologies.
- **Content Creators**: Assists bloggers and influencers in identifying trending topics.

---

## 🚀 Features
✅ Fetches **Google Trends interest over time** for any keyword  
✅ Converts **Pandas DataFrame to JSON API response**  
✅ Implements **error handling** for missing data and rate limits  
✅ Uses **Flask** to create a REST API  
✅ Designed for **command-line interaction** using `curl`  
✅ **Customizable Search**: Users can hardcode any keyword(s) in the script.  
✅ **No Server Setup Required**: Runs directly as a Python script.  
✅ **Easy to Use**: Just edit the script and run it in the terminal.  

---

## 🛠️ Tech Stack & Skills Gained
- **Python** - Scripting, automation, and data extraction.
- **PyTrends** - API interaction and data retrieval from Google Trends.
- **Pandas** - Data manipulation, structuring, and processing.
- **Flask (Optional for expansion)** - Web API development.
- **Command Line Usage** - Running and debugging scripts via terminal.
- **Data Visualization (Future Scope)** - Potential use of Matplotlib/Seaborn for trend graphs.
- **Error Handling & Rate Limiting** - Handling API request limits and exceptions.
- **REST API Development** - Understanding API endpoints and JSON responses.
- **Data-Driven Decision Making** - Applying insights from search trends.

---

## 📂 Project Structure
```
ctrl+shift/
│── backend/
│   ├── trend_data.py  # Main script where users edit keywords and run the program
│── frontend/          # (Optional) Placeholder for future enhancements
│── README.md          # Documentation (this file)
```

---

## 🔧 How to Run the Project

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/ctrl-shift.git
cd ctrl-shift
```

### **2️⃣ Install Dependencies**
Ensure you have Python 3 installed, then install the required packages:
```sh
pip install -r requirements.txt
```

### **3️⃣ Edit `trend_data.py`**
Open the file `trend_data.py` and **change the keyword** inside the script:
```python
keywords = ["nike dunks"]  # <-- Change this to any keyword you want to analyze
```

### **4️⃣ Run the Script**
Execute the script in the terminal:
```sh
python3 backend/trend_data.py
```

### **5️⃣ View the Output**
The search trend data will be displayed in the terminal in a tabular format.

---

## 🎯 Why CTRL+SHIFT?
CTRL+SHIFT is designed to provide quick insights into search trends with minimal setup. Unlike complex data scraping tools, this project simplifies trend analysis by fetching data with just a few lines of Python. The name "CTRL+SHIFT" reflects the rapid change in trends, just like the keyboard shortcut that allows users to switch focus quickly.

---

## 🌟 Future Improvements
- [ ] Implement a GUI for selecting keywords instead of manual editing.
- [ ] Enhance visualization with trend graphs.
- [ ] Optimize request handling to avoid Google rate limits.
- [ ] Expand analysis to include related search queries and topics.

---

## 📜 License
This project is open-source and available under the MIT License.

---

## 📩 Contact
For questions or contributions, reach out via [your contact info].

---

