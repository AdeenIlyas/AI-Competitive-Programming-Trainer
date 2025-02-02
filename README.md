# AI Coding Interviewer & Competitive Programming Trainer 

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0B0B0B?style=for-the-badge)](https://www.crewai.com/)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-05122A?style=for-the-badge)](https://deepseek.com/)

An AI-powered platform for practicing coding interviews and competitive programming challenges, featuring automated problem generation, code evaluation, and personalized feedback.

![Screenshot 2025-02-02 233251](https://github.com/user-attachments/assets/42c38d9e-4c6b-4a12-8974-daceafc1ec90)

<p align="center">
  <img src="https://github.com/user-attachments/assets/23f50d4e-1dc5-4695-a9fe-61f4550b6a90" width="45%">
  <img src="https://github.com/user-attachments/assets/a7a9e464-5ccb-4919-a0c0-63d909efd81c" width="45%">
</p>



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
  - 🧠 gemma2-9b-it (via Groq)
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
