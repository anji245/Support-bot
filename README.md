# Support Bot – AI-Powered Customer Support Assistant

Support Bot is an AI-powered customer support assistant designed to automatically analyze customer queries, classify support tickets, and generate intelligent responses using Large Language Models (LLMs). The project demonstrates how artificial intelligence can be applied to real-world customer support systems to reduce manual effort, improve response accuracy, and enhance overall efficiency. It integrates backend AI logic with a simple and interactive user interface, making it suitable for academic projects, learning purposes, and practical demonstrations.

The system accepts customer queries in natural language, processes them using trained classification models and LLMs, and produces meaningful responses. The project also includes dedicated modules to evaluate both the machine learning model performance and the accuracy of LLM-generated responses, ensuring the reliability and effectiveness of the system.


## Features

* AI-based understanding of customer support queries
* Automatic classification of support issues
* Intelligent response generation using Large Language Models
* Evaluation of model performance and response accuracy
* Simple and user-friendly web interface
* Secure handling of API tokens using environment variables


## Technologies Used

* **Programming Language:** Python
* **Backend Framework:** Flask
* **Frontend / UI:** Streamlit or Web-based UI
* **AI & ML:** Hugging Face Transformers, Large Language Models (LLMs)
* **Version Control:** Git and GitHub
* **Configuration Management:** Environment variables using `.env`


## Project Structure

support-bot/
├── ui/
│   └── app.py – User interface for interacting with the support bot
├── evaluate_model.py – Script to evaluate classification model performance
├── evaluate_llm_accuracy.py – Script to evaluate LLM response accuracy
├── requirements.txt – List of required Python dependencies
├── .gitignore – Files and folders excluded from GitHub
├── .env – Environment variables (not pushed to GitHub)
└── README.md – Project documentation


## Installation and Setup

Clone the repository and navigate to the project directory:

git clone [https://github.com/anji245/Support-bot.git](https://github.com/anji245/Support-bot.git)
cd Support-bot

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

Windows:
venv\Scripts\activate

Linux / macOS:
source venv/bin/activate

Install required dependencies:

pip install -r requirements.txt

Create a `.env` file in the project root directory and add your Hugging Face access token:

HF_ACCESS_TOKEN=your_huggingface_token


## Running the Application

To start the application UI:

python ui/app.py

If the project uses Streamlit:

streamlit run ui/app.py


## Model Evaluation

The project includes separate evaluation scripts to measure system performance.

* `evaluate_model.py` evaluates the classification model accuracy and predictions.
* `evaluate_llm_accuracy.py` evaluates the correctness and quality of LLM-generated responses.

Run the evaluation scripts using:

python evaluate_model.py
python evaluate_llm_accuracy.py


## Security Considerations

Sensitive information such as API tokens is stored securely using environment variables in a `.env` file. This file is excluded from version control using `.gitignore`, ensuring that confidential data is never exposed on GitHub.


##  Applications and Use Cases

* Automated customer support systems
* Helpdesk ticket classification
* AI-powered chatbot applications
* Academic and final-year engineering projects
* Demonstration of real-world AI and ML integration

## Author
Anji V Y
Computer Science Engineering Student
Interests: Backend developer, Artificial Intelligence
GitHub: https://github.com/anji245

## Future Enhancements

Future improvements may include advanced NLP-based intent detection, multi-language support, persistent chat history storage, database integration, cloud deployment, and integration with real-time messaging platforms.


## License

This project is developed for educational and academic purposes. It may be freely used and modified with proper attribution.
