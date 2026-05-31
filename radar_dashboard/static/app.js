const state = {
  summary: null,
  week: "",
  direction: "all",
  query: "",
  theme: "all",
  visiblePapers: [],
};

const colors = ["#2f7d62", "#3867a6", "#a64f3c", "#9a6b20", "#6f5aa8"];
const staticData = window.location.protocol === "file:" ? (window.RADAR_STATIC_DATA || null) : null;

const $ = (id) => document.getElementById(id);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
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
    return Promise.resolve({ themes: staticData.summary.method_families || [] });
  }
  return Promise.reject(new Error(`Static data route not found: ${url}`));
}

function filterStaticPapers(params) {
  const week = params.get("week") || "";
  const direction = params.get("direction") || "";
  const query = (params.get("q") || "").trim().toLowerCase();
  const theme = (params.get("theme") || "").trim();
  const limit = Number(params.get("limit") || 120);

  let result = staticData.papers || [];
  if (week && week !== "all") {
    result = result.filter((paper) => paper.week === week);
  }
  if (direction && direction !== "all") {
    result = result.filter((paper) => paper.direction_id === direction);
  }
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
        "problem",
        "method",
        "contribution",
        "limitations",
        "key_finding",
        "theme",
        "method_family",
        "edit_target",
        "evaluation_signal",
        "failure_mode",
        "idea_hook",
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

function setOptions(select, options, value) {
  select.innerHTML = options.map((option) => (
    `<option value="${escapeHtml(option.value)}">${escapeHtml(option.label)}</option>`
  )).join("");
  select.value = value;
}

function renderSummary() {
  const summary = state.summary;
  const source = staticData ? `静态快照 · ${staticData.generated_at || "local"}` : "实时 API";
  $("subtitle").textContent = `Knowledge editing / unlearning / reliability · ${summary.current_week || "no week"} · ${source}`;
  $("totalPapers").textContent = summary.total_papers;
  $("totalCode").textContent = summary.total_code;
  $("directionCount").textContent = summary.directions.length;
  $("currentWeek").textContent = summary.current_week || "-";

  const weekOptions = [
    ...summary.weeks.map((week) => ({ value: week, label: week })),
    { value: "all", label: "全部周" },
  ];
  setOptions($("weekSelect"), weekOptions, state.week || summary.current_week || "all");

  const directionOptions = [
    { value: "all", label: "全部方向" },
    ...summary.directions.map((direction) => ({ value: direction.id, label: direction.name })),
  ];
  setOptions($("directionSelect"), directionOptions, state.direction);

  renderTrend(summary);
  renderDirections(summary);
  renderMethodFamilies(summary);
  renderVenues(summary);
  renderFailureModes(summary);
  renderEvaluationSignals(summary);
  renderIdeaHooks(summary);
  renderCodePapers(summary);
}

function renderVenues(summary) {
  const venues = summary.venues || [];
  $("venueList").innerHTML = venues.map(([venue, count]) => (
    `<li><span class="venue venue-${escapeHtml(String(venue).toLowerCase())}">${escapeHtml(venue)}</span> <span class="tag">${count}</span></li>`
  )).join("") || `<li>本周暂无已识别 A 会标签</li>`;
}

function renderTrend(summary) {
  const maxTotal = Math.max(1, ...summary.trend.map((row) => row.total));
  $("trendChart").innerHTML = summary.trend.map((row) => {
    const segments = summary.directions.map((direction, index) => {
      const count = row.directions[direction.id] || 0;
      const width = row.total ? (count / row.total) * 100 : 0;
      return `<span class="trend-seg" title="${escapeHtml(direction.name)}: ${count}" style="width:${width}%;background:${colors[index % colors.length]}"></span>`;
    }).join("");
    const barWidth = row.total ? Math.max(6, (row.total / maxTotal) * 100) : 2;
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
    const highText = high ? `<span>${high[1]} high</span>` : "";
    return `
      <article class="direction-card" style="border-left:4px solid ${colors[index % colors.length]}">
        <h3>${escapeHtml(direction.name)}</h3>
        <p>${escapeHtml(direction.description)}</p>
        <div class="direction-stats">
          <span>${direction.count} 篇</span>
          <span>${direction.code_count} 代码</span>
          ${highText}
        </div>
        <div class="paper-meta">${families}</div>
      </article>
    `;
  }).join("") || `<p class="empty">暂无方向配置</p>`;
}

function renderMethodFamilies(summary) {
  const families = summary.method_families || [];
  const chips = families.map(([family, count]) => (
    `<button class="chip ${state.theme === family ? "active" : ""}" type="button" data-theme="${escapeHtml(family)}">${escapeHtml(family)} · ${count}</button>`
  )).join("");
  $("themeCloud").innerHTML = `<button class="chip ${state.theme === "all" ? "active" : ""}" type="button" data-theme="all">全部</button>${chips || `<span class="empty-inline">暂无数据</span>`}`;
  $("themeCloud").querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      state.theme = button.dataset.theme;
      loadPapers();
      renderMethodFamilies(state.summary);
    });
  });
}

