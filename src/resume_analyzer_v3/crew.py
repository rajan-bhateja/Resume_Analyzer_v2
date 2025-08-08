from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool, FileWriterTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os


os.makedirs("analysis", exist_ok=True)


pdf_rag_tool = PDFSearchTool()
overview_writer_tool = FileWriterTool()
skills_extractor_tool = FileWriterTool()
jobs_recommendation_tool = FileWriterTool()
summary_writer_tool = FileWriterTool()

@CrewBase
class ResumeAnalyzerV3():
    """ResumeAnalyzerV3 crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def resume_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_analyst'], # type: ignore[index]
            tools=[pdf_rag_tool, overview_writer_tool],
            verbose=True
        )

    @agent
    def skill_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['skill_evaluator'], # type: ignore[index]
            tools=[pdf_rag_tool, skills_extractor_tool],
            verbose=True
        )

    @agent
    def job_matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['job_matcher'],  # type: ignore[index]
            tools=[pdf_rag_tool, jobs_recommendation_tool],
            verbose=True
        )

    @agent
    def candidate_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['candidate_summarizer'],  # type: ignore[index]
            tools=[summary_writer_tool],
            verbose=True
        )


    @task
    def summarize_resume(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_resume'], # type: ignore[index]
        )

    @task
    def skill_extraction_and_evaluation(self) -> Task:
        return Task(
            config=self.tasks_config['skill_extraction_and_evaluation'], # type: ignore[index]
        )

    @task
    def job_matching(self) -> Task:
        return Task(
            config=self.tasks_config['job_matching'], # type: ignore[index]
        )

    @task
    def final_candidate_summary(self) -> Task:
        return Task(
            config=self.tasks_config['final_candidate_summary'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeAnalyzerV3 crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
