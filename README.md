# AI Coding Interviewer & Competitive Programming Trainer 

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0B0B0B?style=for-the-badge)](https://www.crewai.com/)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-05122A?style=for-the-badge)](https://deepseek.com/)

An AI-powered platform for practicing coding interviews and competitive programming challenges, featuring automated problem generation, code evaluation, and personalized feedback.

![Screenshot 2025-02-02 231910](https://github.com/user-attachments/assets/27758fbe-97b8-4ea5-a136-ed16df5b0842)

![Screenshot 2025-02-02 231926](https://github.com/user-attachments/assets/413fa806-ca4f-4322-a30b-7fb36b42d2dc)


## Key Features ✨

- **Smart Problem Generation**
  - Customizable by difficulty (Easy/Medium/Hard)
  - Topic-specific challenges (Arrays, Graphs, DP, etc)
  - Real-world interview question patterns

- **AI-Powered Evaluation** 🔍
  - Code correctness verification
  - Time/space complexity analysis
  - Edge case detection
  - Code quality assessment

- **Personalized Feedback** 🚀
  - Step-by-step solution explanations
  - Optimization suggestions
  - Alternative approach recommendations

## Tech Stack ⚙️

- **Core AI**
  - 🧠 DeepSeek-R1 (via Groq)
  - 🤖 CrewAI Agent Orchestration

- **Frontend**
  - 🎨 Streamlit Web Interface
  - 📊 Interactive Code Editor

- **Backend**
  - 🐍 Python 3.10+
  - 📦 Poetry Package Management

## Getting Started 🚀

### Prerequisites
- Python 3.10+
- [DeepSeek API Key](https://platform.deepseek.com/api-keys)
- [Groq Cloud API Key](https://console.groq.com/keys)

### Installation
```bash
# Clone repository
git clone https://github.com/AdeenIlyas/AI-Competitive-Programming-Trainer.git
cd ai-coding-interviewer

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env
