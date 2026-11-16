/* Resolve the theme before rendering; System is the default for new visitors. */
(() => {
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const choices = ['system', 'light', 'dark'];
  let preference = 'system';
  try {
    const saved = localStorage.getItem('poc-theme');
    if (choices.includes(saved)) preference = saved;
  } catch (_) {}

  function apply() {
    const resolved = preference === 'system' ? (system.matches ? 'dark' : 'light') : preference;
    document.documentElement.dataset.theme = resolved;
    document.documentElement.dataset.themePreference = preference;
    const button = document.querySelector('.theme-toggle');
    if (button) {
      const next = choices[(choices.indexOf(preference) + 1) % choices.length];
      const label = `Theme: ${preference} (${resolved}). Switch to ${next}.`;
      button.setAttribute('aria-label', label);
      button.title = label;
      button.querySelectorAll('[data-theme-icon]').forEach(icon => {
        icon.toggleAttribute('hidden', icon.dataset.themeIcon !== preference);
      });
    }
  }
  apply();
  system.addEventListener('change', () => { if (preference === 'system') apply(); });
  window.addEventListener('storage', (event) => {
    if (event.key === 'poc-theme' || event.key === null) {
      preference = choices.includes(event.newValue) ? event.newValue : 'system';
      apply();
    }
  });
  document.addEventListener('DOMContentLoaded', () => {
    apply();
    document.querySelector('.theme-toggle')?.addEventListener('click', () => {
      preference = choices[(choices.indexOf(preference) + 1) % choices.length];
      try { localStorage.setItem('poc-theme', preference); } catch (_) {}
      apply();
    });
  });
})();
