# FinChain
This application allows users to query financial data efficiently using natural language. This project demonstrates how to integrate a ChromaDB vector store within a LangChain pipeline to build an AI-powered GPT Investment Advisor Q&amp;A agent for querying and analyzing financial data.

### Data Source
**2022 Full Year Annual Report** – [Macquarie Group 2022 Full Year Annual Report](https://www.macquarie.com/au/en/investors/reports/full-year-2022.html)


## Demo Video
[![Watch the Demo](https://img.youtube.com/vi/DGCTQqQOdMA/0.jpg)](https://youtu.be/DGCTQqQOdMA)


## Run the App

Follow these steps to set up and run the project:

### Create a Virtual Environment  
```bash
python -m venv env
```

### Activate the Virtual Environment  
- **Windows:**  
  ```bash
  .\env\Scripts\activate
  ```
- **Mac/Linux:**  
  ```bash
  source env/bin/activate
  ```

### Clone the Repository  
```bash
git clone https://github.com/dthatprince/finchain
```

### Navigate into the Project Directory  
```bash
cd finchain
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

### Add OpenAI API Key  
Open **app.py** and update **line 28** with your OpenAI API key (https://platform.openai.com/api-keys):  
```python
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
```


### Run the App  
```bash
streamlit run app.py
```

### Sample test questions:
1. What was the net profit of the company?
2. What initiatives did the bank take towards sustainability?
3. Summarize the financial performance of the bank.


## 🛠️ Features
✅ AI-powered financial analysis  
✅ Natural language queries  
✅ ChromaDB vector storage integration  
✅ LangChain-powered pipeline  
✅ Easy deployment with Streamlit  

## Requirements
- Python 3.8+
- OpenAI API Key
- Streamlit


