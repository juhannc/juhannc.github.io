(() => {
  const theme = document.querySelector('.theme-toggle');
  theme?.addEventListener('click', () => {
    const dark = document.documentElement.dataset.theme !== 'dark';
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    try { localStorage.setItem('poc-theme', dark ? 'dark' : 'light'); } catch (_) {}
  });
  const controls = document.querySelector('[data-library-controls]');
  if (!controls) return;
  controls.hidden = false;
  const search = document.querySelector('#paper-search');
  const year = document.querySelector('#paper-year');
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const papers = [...document.querySelectorAll('[data-paper]')];
  let category = '';
  function update() {
    const words = search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    papers.forEach(p => {
      const show = (!category || p.dataset.category === category) && (!year.value || p.dataset.year === year.value) && words.every(w => p.dataset.search.includes(w));
      p.hidden = !show;
      if (show) count++;
    });
    document.querySelector('[data-result-count]').textContent = `${count} ${count === 1 ? 'Work' : 'Works'}`;
    document.querySelector('[data-empty]').hidden = count !== 0;
    buttons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === category)));
  }
  buttons.forEach(b => b.addEventListener('click', () => { category = b.dataset.filter; update(); }));
  search.addEventListener('input', update);
  year.addEventListener('change', update);
  document.querySelector('[data-reset]').addEventListener('click', () => { category = ''; search.value = ''; year.value = ''; update(); search.focus(); });
})();
