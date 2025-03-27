import subprocess
import os
import shutil

# Step 1: Clone the Repository (only if it doesn't exist)
repo_dir = "tinytroupe"
if os.path.exists(repo_dir):
    print(f"Directory {repo_dir} already exists. Skipping clone.")
else:
    subprocess.run(["git", "clone", "https://github.com/microsoft/tinytroupe"])

# Navigate to the directory and install
os.chdir(repo_dir)
subprocess.run(["pip", "install", "."])

# Step 2: Set Up Your Environment
os.environ["OPENAI_API_KEY"] = "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"

# Step 3: Create Lila the Linguist
from tinytroupe.examples import create_lila_the_linguist

lila_ds = create_lila_the_linguist()
lila_ds.listen_and_act("Tell me about your life.")
lila_ds.listen_and_act("Where are you from?")
lila_ds.listen_and_act("Translate 'Hello' to French.")
lila_ds.listen_and_act("Explain the difference between 'affect' and 'effect'.")
lila_ds.listen_and_act("What is the meaning of 'serendipity'?")

# Step 4: Meet Kavya, the Engineer
from tinytroupe.agent import TinyPerson

kavya = TinyPerson("Kavya")
kavya.define("age", 27)
kavya.define("nationality", "Indian")
kavya.define("occupation", "Engineer")
kavya.define("professional_history", "Kavya has worked as Senior Data Analyst and QA Analyst in 2019, leading telecom domain solutions, including SQL, Python, Unix, Excel, Data Visualization tools like PowerBI and Tableau.")

kavya.listen_and_act("What technologies have you worked with?")
kavya.listen_and_act("What data visualization tools do you use?")
kavya.listen_and_act("Explain how you perform data analysis.")
kavya.listen_and_act("What is your experience with telecom domain solutions?")
kavya.listen_and_act("What is your favorite part of being a Data Analyst?")

# Step 4: Create a 2-way Conversation
emma = TinyPerson("Emma")
emma.define("age", 38)
emma.define("nationality", "British")
emma.define("occupation", "AI Research Scientist")
emma.define("professional_history", """
Emma has spent the past 15 years researching artificial intelligence, with a focus on explainability and ethical AI.
She works at a leading tech company, developing AI models that provide transparent decision-making processes.
Emma frequently collaborates with academic institutions, publishes in top AI journals, and speaks at conferences about responsible AI practices.
""")

alex = TinyPerson("Alex")
alex.define("age", 42)
alex.define("nationality", "Canadian")
alex.define("occupation", "Chief Data Scientist at a FinTech Company")
alex.define("professional_history", """
Alex has been working in the financial technology sector for over 18 years, specializing in predictive analytics and risk assessment.
As the Chief Data Scientist, Alex leads a team focused on developing AI-driven solutions for fraud detection and financial forecasting.
""")

emma.listen("You want to ask alex for insights on how AI models are used in financial risk assessment.")
emma.listen("You want to ask alex for details on how AI-driven fraud detection works in FinTech.")
emma.listen("You want to ask alex for his opinion on the challenges of implementing explainable AI in financial decision-making.")
emma.listen("You want to ask alex for his perspective on ethical considerations when using AI for credit scoring and lending.")
emma.listen("You want to ask alex for best practices in making predictive models interpretable for regulators and stakeholders.")

# Step 5: Run for 3-5 iterations
from tinytroupe.environment import TinyWorld

world = TinyWorld("Chat Room", [emma, alex])
world.run(2)
world.run(3)
world.run(5)
