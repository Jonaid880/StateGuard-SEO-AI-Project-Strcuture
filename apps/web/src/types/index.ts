/** Shared frontend types for StateGuard SEO AI. */

export interface ContentRequest {
  topic: string;
  keywords: string[];
  tone?: "professional" | "casual" | "technical";
}

export interface GeneratedContent {
  title: string;
  metaDescription: string;
  body: string;
}

export interface KeywordMetric {
  keyword: string;
  position: number;
  volume: number;
  difficulty: number;
}
