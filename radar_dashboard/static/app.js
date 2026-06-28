const state = {
  summary: null,
  week: "",
  direction: "all",
  query: "",
  theme: "all",
  paperLimit: 20,
  sourcePapers: [],
  allPapers: [],
  visiblePapers: [],
  methodFamilies: [],
};

const colors = ["#2f7d62", "#3867a6", "#a64f3c", "#9a6b20", "#6f5aa8"];
const authorityVenues = new Set([
  "AAAI",
  "ACL",
  "COLM",
  "CVPR",
  "EACL",
  "EMNLP",
  "ICLR",
  "ICML",
  "IJCAI",
  "KDD",
  "NAACL",
  "NEURIPS",
  "SIGIR",
  "TACL",
  "WWW",
]);
const staticData = window.RADAR_STATIC_DATA || null;

const $ = (id) => document.getElementById(id);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function venueClass(venue) {
  return String(venue || "").toLowerCase().replace(/[^a-z0-9-]/g, "");
}

function isAuthorityVenue(paper) {
  if (paper?.is_authority_venue) return true;
  return authorityVenues.has(String(paper?.venue || "").trim().toUpperCase());
}

function compactText(value, fallback = "未提及") {
  const text = String(value || "").trim();
  if (!text || ["提取失败", "摘要未提及", "未提及", "暂不明显"].includes(text)) {
    return fallback;
  }
  return text;
}

function truncateText(value, limit = 120) {
  const text = compactText(value, "");
  if (!text) return "";
  return text.length > limit ? `${text.slice(0, limit)}...` : text;
}

