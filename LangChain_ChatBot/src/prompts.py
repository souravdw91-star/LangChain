"""
===========================================================
Prompt Template

Why do we use Prompt Templates?

Without LangChain

Question
↓

Gemini

With LangChain

System Prompt

↓

Chat History

↓

Current Question

↓

Gemini

Prompt Templates generate the final prompt dynamically.
===========================================================
"""

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)


def get_prompt():

    prompt = ChatPromptTemplate.from_messages(

        [

            (
                "system",

                """
                You are an AI Tutor.

                Answer clearly.

                Explain concepts step by step.

                If possible,
                provide examples.

                If the user is learning coding,
                explain WHY as well.
                """

            ),

            MessagesPlaceholder(
                variable_name="history"
            ),

            (
                "human",
                "{question}"
            )

        ]
    )

    return prompt