function renderFailureModes(summary) {
  $("failureModesList").innerHTML = (summary.failure_modes || []).map(([text, count]) => (
    `<li>${escapeHtml(text)} <span class="tag">${count}</span></li>`
  )).join("") || `<li>本周摘要未显式提到 failure mode</li>`;
}

function renderEvaluationSignals(summary) {
  $("evaluationSignalsList").innerHTML = (summary.evaluation_signals || []).map(([text, count]) => (
    `<li>${escapeHtml(text)} <span class="tag">${count}</span></li>`
  )).join("") || `<li>本周暂无明确评测信号</li>`;
}

function renderIdeaHooks(summary) {
  $("ideaHooksList").innerHTML = (summary.idea_hooks || []).map((item) => (
    `<li><span class="priority ${escapeHtml(item.read_priority)}">${escapeHtml(item.read_priority)}</span> ${escapeHtml(item.idea_hook)}<br><a href="${escapeHtml(item.url)}" target="_blank" rel="noreferrer">${escapeHtml(item.title)}</a></li>`
  )).join("") || `<li>本周暂无可延展 idea hook</li>`;
}

function renderCodePapers(summary) {
  $("codeList").innerHTML = summary.code_papers.map((paper) => (
    `<li><a href="${escapeHtml(paper.url)}" target="_blank" rel="noreferrer">${escapeHtml(paper.title)}</a><br><span>${escapeHtml(paper.direction_name)}</span>${paper.repo_url ? ` · <a href="${escapeHtml(paper.repo_url)}" target="_blank" rel="noreferrer">repo</a>` : ""}</li>`
  )).join("") || `<li>本周暂无带代码论文</li>`;
}

function venueBadge(paper) {
  if (!paper.venue) return "";
  const year = paper.venue_year ? ` ${paper.venue_year}` : "";
  const type = paper.venue_type ? ` · ${paper.venue_type}` : "";
  const label = `${paper.venue}${year}${type}`;
  const cls = `venue venue-${String(paper.venue).toLowerCase()}`;
  const content = `<span class="${escapeHtml(cls)}">${escapeHtml(label)}</span>`;
  if (paper.venue_url) {
    return `<a class="venue-link" href="${escapeHtml(paper.venue_url)}" target="_blank" rel="noreferrer">${content}</a>`;
  }
  return content;
}

function chips(values) {
  if (!Array.isArray(values) || values.length === 0) return `<span class="muted">未提及</span>`;
  return values.map((value) => `<span class="tag">${escapeHtml(value)}</span>`).join("");
}

function detailRow(label, value) {
  const text = String(value || "").trim();
  if (!text) return "";
  return `<div><dt>${escapeHtml(label)}</dt><dd>${escapeHtml(text)}</dd></div>`;
}

