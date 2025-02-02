# app.py
import streamlit as st
from crewai import Task, Crew
from agents import get_problem_generator, get_code_evaluator, get_solution_explainer , get_feedback_reporter
from tasks import create_problem_prompt, create_evaluation_prompt, create_explanation_prompt , create_feedback_report_prompt
from history import init_history, add_history_item, get_history

def main():
    st.title("AI Coding Interviewer ֎ ")
    st.markdown("Practice coding interviews with AI-powered feedback!")
    
    # Initialize chat history
    init_history()
    
    # Sidebar for settings and chat history review
    with st.sidebar:
        st.header("Settings")
        difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"], index=1)
        topic = st.selectbox("Select Topic", ["Arrays", "Graphs", "Dynamic Programming", "Sorting", "Strings", "Data Structures and Algorithms"], index=0)
        
        st.header("Chat History")
        history = get_history()
        if history:
            for idx, item in enumerate(history):
                # Display each history item as a button; when clicked, store its content to display above
                if st.button(f"View {idx+1}: {item['title']}", key=f"history_{idx}"):
                    st.session_state['selected_history'] = item['content']
        else:
            st.write("No history yet.")
    
    # If a history item is selected, display it
    if 'selected_history' in st.session_state:
        st.subheader("Selected Chat History")
        st.markdown(st.session_state['selected_history'])
    
    # Layout: Two columns for generating a problem and submitting code
    col1, col2 = st.columns([1, 1])
    
    # Column 1: Problem Generation
    with col1:
        if st.button("Generate New Problem"):
            with st.spinner("Creating challenge..."):
                problem_generator = get_problem_generator()
                problem_prompt = create_problem_prompt(difficulty, topic)
                problem_task = Task(
                    description=problem_prompt,
                    expected_output="A comprehensive, well-structured coding problem following the specified format",
                    agent=problem_generator
                )
                crew = Crew(
                    agents=[problem_generator],
                    tasks=[problem_task],
                    verbose=True
                )
                generated_problem = crew.kickoff()
                st.session_state.generated_problem = generated_problem
                st.session_state.user_code = ""
                
                # Save the generated problem to history
                add_history_item("Generated Problem", generated_problem)
                
        if 'generated_problem' in st.session_state and st.session_state.generated_problem:
            st.subheader("Coding Challenge")
            st.markdown(st.session_state.generated_problem)
    
    # Column 2: Code Submission & Feedback
    with col2:
        if 'generated_problem' in st.session_state and st.session_state.generated_problem:
            st.subheader("Write Your Solution")
            st.session_state.user_code = st.text_area("Enter your code here:", height=400, value=st.session_state.user_code)
            
            if st.button("Submit Solution"):
                with st.spinner("Analyzing your code..."):
                    evaluator = get_code_evaluator()
                    explainer = get_solution_explainer()
                    
                    # Create tasks for evaluation and explanation
                    evaluation_task = Task(
                        description=create_evaluation_prompt(
                            st.session_state.generated_problem,
                            st.session_state.user_code
                        ),
                        expected_output="Detailed code evaluation report following the specified format including submitted code score /10 and feedback",
                        agent=evaluator,
                        allow_delegation=True
                    )
                    
                    explanation_task = Task(
                         description=create_explanation_prompt("[evaluation_result]"),
                         expected_output="Comprehensive educational explanation following the specified format",
                         agent=explainer,
                         dependencies=[evaluation_task]
                    )
                    
                    reporter = get_feedback_reporter()
                    feedback_task = Task(
                        description=create_feedback_report_prompt(
                        "[evaluation_result]",
                        "[explanation_result]"
                    ),
                        expected_output="Concise feedback report combining evaluation and optimization insights",
                        agent=reporter,
                        dependencies=[evaluation_task, explanation_task]
                    )
                    crew = Crew(
                        agents=[evaluator , explainer , reporter],
                        tasks=[evaluation_task, explanation_task , feedback_task],
                        verbose=True
                    )
                    
                    results = crew.kickoff()
                    st.markdown(results)
                
                    
if __name__ == "__main__":
    main()








