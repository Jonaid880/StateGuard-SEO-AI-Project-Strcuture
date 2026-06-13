/**
 * Thin client for the StateGuard FastAPI backend.
 * The base URL is configured via NEXT_PUBLIC_API_URL.
 */
const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getApiHealth(): Promise<{ ok: boolean }> {
  try {
    const res = await fetch(`${API_URL}/api/health`, { cache: "no-store" });
    return { ok: res.ok };
  } catch {
    return { ok: false };
  }
}

export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...init?.headers },
    ...init,
  });
  if (!res.ok) {
    throw new Error(`API request failed: ${res.status} ${res.statusText}`);
  }
  return res.json() as Promise<T>;
}
