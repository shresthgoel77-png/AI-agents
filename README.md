# Gen-AI Agents Project 🤖

Welcome to the **AI Agents** repository! This project is a comprehensive Generative AI application focused on building intelligent, context-aware multi-agent systems. By leveraging **LangChain** and **Retrieval-Augmented Generation (RAG)** architectures, this project demonstrates how to create chatbots and agents that can retrieve real-time data, remember past interactions, and understand user sentiment.

## ✨ Key Features

* **Retrieval-Augmented Generation (RAG):** Utilizes custom chunking logic and retrieval tools to anchor the AI's responses in factual, external data sources, reducing hallucinations.
* **LangChain Framework:** Employs LangChain to orchestrate complex agent workflows, manage prompt templates, and chain together LLM calls.
* **Multi-Agent Architecture:**
    * **Retrieval Agents:** Fetches external data (e.g., a Weather API integration).
    * **Memory Agents:** Stores and manages conversation history and context.
    * **Response Agents:** Synthesizes information into natural, user-friendly responses.
* **Emotion Detection:** Integrates IBM Watson NLP to analyze the user's emotional state and sentiment, allowing the chatbot to respond with appropriate empathy.
* **Web Deployment:** Includes a Flask backend to serve the AI chatbot as a web application.

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `ai chatbot.py` | The main entry point for the conversational AI chatbot, featuring enhanced configuration and error handling. |
| `RAG project.py` / `Minirag.py` | Core implementations of the RAG pipeline, including document processing and chunking logic. |
| `ragtools.py` | Utility functions and tool integrations supporting the RAG framework. |
| `agent.py` | Defines the `WeatherRetrievalAgent` class for interacting with external weather APIs. |
| `memory.py` | Implements the `MemoryAgent` class for storing context, such as previously requested weather info. |
| `response.py` | Houses the `ResponseAgent` class responsible for generating the final output delivered to the user. |
| `emotion_detection.py` | Implementation of Watson NLP to extract and classify user emotions during interactions. |
| `flaskmy.py` | Flask application setup for hosting the chatbot on a web server. |

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* API Keys for your chosen LLM (e.g., OpenAI), Weather API, and IBM Watson NLP.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shresthgoel77-png/AI-agents.git](https://github.com/shresthgoel77-png/AI-agents.git)
    cd AI-agents
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    *(Note: Ensure you have a `requirements.txt` file, or manually install `langchain`, `flask`, `ibm-watson`, etc.)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    WEATHER_API_KEY=your_weather_api_key
    WATSON_API_KEY=your_watson_api_key
    WATSON_URL=your_watson_service_url
    ```
### Usage

To run the Flask application and interact with the AI agents via the web interface:

```bash
python flaskmy.py
```

### To run the CLI CHATBOTS DIRECTLY:
```bash
python "ai chatbot.py"
```

### LICENSE:
This project is licensed under the MIT License.
