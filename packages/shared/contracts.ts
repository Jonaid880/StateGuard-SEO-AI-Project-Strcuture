/**
 * Shared API contracts between the Next.js frontend and the FastAPI backend.
 * Mirror of services/api/app/models/schemas.py — keep both in sync.
 */

export type Tone = "professional" | "casual" | "technical";

export interface ContentRequest {
  topic: string;
  keywords: string[];
  tone?: Tone;
}

export interface GeneratedContent {
  title: string;
  meta_description: string;
  body: string;
}

export interface KeywordMetric {
  keyword: string;
  position: number;
  volume: number;
  difficulty: number;
}

export interface AnalyticsResponse {
  domain: string;
  keywords: KeywordMetric[];
}
