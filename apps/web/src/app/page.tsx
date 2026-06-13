import Link from "next/link";

export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen max-w-3xl flex-col items-center justify-center gap-6 px-6 text-center">
      <h1 className="text-4xl font-bold tracking-tight text-brand">
        StateGuard SEO AI
      </h1>
      <p className="max-w-xl text-lg text-slate-600">
        An AI-powered SEO automation suite — content generation, analytics, and
        autonomous SEO agents in one place.
      </p>
      <Link
        href="/dashboard"
        className="rounded-md bg-brand px-5 py-2.5 font-medium text-white transition hover:bg-brand-dark"
      >
        Open dashboard
      </Link>
    </main>
  );
}
