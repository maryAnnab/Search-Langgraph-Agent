from typing import Dict, Any


class PromptTemplates:
    """Container for all prompt templates used in the research assistant."""

    @staticmethod
    def reddit_url_analysis_system() -> str:
        """System prompt for analyzing Reddit URLs."""
        return """You are an expert at analyzing social media content. Your task is to examine Reddit search results and identify the most relevant posts that would provide valuable additional information for answering the user's question.

Analyze the provided Reddit results and identify URLs of posts that contain valuable information worth investigating further. Focus on posts that:
- Directly relate to the user's question
- Contain detailed discussions or expert opinions
- Have high engagement (upvotes/comments)
- Provide unique perspectives or insights

Return a structured response with the selected URLs."""

