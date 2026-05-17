import os
import sys
import tempfile
from dotenv import load_dotenv
from typing import Annotated, Any, Iterable, List, Optional, Sequence, TypedDict
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_litellm import ChatLiteLLM
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

