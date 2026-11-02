"use strict";
/* ========== 1. CONFIG & LOG (debug) ========== */
// Para depurar: adicione ?debug=1 na URL ou rode localStorage.setItem("debug","1")
const CONFIG = { email: "seu.email@exemplo.com" };
const DEBUG = (() => {
  try { return new URLSearchParams(location.search).has("debug") || localStorage.getItem("debug") === "1"; }
  catch { return false; }
})();
const log = (...a) => { if (DEBUG) console.log("[portfolio]", ...a); };
window.addEventListener("error", e => console.error("[portfolio] Erro:", e.message, e.filename, e.lineno));
window.addEventListener("unhandledrejection", e => console.error("[portfolio] Promise rejeitada:", e.reason));
 
/* ========== 2. DADOS (edite aqui) ========== */
const SKILLS = {
  "Front-end": ["HTML5", "CSS3", "JavaScript", "Responsividade","Bootstrap","tailwind CSS"],
  "Back-end": ["Node.js", "Python", "REST APIs"],
  "Banco de dados": ["linguagem SQL","Modelagem de Dados"],
  "Ferramentas": ["Git/GitHub", "Scrum/Kanban","Docker"]

};
//const PROJECTS = [
//  { title: "Sistema de Tarefas", desc: "Aplicação para gerenciar tarefas com filtros e persistência local.", tags: ["JavaScript", "CSS"], repo: "https://github.com/seu-usuario/projeto-1", demo: "" },
//  { title: "API de Cadastro", desc: "API REST com validação de dados e documentação dos endpoints.", tags: ["Node.js", "SQL"], repo: "https://github.com/seu-usuario/projeto-2", demo: "" },
//  { title: "Landing Page Responsiva", desc: "Página mobile-first com foco em acessibilidade e performance.", tags: ["HTML", "CSS"], repo: "https://github.com/seu-usuario/projeto-3", demo: "" }
//];
 
/* ========== 3. UTILITÁRIOS SEGUROS ========== */
// Sempre textContent (nunca innerHTML) para evitar XSS.
function el(tag, { text, cls, attrs } = {}, children = []) {
  const n = document.createElement(tag);
  if (text) n.textContent = text;
  if (cls) n.className = cls;
  if (attrs) for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
  children.forEach(c => n.appendChild(c));
  return n;
}
const isHttps = u => { try { return new URL(u).protocol === "https:"; } catch { return false; } };
const link = (label, href) => el("a", { text: label, attrs: { href, target: "_blank", rel: "noopener noreferrer" } });
 
/* ========== 4. RENDERIZAÇÃO ========== */
function renderSkills() {
  const root = document.getElementById("skills");
  for (const [group, items] of Object.entries(SKILLS)) {
    const ul = el("ul", { cls: "tags" }, items.map(i => el("li", { text: i, cls: "tag" })));
    root.appendChild(el("div", { cls: "card" }, [el("h3", { text: group }), ul]));
  }
  log("skills renderizadas");
}
function renderProjects() {
  const root = document.getElementById("projects");
  for (const p of PROJECTS) {
    const links = el("div", { cls: "project__links" });
    if (isHttps(p.repo)) links.appendChild(link("Código", p.repo));
    if (isHttps(p.demo)) links.appendChild(link("Demo", p.demo));
    const tags = el("ul", { cls: "tags" }, p.tags.map(t => el("li", { text: t, cls: "tag" })));
    root.appendChild(el("article", { cls: "card project" }, [
      el("h3", { text: p.title }), el("p", { text: p.desc, cls: "muted" }), tags, links
    ]));
  }
  log("projetos renderizados:", PROJECTS.length);
}
 
/* ========== 5. TEMA ========== */
function initTheme() {
  const root = document.documentElement;
  try { const s = localStorage.getItem("theme"); if (s === "light" || s === "dark") root.dataset.theme = s; } catch {}
  document.getElementById("theme-btn").addEventListener("click", () => {
    const dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch {}
    log("tema:", root.dataset.theme);
  });
}
 
/* ========== 6. MENU MOBILE + LINK ATIVO ========== */
function initNav() {
  const btn = document.getElementById("menu-btn"), menu = document.getElementById("menu");
  const close = () => { menu.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false"); };
  btn.addEventListener("click", () => {
    const open = menu.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", String(open));
  });
  menu.addEventListener("click", e => { if (e.target.closest("a")) close(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") close(); });
 
  if (!("IntersectionObserver" in window)) return;
  const links = [...menu.querySelectorAll("a")];
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      links.forEach(a => a.setAttribute("aria-current", String(a.hash === "#" + en.target.id)));
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  document.querySelectorAll("main section[id]").forEach(s => io.observe(s));
}
 
/* ========== 7. ANIMAÇÃO DE ENTRADA ========== */
function initReveal() {
  const items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) { items.forEach(i => i.classList.add("is-visible")); return; }
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add("is-visible"); obs.unobserve(en.target); } });
  }, { threshold: .12 });
  items.forEach(i => io.observe(i));
}
 
/* ========== 8. FORMULÁRIO ========== */
async function initForm() {
  const form = document.getElementById("form");
  
  // Se não houver formulário na página, para a execução
  if (!form) return;

  const rules = {
    name: v => v.trim().length >= 2 || "Informe seu nome.",
    email: v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) || "Informe um e-mail válido.",
    message: v => v.trim().length >= 10 || "Escreva ao menos 10 caracteres."
  };

  const check = field => {
    const res = rules[field.name](field.value);
    const msg = res === true ? "" : res;
    form.querySelector(`[data-error-for="${field.name}"]`).textContent = msg;
    field.setAttribute("aria-invalid", String(Boolean(msg)));
    return !msg;
  };

  // Validação em tempo real
  form.addEventListener("input", e => { 
    if (e.target.name in rules) check(e.target); 
  });

  // Novo envio via Formspree
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const fields = [...form.elements].filter(f => f.name in rules);
    
    // Se algum campo estiver inválido, para aqui
    if (!fields.map(check).every(Boolean)) { 
      fields.find(f => f.getAttribute("aria-invalid") === "true").focus(); 
      return; 
    }

    const formData = new FormData(form);
    const btn = form.querySelector('button[type="submit"]');
    
    // UX: Desabilita o botão
    const originalText = btn.textContent;
    btn.textContent = "Enviando...";
    btn.disabled = true;

    try {
      const response = await fetch(form.action, {
        method: "POST",
        body: formData,
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        form.reset();
        alert("Mensagem enviada com sucesso! Entrarei em contato em breve.");
      } else {
        alert("Ops! Ocorreu um erro ao enviar. Tente novamente ou use o WhatsApp.");
      }
    } catch (error) {
      alert("Erro de conexão. Verifique sua internet ou tente novamente mais tarde.");
    } finally {
      btn.textContent = originalText;
      btn.disabled = false;
    }
  });
}

// Não esqueça de chamar a função quando a página carregar!
document.addEventListener("DOMContentLoaded", initForm);
 
/* ========== 9. INICIALIZAÇÃO ========== */
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("year").textContent = new Date().getFullYear();
  [renderSkills, renderProjects, initTheme, initNav, initReveal, initForm].forEach(fn => {
    try { fn(); } catch (err) { console.error(`[portfolio] falha em ${fn.name}:`, err); }
  });
  log("inicializado");
});
 