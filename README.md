# AI Agent Recommendation System

A web application that recommends the best coding AI agents for given programming tasks. The system analyzes task descriptions and provides personalized recommendations with detailed explanations.

## Features

- **Natural Language Processing**: Accepts task descriptions in plain English
- **Intelligent Matching**: Analyzes task complexity, requirements, and type
- **Top 3 Recommendations**: Provides the best 3 AI agents with detailed justifications
- **Comprehensive Agent Database**: Supports multiple AI coding assistants including:
  - GitHub Copilot
  - Amazon CodeWhisperer
  - Replit Ghostwriter
  - Cursor AI
  - Tabnine
  - Cody by Sourcegraph
  - Codeium

## Screenshots

### Before Query Submission
![Application Interface - Before Query](./demo/Screenshot%20(17).png)
*The main interface showing the task input form ready for user input*

### After Query Submission
![Application Interface - After Query](./demo/Screenshot%20(18).png)
*The interface displaying AI agent recommendations with detailed explanations*

## Project Structure

```
ai-agent-recommendation-system/
├── app.py                    # FastAPI main application
├── recommendation_engine.py  # Core recommendation algorithm
├── knowledge_base.json       # Agent capabilities database
├── frontend.html            # Web interface
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys)
└── README.md               # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-agent-recommendation-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access the application**
   - Open `frontend.html` in your browser
   - Or visit `http://localhost:8000` for API endpoints

## Usage Examples

### Web Interface

1. Open `frontend.html` in your browser
2. Enter your programming task description
3. Click "Get Recommendations"
4. View the top 3 recommended AI agents with explanations

### API Usage

```bash
# Example API call
curl -X POST "http://localhost:8000/" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "I need to build a React frontend with TypeScript for a todo app"}'
```

### Example Task Descriptions

- "Build a Python web scraper for e-commerce sites"
- "Create a React component with TypeScript and styled-components"
- "Develop a machine learning model for image classification"
- "Build a REST API with Node.js and Express"
- "Create a mobile app with React Native"

## API Endpoints

### POST `/`
Recommends AI agents for a given task.

**Request Body:**
```json
{
  "prompt": "Your task description here"
}
```

**Response:**
```json
{
  "recommendations": "Detailed recommendation text with top 3 agents and explanations"
}
```

## How It Works

1. **Task Analysis**: The system uses OpenAI's GPT model to analyze the task description
2. **Agent Matching**: Compares task requirements with agent capabilities from the knowledge base
3. **Scoring Algorithm**: Ranks agents based on relevance, strengths, and limitations
4. **Recommendation**: Returns top 3 agents with detailed explanations

## Agent Knowledge Base

The `knowledge_base.json` file contains detailed information about each AI agent:

- **Strengths**: Primary capabilities and specialties
- **Limitations**: Known constraints and weaknesses
- **System Prompts**: How the agent is configured
- **Use Cases**: Best scenarios for each agent

## Contributing

To add new AI agents or improve recommendations:

1. Update `knowledge_base.json` with agent information
2. Modify `recommendation_engine.py` for algorithm improvements
3. Test with various task descriptions
4. Update documentation

## Technologies Used

- **Backend**: FastAPI (Python)
- **AI Integration**: OpenAI GPT-3.5-turbo
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: JSON-based knowledge base

## License

This project is open source and available under the MIT License. 