async function fetchJson(url) {
  if (staticData) {
    return readStaticData(url);
  }
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Request failed: ${url}`);
  return response.json();
}

function readStaticData(url) {
  const parsed = new URL(url, window.location.href);
  if (parsed.pathname.endsWith("/api/summary")) {
    return Promise.resolve(staticData.summary);
  }
  if (parsed.pathname.endsWith("/api/papers")) {
    return Promise.resolve({ papers: filterStaticPapers(parsed.searchParams) });
  }
  if (parsed.pathname.endsWith("/api/themes")) {
    return Promise.resolve({ themes: countStaticMethodFamilies(parsed.searchParams) });
  }
  return Promise.reject(new Error(`Static data route not found: ${url}`));
}

function staticPapersForScope(params) {
  const week = params.get("week") || "";
  const direction = params.get("direction") || "";

  let result = staticData.papers || [];
  if (week && week !== "all") {
    result = result.filter((paper) => paper.week === week);
  }
  if (direction && direction !== "all") {
    result = result.filter((paper) => paper.direction_id === direction);
  }
  return result;
}

function countStaticMethodFamilies(params) {
  const counts = new Map();
  for (const paper of staticPapersForScope(params)) {
    const family = paper.method_family || paper.theme || "未分类";
    if (!family || family === "未分类") continue;
    counts.set(family, (counts.get(family) || 0) + 1);
  }
  return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).slice(0, 40);
}

function filterStaticPapers(params) {
  const query = (params.get("q") || "").trim().toLowerCase();
  const theme = (params.get("theme") || "").trim();
  const limit = Number(params.get("limit") || 1000);

  let result = staticPapersForScope(params);
  if (theme && theme !== "all") {
    result = result.filter((paper) => paper.theme === theme || paper.method_family === theme);
  }
  if (query) {
    const terms = query.split(/\s+/).filter(Boolean);
    result = result.filter((paper) => {
      const haystack = [
        "title",
        "title_zh",
        "abstract",
        "abstract_zh",
        "venue",
        "manual_reason",
        "problem",
        "method",
        "contribution",
        "limitations",
        "key_finding",
        "theme",
        "method_family",
        "cross_direction",
        "edit_target",
        "agent_setting",
        "control_mechanism",
        "evaluation_environment",
        "evaluation_signal",
        "failure_mode",
        "reliability_risk",
        "industrial_relevance",
        "idea_feasibility",
        "compute_cost",
        "idea_hook",
        "mentor_question",
        "direction_fit",
        "category",
      ].map((key) => String(paper[key] || "")).join(" ").toLowerCase();
      return terms.every((term) => haystack.includes(term));
    });
  }

  return result
    .slice()
    .sort((a, b) => [b.week, b.collected || "", b.title].join("\0").localeCompare([a.week, a.collected || "", a.title].join("\0")))
    .slice(0, limit);
}

function priorityScore(value) {
  return { high: 3, medium: 2, low: 1 }[String(value || "").toLowerCase()] || 0;
}

function mergeDuplicatePapers(papers) {
  const merged = new Map();
  for (const paper of papers) {
    const key = paper.id || paper.url || String(paper.title || "").toLowerCase();
    if (!merged.has(key)) {
      merged.set(key, {
        ...paper,
        direction_names: [paper.direction_name].filter(Boolean),
      });
      continue;
    }

    const current = merged.get(key);
    const directions = new Set([...(current.direction_names || []), paper.direction_name].filter(Boolean));
    const better =
      priorityScore(paper.read_priority) > priorityScore(current.read_priority) ||
      (paper.ingest_source === "manual" && current.ingest_source !== "manual") ||
      (isAuthorityVenue(paper) && !isAuthorityVenue(current)) ||
      (Boolean(paper.venue) && !current.venue) ||
      (Boolean(paper.has_code) && !current.has_code);
    const base = better ? { ...current, ...paper } : current;
    merged.set(key, {
      ...base,
      has_code: Boolean(current.has_code || paper.has_code),
      repo_url: current.repo_url || paper.repo_url || "",
      repo_stars: Math.max(Number(current.repo_stars || 0), Number(paper.repo_stars || 0)),
      venue: current.venue || paper.venue || "",
      venue_year: current.venue_year || paper.venue_year || "",
      venue_type: current.venue_type || paper.venue_type || "",
      venue_url: current.venue_url || paper.venue_url || "",
      is_authority_venue: Boolean(isAuthorityVenue(current) || isAuthorityVenue(paper)),
      ingest_source: current.ingest_source || paper.ingest_source || "",
      manual_reason: current.manual_reason || paper.manual_reason || "",
      manual_tags: current.manual_tags || paper.manual_tags || [],
      cross_direction: current.cross_direction || paper.cross_direction || "",
      direction_names: [...directions],
      direction_name: [...directions].join(" / "),
    });
  }
  return [...merged.values()];
}

function readingScore(paper) {
  return (
    priorityScore(paper.read_priority) * 100 +
    (paper.ingest_source === "manual" ? 28 : 0) +
    (isAuthorityVenue(paper) ? 30 : paper.venue ? 8 : 0) +
    (paper.has_code ? 12 : 0) +
    Math.min(Number(paper.repo_stars || 0), 50) / 10
  );
}

function sortReadingQueue(papers) {
  return papers.slice().sort((a, b) => {
    const scoreA = readingScore(a);
    const scoreB = readingScore(b);
    if (scoreA !== scoreB) return scoreB - scoreA;
    return String(a.title || "").localeCompare(String(b.title || ""));
  });
}

function paperIdentity(paper) {
  return paper.id || paper.url || String(paper.title || "").trim().toLowerCase();
}

function uniquePaperCount(papers) {
  return new Set(papers.map(paperIdentity).filter(Boolean)).size;
}

function activeWeek() {
  return state.week || state.summary?.current_week || "all";
}

function countEntries(items, getValue, { limit = 16, skip = [] } = {}) {
  const skipped = new Set(skip);
  const counts = new Map();
  for (const item of items) {
    const value = String(getValue(item) || "").trim();
    if (!value || skipped.has(value)) continue;
    counts.set(value, (counts.get(value) || 0) + 1);
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, limit);
}

function scopedPapers({ applyWeek = true, applyDirection = true } = {}) {
  const week = activeWeek();
  let papers = state.sourcePapers || [];
  if (applyWeek && week && week !== "all") {
    papers = papers.filter((paper) => paper.week === week);
  }
  if (applyDirection && state.direction && state.direction !== "all") {
    papers = papers.filter((paper) => paper.direction_id === state.direction);
  }
  return papers;
}

function buildScopedSummary() {
  const base = state.summary || {};
  const allPapers = state.sourcePapers || [];
  const week = activeWeek();
  const weekLabel = week === "all" ? "全部周" : week;
  const directionsBase = base.directions || [];
  const directionScope = state.direction && state.direction !== "all"
    ? directionsBase.filter((direction) => direction.id === state.direction)
    : directionsBase;
  const papers = scopedPapers();
  const authorityPapers = papers.filter((paper) => isAuthorityVenue(paper));
  const authorityAnchors = base.authority_anchors || [];
  const scopedAnchors = state.direction && state.direction !== "all"
    ? authorityAnchors.filter((anchor) => anchor.direction_id === state.direction)
    : authorityAnchors;
  const anchorCounts = new Map(countEntries(authorityAnchors, (anchor) => anchor.direction_id, { limit: 1000 }));

  const directions = directionScope.map((direction) => {
    const subset = papers.filter((paper) => paper.direction_id === direction.id);
    return {
      ...direction,
      count: subset.length,
      code_count: subset.filter((paper) => paper.has_code).length,
      authority_count: subset.filter((paper) => isAuthorityVenue(paper)).length,
      anchor_count: anchorCounts.get(direction.id) || 0,
      themes: countEntries(subset, (paper) => paper.theme, { limit: 8, skip: ["未分类"] }),
      method_families: countEntries(subset, (paper) => paper.method_family || paper.theme, { limit: 8, skip: ["未分类"] }),
      priorities: countEntries(subset, (paper) => paper.read_priority, { limit: 8 }),
    };
  });

  const weeks = base.weeks || [...new Set(allPapers.map((paper) => paper.week).filter(Boolean))].sort();
  const trend = weeks.map((trendWeek) => {
    const row = { week: trendWeek, total: 0, directions: {} };
    for (const direction of directionScope) {
      const count = allPapers.filter((paper) => paper.week === trendWeek && paper.direction_id === direction.id).length;
      row.directions[direction.id] = count;
      row.total += count;
    }
    return row;
  });

  const ideaHooks = papers
    .filter((paper) => {
      const hook = compactText(paper.idea_hook, "");
      return hook && hook !== "暂不明显";
    })
    .sort((a, b) => readingScore(b) - readingScore(a))
    .slice(0, 10)
    .map((paper) => ({
      title: paper.title,
      url: paper.url,
      idea_hook: paper.idea_hook,
      read_priority: paper.read_priority,
      direction_name: paper.direction_name,
    }));

  const codePapers = papers
    .filter((paper) => paper.has_code)
    .sort((a, b) => Number(b.repo_stars || 0) - Number(a.repo_stars || 0) || String(a.title || "").localeCompare(String(b.title || "")))
    .map((paper) => ({
      title: paper.title,
      url: paper.url,
      repo_url: paper.repo_url,
      repo_stars: paper.repo_stars || 0,
      direction_name: paper.direction_name,
    }));

  return {
    ...base,
    current_week: weekLabel,
    selected_week: week,
    weeks,
    total_papers: papers.length,
    unique_papers: uniquePaperCount(papers),
    total_code: papers.filter((paper) => paper.has_code).length,
    total_authority: uniquePaperCount(authorityPapers),
    authority_anchor_count: scopedAnchors.length,
    authority_anchors: scopedAnchors,
    directions,
    trend,
    themes: countEntries(papers, (paper) => paper.theme, { limit: 16, skip: ["未分类"] }),
    method_families: countEntries(papers, (paper) => paper.method_family || paper.theme, { limit: 16, skip: ["未分类"] }),
    cross_directions: countEntries(papers, (paper) => paper.cross_direction, {
      limit: 12,
      skip: ["not-crossing", "benchmark-only"],
    }),
    priorities: countEntries(papers, (paper) => paper.read_priority, { limit: 8 }),
    venues: countEntries(papers, (paper) => paper.venue, { limit: 12 }),
    authority_venues: countEntries(authorityPapers, (paper) => paper.venue, { limit: 12 }),
    categories: countEntries(papers, (paper) => paper.category || "unknown", { limit: 10 }),
    idea_hooks: ideaHooks,
    code_papers: codePapers,
  };
}

function setOptions(select, options, value) {
  select.innerHTML = options.map((option) => (
    `<option value="${escapeHtml(option.value)}">${escapeHtml(option.label)}</option>`
  )).join("");
  select.value = value;
}

function renderSummary() {
  const summary = buildScopedSummary();
  const baseSummary = state.summary || {};
  const source = staticData ? `静态快照 · ${staticData.generated_at || "local"}` : "实时 API";
  const directionLabel = state.direction === "all"
    ? "全部方向"
    : (baseSummary.directions || []).find((direction) => direction.id === state.direction)?.name || state.direction;
  $("subtitle").textContent = `agent harness / reliability · ${summary.current_week || "no week"} · ${directionLabel} · ${source}`;
  $("totalPapers").textContent = summary.unique_papers || summary.total_papers;
  $("totalCode").textContent = summary.total_code;
  $("authorityCount").textContent = summary.total_authority || 0;

  const weekOptions = [
    ...(baseSummary.weeks || []).map((week) => ({ value: week, label: week })),
    { value: "all", label: "全部周" },
  ];
  setOptions($("weekSelect"), weekOptions, activeWeek());

  const directionOptions = [
    { value: "all", label: "全部方向" },
    ...(baseSummary.directions || []).map((direction) => ({ value: direction.id, label: direction.name })),
  ];
  setOptions($("directionSelect"), directionOptions, state.direction);

  renderTrend(summary);
  renderDirections(summary);
  renderAuthorityAnchors(summary);
  renderCrossDirections(summary);
  renderVenues(summary);
  renderIdeaHooks(summary);
  renderCodePapers(summary);
}

function renderCrossDirections(summary) {
  const rows = summary.cross_directions || [];
  $("crossDirectionList").innerHTML = rows.map(([label, count]) => (
    `<li class="cross-row"><span class="tag cross">${escapeHtml(label)}</span><span>${count} 篇</span></li>`
  )).join("") || `<li>本周暂无明显交叉标签</li>`;
}

function renderTrend(summary) {
  const maxTotal = Math.max(1, ...summary.trend.map((row) => row.total));
  $("trendChart").innerHTML = summary.trend.map((row) => {
    const segments = summary.directions.map((direction, index) => {
      const count = row.directions[direction.id] || 0;
      const width = row.total ? (count / row.total) * 100 : 0;
      return `<span class="trend-seg" title="${escapeHtml(direction.name)}: ${count}" style="width:${width}%;background:${colors[index % colors.length]}"></span>`;
    }).join("");
    const barWidth = row.total ? Math.max(8, (row.total / maxTotal) * 100) : 2;
    return `
      <div class="trend-row">
        <span>${escapeHtml(row.week)}</span>
        <div class="trend-bar" style="width:${barWidth}%">${segments}</div>
        <strong>${row.total}</strong>
      </div>
    `;
  }).join("") || `<p class="empty">暂无趋势数据</p>`;
}

function renderDirections(summary) {
  $("directionCards").innerHTML = summary.directions.map((direction, index) => {
    const families = (direction.method_families || []).slice(0, 4).map(([family, count]) => (
      `<span class="tag">${escapeHtml(family)} ${count}</span>`
    )).join("");
    const high = (direction.priorities || []).find(([name]) => name === "high");
    const highCount = high ? high[1] : 0;
    const metrics = [
      ["论文", direction.count || 0],
      ["A会", direction.authority_count || 0],
      ["代码", direction.code_count || 0],
      ["高优先", highCount],
    ].map(([label, value]) => (
      `<div class="direction-metric"><strong>${value}</strong><span>${label}</span></div>`
    )).join("");
    const anchorTag = direction.anchor_count ? `<span class="tag authority">锚点 ${direction.anchor_count}</span>` : "";
    return `
      <article class="direction-card" style="border-left-color:${colors[index % colors.length]}">
        <div class="direction-head">
          <h3>${escapeHtml(direction.name)}</h3>
          <div class="direction-metrics">${metrics}</div>
        </div>
        <p class="direction-desc">${escapeHtml(direction.description)}</p>
        <div class="paper-meta direction-families">${anchorTag}${families}</div>
      </article>
    `;
  }).join("") || `<p class="empty">暂无方向配置</p>`;
}

function renderAuthorityAnchors(summary) {
  const anchors = summary.authority_anchors || [];
  const scoped = state.direction && state.direction !== "all"
    ? anchors.filter((anchor) => anchor.direction_id === state.direction)
    : anchors;
  const shown = scoped.slice(0, 12);
  const hidden = scoped.length - shown.length;
  $("authorityMeta").textContent = state.direction === "all"
    ? `${anchors.length} 篇`
    : `${scoped.length} 篇 · 当前方向`;
  $("authorityAnchorList").innerHTML = shown.map((anchor) => {
    const tags = (anchor.tags || []).slice(0, 3).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join("");
    const badge = venueBadge({
      venue: anchor.venue,
      venue_year: anchor.year,
      venue_type: anchor.type,
      venue_url: anchor.url,
    });
    return `
      <li class="anchor-card">
        <div class="anchor-top">
          ${badge}
          <span class="tag">${escapeHtml(anchor.direction_name || anchor.direction_id)}</span>
          ${tags}
        </div>
        <a class="anchor-title" href="${escapeHtml(anchor.url)}" target="_blank" rel="noreferrer">${escapeHtml(anchor.title)}</a>
        ${anchor.note ? `<p class="anchor-note">${escapeHtml(truncateText(anchor.note, 130))}</p>` : ""}
      </li>
    `;
  }).join("") || `<li>暂无手工权威锚点</li>`;
  if (hidden > 0) {
    $("authorityAnchorList").innerHTML += `<li class="anchor-card"><strong>还有 ${hidden} 篇</strong><p class="anchor-note">切到具体方向可查看对应锚点，导师讨论时优先对齐这些已发表工作。</p></li>`;
  }
}

function renderMethodFamilies() {
  const container = $("themeCloud");
  if (!container) return;
  const families = state.methodFamilies.length ? state.methodFamilies : (buildScopedSummary().method_families || []);
  const chips = families.map(([family, count]) => (
    `<button class="chip ${state.theme === family ? "active" : ""}" type="button" data-theme="${escapeHtml(family)}">${escapeHtml(family)} <strong>${count}</strong></button>`
  )).join("");
  container.innerHTML = `<button class="chip ${state.theme === "all" ? "active" : ""}" type="button" data-theme="all">全部</button>${chips || `<span class="empty-inline">暂无数据</span>`}`;
  container.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      state.theme = button.dataset.theme;
      loadPapers();
      renderMethodFamilies();
    });
  });
}

function renderVenues(summary) {
  const venues = summary.authority_venues || summary.venues || [];
  $("venueList").innerHTML = venues.map(([venue, count]) => (
    `<li class="venue-row"><span class="venue venue-${venueClass(venue)}">${escapeHtml(venue)}</span><span>${count} 篇</span></li>`
  )).join("") || `<li>本周暂无已识别 A 会标签</li>`;
}

function renderIdeaHooks(summary) {
  $("ideaHooksList").innerHTML = (summary.idea_hooks || []).slice(0, 5).map((item) => (
    `<li class="hook-card"><div class="hook-summary"><span class="priority ${escapeHtml(item.read_priority)}">${escapeHtml(item.read_priority)}</span><span class="hook-text">${escapeHtml(truncateText(item.idea_hook, 96))}</span></div><a href="${escapeHtml(item.url)}" target="_blank" rel="noreferrer">${escapeHtml(truncateText(item.title, 80))}</a></li>`
  )).join("") || `<li>本周暂无可延展 idea hook</li>`;
}

function renderCodePapers(summary) {
  $("codeList").innerHTML = (summary.code_papers || []).slice(0, 6).map((paper) => (
    `<li class="resource-card"><a href="${escapeHtml(paper.url)}" target="_blank" rel="noreferrer">${escapeHtml(truncateText(paper.title, 82))}</a><span>${escapeHtml(paper.direction_name)}</span>${paper.repo_url ? `<a class="repo-link" href="${escapeHtml(paper.repo_url)}" target="_blank" rel="noreferrer">repo</a>` : ""}</li>`
  )).join("") || `<li>本周暂无带代码论文</li>`;
}

function venueBadge(paper) {
  if (!paper.venue) return "";
  const year = paper.venue_year ? ` ${paper.venue_year}` : "";
  const type = paper.venue_type ? ` · ${paper.venue_type}` : "";
  const label = `${paper.venue}${year}${type}`;
  const content = `<span class="venue venue-${venueClass(paper.venue)}">${escapeHtml(label)}</span>`;
  if (paper.venue_url) {
    return `<a class="venue-link" href="${escapeHtml(paper.venue_url)}" target="_blank" rel="noreferrer">${content}</a>`;
  }
  return content;
}

function directionBadges(paper) {
  const names = paper.direction_names && paper.direction_names.length ? paper.direction_names : [paper.direction_name];
  return names.filter(Boolean).map((name) => `<span class="tag">${escapeHtml(name)}</span>`).join("");
}

function chips(values) {
  if (!Array.isArray(values) || values.length === 0) return `<span class="muted">未提及</span>`;
  return values.map((value) => `<span class="tag">${escapeHtml(value)}</span>`).join("");
}

function detailRow(label, value) {
  const text = compactText(value, "");
  if (!text) return "";
  return `<div><dt>${escapeHtml(label)}</dt><dd>${escapeHtml(text)}</dd></div>`;
}

function insight(label, value, limit = 110) {
  const text = compactText(value, "");
  if (!text) return "";
  return `
    <div class="insight">
      <span>${escapeHtml(label)}</span>
      <p>${escapeHtml(truncateText(text, limit))}</p>
    </div>
  `;
}

function paperCard(paper, index) {
  const titleZh = compactText(paper.title_zh, "");
  const abstractZh = compactText(paper.abstract_zh, "");
  const priority = paper.read_priority || "low";
  const authority = isAuthorityVenue(paper);
  const crossTag = compactText(paper.cross_direction, "");
  const crossBadge = crossTag && !["not-crossing", "benchmark-only"].includes(crossTag)
    ? `<span class="tag cross">${escapeHtml(crossTag)}</span>`
    : "";
  return `
    <article class="paper-card paper-priority-${escapeHtml(priority)} ${authority ? "paper-authority" : ""}">
      <div class="paper-main">
        <div class="paper-meta">
          ${venueBadge(paper)}
          ${authority ? `<span class="tag authority">A会重点</span>` : ""}
          ${paper.ingest_source === "manual" ? `<span class="tag manual">手动</span>` : ""}
          ${directionBadges(paper)}
          <span class="tag">${escapeHtml(paper.method_family || paper.theme || "未分类")}</span>
          ${crossBadge}
          <span class="priority ${escapeHtml(priority)}">${escapeHtml(priority)}</span>
          ${paper.has_code ? `<span class="tag code">代码</span>` : ""}
        </div>
        <h3><a href="${escapeHtml(paper.url)}" target="_blank" rel="noreferrer">${escapeHtml(paper.title)}</a></h3>
        ${titleZh ? `<p class="paper-title-zh">${escapeHtml(titleZh)}</p>` : ""}
        ${abstractZh ? `<p class="card-abstract">${escapeHtml(abstractZh)}</p>` : ""}
        <div class="paper-actions">
          <button class="detail-btn" type="button" data-detail-index="${index}">详情</button>
          <a href="${escapeHtml(paper.url)}" target="_blank" rel="noreferrer">arXiv</a>
          ${paper.pdf_url ? `<a href="${escapeHtml(paper.pdf_url)}" target="_blank" rel="noreferrer">PDF</a>` : ""}
          ${paper.repo_url ? `<a href="${escapeHtml(paper.repo_url)}" target="_blank" rel="noreferrer">Code</a>` : ""}
        </div>
      </div>
      <aside class="insight-list" aria-label="结构化信号">
        <div class="read-why">
          <span>看点</span>
          <p>${escapeHtml(truncateText(paper.idea_hook || paper.key_finding || paper.contribution, 150))}</p>
        </div>
        ${insight("控制机制", paper.control_mechanism || paper.evaluation_signal, 96)}
        ${insight("可靠性风险", paper.reliability_risk || paper.failure_mode, 84)}
      </aside>
    </article>
  `;
}

async function loadPapers() {
  const params = new URLSearchParams({
    week: state.week || state.summary.current_week,
    direction: state.direction,
    q: state.query,
    theme: state.theme,
    limit: "1000",
  });
  const data = await fetchJson(`/api/papers?${params.toString()}`);
  const papers = sortReadingQueue(state.direction === "all" ? mergeDuplicatePapers(data.papers) : data.papers);
  state.allPapers = papers;
  state.paperLimit = 20;
  renderPaperList();
}

async function loadMethodFamilies() {
  const params = new URLSearchParams({
    week: state.week || state.summary.current_week || "all",
    direction: state.direction,
  });
  const data = await fetchJson(`/api/themes?${params.toString()}`);
  state.methodFamilies = data.themes || [];
  renderMethodFamilies();
}

function activeFilterText() {
  const filters = [];
  if (state.theme && state.theme !== "all") {
    filters.push(`方法族：${state.theme}`);
  }
  if (state.query) {
    filters.push(`搜索：${state.query}`);
  }
  return filters.length ? ` · ${filters.join(" · ")}` : "";
}

function renderPaperList() {
  const papers = state.allPapers.slice(0, state.paperLimit);
  state.visiblePapers = papers;
  $("paperCount").textContent = state.direction === "all"
    ? `${state.allPapers.length} 篇去重论文 · high / A会 / code 优先${activeFilterText()}`
    : `${state.allPapers.length} 篇论文 · high / A会 / code 优先${activeFilterText()}`;
  $("papers").innerHTML = papers.map((paper, index) => paperCard(paper, index)).join("") || `<p class="empty">没有匹配论文</p>`;
  const hasMore = state.paperLimit < state.allPapers.length;
  $("showMoreBtn").classList.toggle("hidden", !hasMore);
  $("showMoreBtn").textContent = hasMore
    ? `显示更多（${Math.min(state.paperLimit, state.allPapers.length)} / ${state.allPapers.length}）`
    : "已经到底";
}

function openPaperDetail(index) {
  const paper = state.visiblePapers[Number(index)];
  if (!paper) return;

  const authors = Array.isArray(paper.authors) ? paper.authors.join(", ") : "";
  $("detailContent").innerHTML = `
    <div class="modal-title">
      <div>
        ${venueBadge(paper)}
        <h2>${escapeHtml(paper.title)}</h2>
        ${paper.title_zh ? `<p>${escapeHtml(paper.title_zh)}</p>` : ""}
      </div>
      <span class="priority ${escapeHtml(paper.read_priority || "low")}">${escapeHtml(paper.read_priority || "low")}</span>
    </div>
    <p class="paper-authors">${escapeHtml(authors)}</p>
    <div class="paper-meta">
      ${directionBadges(paper)}
      <span class="tag">${escapeHtml(paper.week)}</span>
      <span class="tag">${escapeHtml(paper.method_family || paper.theme || "未分类")}</span>
      ${isAuthorityVenue(paper) ? `<span class="tag authority">A会重点</span>` : ""}
      ${paper.ingest_source === "manual" ? `<span class="tag manual">手动</span>` : ""}
      ${paper.has_code ? `<span class="tag code">代码</span>` : ""}
      ${paper.hf_upvotes ? `<span class="tag">HF ${escapeHtml(paper.hf_upvotes)}</span>` : ""}
    </div>
    <section class="detail-section">
      <h3>摘要</h3>
      ${paper.abstract_zh ? `<p>${escapeHtml(paper.abstract_zh)}</p>` : `<p class="muted">暂无中文翻译，下一次豆包提取会补齐。</p>`}
      ${paper.abstract ? `<details><summary>英文摘要</summary><p>${escapeHtml(paper.abstract)}</p></details>` : ""}
    </section>
    <dl class="detail-grid">
      ${detailRow("问题", paper.problem)}
      ${detailRow("方法", paper.method)}
      ${detailRow("贡献", paper.contribution)}
      ${detailRow("关键发现", paper.key_finding)}
      ${detailRow("方法族", paper.method_family)}
      ${detailRow("交叉标签", paper.cross_direction)}
      ${detailRow("编辑对象", paper.edit_target)}
      ${detailRow("Agent 场景", paper.agent_setting)}
      ${detailRow("控制机制", paper.control_mechanism)}
      ${detailRow("评测环境", paper.evaluation_environment)}
      ${detailRow("评测信号", paper.evaluation_signal)}
      ${detailRow("失败模式", paper.failure_mode)}
      ${detailRow("可靠性风险", paper.reliability_risk)}
      ${detailRow("工业相关性", paper.industrial_relevance)}
      ${detailRow("Idea 可行性", paper.idea_feasibility)}
      ${detailRow("计算成本", paper.compute_cost)}
      ${detailRow("看点", paper.idea_hook)}
      ${detailRow("想问导师", paper.mentor_question)}
      ${detailRow("手动注入原因", paper.manual_reason)}
      ${detailRow("方向契合", paper.direction_fit)}
      ${detailRow("局限", paper.limitations)}
    </dl>
    <section class="detail-section">
      <h3>Baselines</h3>
      <div class="paper-meta">${chips(paper.baselines)}</div>
    </section>
    <section class="detail-section">
      <h3>Datasets</h3>
      <div class="paper-meta">${chips(paper.datasets)}</div>
    </section>
    <div class="paper-actions detail-actions">
      <a href="${escapeHtml(paper.url)}" target="_blank" rel="noreferrer">arXiv</a>
      ${paper.pdf_url ? `<a href="${escapeHtml(paper.pdf_url)}" target="_blank" rel="noreferrer">PDF</a>` : ""}
      ${paper.repo_url ? `<a href="${escapeHtml(paper.repo_url)}" target="_blank" rel="noreferrer">Code</a>` : ""}
      ${paper.venue_url ? `<a href="${escapeHtml(paper.venue_url)}" target="_blank" rel="noreferrer">Venue</a>` : ""}
    </div>
  `;
  $("paperModal").classList.remove("hidden");
  document.body.classList.add("modal-open");
}

function closePaperDetail() {
  $("paperModal").classList.add("hidden");
  document.body.classList.remove("modal-open");
}

async function loadAll() {
  state.summary = await fetchJson("/api/summary");
  if (staticData) {
    state.sourcePapers = staticData.papers || [];
  } else {
    const data = await fetchJson("/api/papers?week=all&direction=all&limit=100000");
    state.sourcePapers = data.papers || [];
  }
  if (!state.week) state.week = state.summary.current_week || "all";
  renderSummary();
  await loadMethodFamilies();
  await loadPapers();
}

function debounce(fn, delay) {
  let timer = null;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

$("weekSelect").addEventListener("change", (event) => {
  state.week = event.target.value;
  state.theme = "all";
  renderSummary();
  loadMethodFamilies();
  loadPapers();
});

$("directionSelect").addEventListener("change", (event) => {
  state.direction = event.target.value;
  state.theme = "all";
  renderSummary();
  loadMethodFamilies();
  loadPapers();
});

$("searchInput").addEventListener("input", debounce((event) => {
  state.query = event.target.value;
  loadPapers();
}, 180));

$("refreshBtn").addEventListener("click", () => loadAll());

$("showMoreBtn").addEventListener("click", () => {
  state.paperLimit += 20;
  renderPaperList();
});

$("papers").addEventListener("click", (event) => {
  const target = event.target instanceof Element ? event.target : null;
  const button = target ? target.closest("[data-detail-index]") : null;
  if (button) openPaperDetail(button.dataset.detailIndex);
});

$("modalClose").addEventListener("click", closePaperDetail);
$("paperModal").addEventListener("click", (event) => {
  if (event.target.id === "paperModal") closePaperDetail();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closePaperDetail();
});

loadAll().catch((error) => {
  console.error(error);
  $("papers").innerHTML = `<p class="empty">加载失败：${escapeHtml(error.message)}</p>`;
});
