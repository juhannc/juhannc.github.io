/* Citation text remains visible in both formats when JavaScript is unavailable. */
document.querySelectorAll('[data-citation-widget]').forEach((widget) => {
  const tablist = widget.querySelector('[data-citation-tabs]');
  const tabs = Array.from(tablist.querySelectorAll('[data-citation-format]'));
  const panels = Array.from(widget.querySelectorAll('[data-citation-panel]'));
  const copy = widget.querySelector('[data-citation-copy]');
  const status = widget.querySelector('[data-citation-status]');
  let activeTab = tabs[0];

  function selectTab(tab, focus = false) {
    activeTab = tab;
    tabs.forEach((item) => {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
    });
    panels.forEach((panel) => {
      panel.hidden = panel.dataset.citationPanel !== tab.dataset.citationFormat;
    });
    status.textContent = '';
    if (focus) tab.focus();
  }

  tablist.setAttribute('role', 'tablist');
  tabs.forEach((tab, index) => {
    tab.setAttribute('role', 'tab');
    tab.addEventListener('click', () => selectTab(tab));
    tab.addEventListener('keydown', (event) => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      selectTab(tabs[next], true);
    });
  });
  panels.forEach((panel) => {
    panel.setAttribute('role', 'tabpanel');
    panel.setAttribute('aria-labelledby', `citation-tab-${panel.dataset.citationPanel}`);
    panel.querySelector('h3').hidden = true;
  });
  selectTab(activeTab);
  tablist.hidden = false;
  copy.hidden = false;

  copy.addEventListener('click', async () => {
    const panel = panels.find((item) => item.dataset.citationPanel === activeTab.dataset.citationFormat);
    const code = panel.querySelector('code');
    try {
      await navigator.clipboard.writeText(code.textContent);
      status.textContent = `${activeTab.textContent.trim()} citation copied.`;
    } catch {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(code);
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy.';
    }
  });
});
