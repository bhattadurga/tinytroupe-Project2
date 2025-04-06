# SmartFinance AI  🤖
## Over View
SmartFinance AI is an AI-driven personal finance assistant designed to help users manage their finances, track expenses, and plan budgets. The app leverages advanced AI to analyze financial habits, predict future spending, and suggest savings strategies.
 
## Features
- **Expense Tracking**: Track your expenses in real-time and categorize them (e.g., groceries, rent, entertainment).
-	**Budget Planner**: Set and monitor monthly budgets for various expense categories.
-	**Expense Forecasting:** AI-driven predictions based on past spending patterns.
-	**Financial Health Insights:** Personalized tips on how to improve your financial health.
-	**Voice Interaction:** Use voice commands to interact with your finances.
-	**Multi-Currency Support:** Automatically detect and convert between currencies based on your region.
-	**Investment Suggestions:** AI-powered recommendations for stocks or savings plans based on risk appetite.
 
## Tech Stack
-	**Frontend:** Streamlit
-	**Backend:** Python (Flask, Requests, Pandas, Matplotlib)
-	**AI Models:** Scikit-learn, TensorFlow/Keras for financial forecasting
-	**Voice Interaction:** Google Speech Recognition and gTTS (Text-to-Speech)
-	**Database:** SQLite for storing user transactions
-	**Currency Conversion:** Open Exchange Rates API
 
## Installation
## Prerequisites
Ensure you have the following installed:
-	Python 3.8+
-	Pip
-	Virtual Environment (optional but recommended)

## Steps
1.	Clone the repository:
   ```sh
   git clone https://github.com/your-repo/smartfinance-ai.git
   cd smartfinance-ai
   ```
2.	Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3.	Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4.	Set up Streamlit:
   ```sh
   streamlit run app.py
   ```
 
## Configuration
Modify your financial parameters in app.py under the sidebar section:
```python
monthly_budget = st.number_input("📊 Monthly Budget", value=1000, step=100, min_value=500, max_value=5000)
currency_code = st.text_input("💱 Currency Code", value="USD")
forecast_months = st.slider("⏳ Forecasting Period", 1, 12, 6)
```
 
## Usage
## Running SmartFinance AI
Launch the application by running:
```sh
streamlit run app.py
```

## Performing Financial Tasks
1.	Track Expenses:
Enter your daily transactions in the input form.
2.	Set Budgets:
Define monthly limits for different categories (e.g., food, rent, entertainment).
3.	View AI Insights:
Get monthly summaries, insights on spending habits, and recommendations for saving.
4.	Investment Suggestions:
View AI-generated recommendations for investment or saving options based on risk appetite.
5.	Voice Interaction:
Activate voice mode and interact with the app by saying commands like “show me my expenses for this week.”
 
## Code Structure
```
smartfinance-ai/
│── models/
│   │── finance_model.h5        # Keras model for expense forecasting
│   │── scaler.pkl              # Scaler for financial data normalization
│── app.py                      # Main application script
│── helper.py                   # Functions for financial analysis, forecasting, and voice interaction
│── output.mp3                  # Text-to-Speech output
│── data/
│   │── transactions.csv        # User transaction data (sample)
│   │── currency_rates.json     # Exchange rates data
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```
 
## API and AI Integration
-	**Scikit-learn Model:** Predicts future expenses and suggests budgets.
-	**TensorFlow Keras Model:** Forecasts future spending trends based on user history.
-	**Google Speech Recognition:** Allows users to speak commands and interact with the app.
-	**Google Text-to-Speech (gTTS):** Converts financial insights and recommendations into speech.
-	**Open Exchange Rates API:** Provides real-time currency conversion.
 
## Troubleshooting
•	Voice Commands Not Working: Ensure that your microphone is properly set up and accessible.
•	AI Predictions Taking Too Long: Try reducing the data set or optimizing the model’s inference time.
 
## Contribution
1.	Fork the repository.
2.	Create a feature branch (`git checkout -b feature-name').
3.	Commit changes (`git commit -m "Added new feature`).
4.	Push to the branch {`git push origin feature-name`).
5.	Open a Pull Request. 

## Contact
For queries or contributions, reach out at: vb46901n@pace.edu
