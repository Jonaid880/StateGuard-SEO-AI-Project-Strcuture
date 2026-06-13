"""Pydantic request/response models shared across the API."""

from enum import Enum

from pydantic import BaseModel, Field


class Tone(str, Enum):
    professional = "professional"
    casual = "casual"
    technical = "technical"


class ContentRequest(BaseModel):
    topic: str = Field(..., description="The subject to write about.")
    keywords: list[str] = Field(default_factory=list, description="Target SEO keywords.")
    tone: Tone = Tone.professional


class GeneratedContent(BaseModel):
    title: str
    meta_description: str
    body: str


class KeywordMetric(BaseModel):
    keyword: str
    position: int
    volume: int
    difficulty: int


class AnalyticsResponse(BaseModel):
    domain: str
    keywords: list[KeywordMetric]
