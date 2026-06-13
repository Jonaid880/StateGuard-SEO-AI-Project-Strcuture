import { getApiHealth } from "@/lib/api";

const features = [
  {
    title: "Content generation",
    description:
      "AI-generated articles, meta titles/descriptions, and keyword-optimized copy.",
  },
  {
    title: "Analytics",
    description:
      "Rankings, backlinks, and traffic pulled from Ahrefs, SE Ranking, and GSC.",
  },
  {
    title: "Audits & agents",
    description: "Automated site audits, reporting, and agentic SEO workflows.",
  },
];

export default async function DashboardPage() {
  const health = await getApiHealth();

  return (
    <main className="mx-auto max-w-5xl px-6 py-12">
      <header className="mb-10">
        <h1 className="text-3xl font-bold text-slate-900">Dashboard</h1>
        <p className="mt-1 text-sm text-slate-500">
          Backend status:{" "}
          <span
            className={
              health.ok ? "font-medium text-green-600" : "font-medium text-red-600"
            }
          >
            {health.ok ? "connected" : "unavailable"}
          </span>
        </p>
      </header>

      <section className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {features.map((feature) => (
          <article
            key={feature.title}
            className="rounded-lg border border-slate-200 bg-white p-6 shadow-sm"
          >
            <h2 className="text-lg font-semibold text-slate-900">
              {feature.title}
            </h2>
            <p className="mt-2 text-sm text-slate-600">{feature.description}</p>
          </article>
        ))}
      </section>
    </main>
  );
}