function paperCard(paper, index) {
  const authors = Array.isArray(paper.authors) ? paper.authors.slice(0, 4).join(", ") : "";
  return `
    <article class="paper-card">
      <h3><a href="${escapeHtml(paper.url)}" target="_blank" rel="noreferrer">${escapeHtml(paper.title)}</a></h3>
      ${paper.title_zh ? `<p class="paper-title-zh">${escapeHtml(paper.title_zh)}</p>` : ""}
      <div class="paper-meta">
        ${venueBadge(paper)}
        <span class="tag">${escapeHtml(paper.direction_name)}</span>
        <span class="tag">${escapeHtml(paper.week)}</span>
        <span class="tag">${escapeHtml(paper.method_family || paper.theme)}</span>
        <span class="priority ${escapeHtml(paper.read_priority)}">${escapeHtml(paper.read_priority)}</span>
        ${paper.has_code ? `<span class="tag code">代码</span>` : ""}
      </div>
      <dl>
        <div><dt>Method Family</dt><dd>${escapeHtml(paper.method_family || "未分类")}</dd></div>
        <div><dt>Method</dt><dd>${escapeHtml(paper.method || "未提取")}</dd></div>
        <div><dt>Key Finding</dt><dd>${escapeHtml(paper.key_finding || "未提取")}</dd></div>
        <div><dt>Evaluation Signal</dt><dd>${escapeHtml(paper.evaluation_signal || "摘要未提及")}</dd></div>
        <div><dt>Failure Mode</dt><dd>${escapeHtml(paper.failure_mode || "摘要未提及")}</dd></div>
        <div><dt>Idea Hook</dt><dd>${escapeHtml(paper.idea_hook || "暂不明显")}</dd></div>
        <div><dt>Direction Fit</dt><dd>${escapeHtml(paper.direction_fit || "未提取")}</dd></div>
      </dl>
      <div class="paper-actions">
        <button class="detail-btn" type="button" data-detail-index="${index}">详情</button>
        <a href="${escapeHtml(paper.url)}" target="_blank" rel="noreferrer">arXiv</a>
        ${paper.pdf_url ? `<a href="${escapeHtml(paper.pdf_url)}" target="_blank" rel="noreferrer">PDF</a>` : ""}
        ${paper.repo_url ? `<a href="${escapeHtml(paper.repo_url)}" target="_blank" rel="noreferrer">Code</a>` : ""}
      </div>
      ${authors ? `<p class="paper-authors">${escapeHtml(authors)}</p>` : ""}
    </article>
  `;
}

async function loadPapers() {
  const params = new URLSearchParams({
    week: state.week || state.summary.current_week,
    direction: state.direction,
    q: state.query,
    theme: state.theme,
    limit: "180",
  });
  const data = await fetchJson(`/api/papers?${params.toString()}`);
  state.visiblePapers = data.papers;
  $("paperCount").textContent = `${data.papers.length} papers`;
  $("papers").innerHTML = data.papers.map((paper, index) => paperCard(paper, index)).join("") || `<p class="empty">没有匹配论文</p>`;
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
      <span class="priority ${escapeHtml(paper.read_priority)}">${escapeHtml(paper.read_priority || "low")}</span>
    </div>
    <p class="paper-authors">${escapeHtml(authors)}</p>
    <div class="paper-meta">
      <span class="tag">${escapeHtml(paper.direction_name)}</span>
      <span class="tag">${escapeHtml(paper.week)}</span>
      <span class="tag">${escapeHtml(paper.method_family || paper.theme || "未分类")}</span>
      ${paper.has_code ? `<span class="tag code">代码</span>` : ""}
      ${paper.hf_upvotes ? `<span class="tag">HF ${escapeHtml(paper.hf_upvotes)}</span>` : ""}
    </div>
    <section class="detail-section">
      <h3>摘要</h3>
      ${paper.abstract_zh ? `<p>${escapeHtml(paper.abstract_zh)}</p>` : `<p class="muted">暂无中文翻译，下一次豆包提取会补齐。</p>`}
      ${paper.abstract ? `<details><summary>英文摘要</summary><p>${escapeHtml(paper.abstract)}</p></details>` : ""}
    </section>
    <dl class="detail-grid">
      ${detailRow("Problem", paper.problem)}
      ${detailRow("Method", paper.method)}
      ${detailRow("Contribution", paper.contribution)}
      ${detailRow("Key Finding", paper.key_finding)}
      ${detailRow("Method Family", paper.method_family)}
      ${detailRow("Edit Target", paper.edit_target)}
      ${detailRow("Evaluation Signal", paper.evaluation_signal)}
      ${detailRow("Failure Mode", paper.failure_mode)}
      ${detailRow("Idea Hook", paper.idea_hook)}
      ${detailRow("Direction Fit", paper.direction_fit)}
      ${detailRow("Limitations", paper.limitations)}
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
  if (!state.week) state.week = state.summary.current_week || "all";
  renderSummary();
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
  loadPapers();
});

$("directionSelect").addEventListener("change", (event) => {
  state.direction = event.target.value;
  state.theme = "all";
  loadPapers();
});

$("searchInput").addEventListener("input", debounce((event) => {
  state.query = event.target.value;
  loadPapers();
}, 180));

$("refreshBtn").addEventListener("click", () => loadAll());

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
