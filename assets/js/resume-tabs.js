/* Enhance the CV's section links; the full CV stays available without JS. */
document.querySelectorAll('[data-resume-tabs]').forEach((widget) => {
  const navigation = widget.querySelector('.resume-sections');
  const tabs = Array.from(navigation.querySelectorAll('[data-resume-tab]'));
  const panels = Array.from(widget.querySelectorAll('[data-resume-panel]'));

  function selectTab(tab, focus = false, updateHash = false) {
    tabs.forEach((item) => {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
    });
    panels.forEach((panel) => {
      panel.hidden = panel.dataset.resumePanel !== tab.dataset.resumeTab;
    });
    if (focus) tab.focus();
    if (updateHash) history.replaceState(null, '', tab.getAttribute('href'));
  }

  function selectFromHash() {
    const target = document.getElementById(location.hash.slice(1));
    const panel = target && target.closest('[data-resume-panel]');
    const tab = panel && tabs.find((item) => item.dataset.resumeTab === panel.dataset.resumePanel);
    selectTab(tab || tabs[0]);
  }

  navigation.setAttribute('role', 'tablist');
  tabs.forEach((tab, index) => {
    const panel = panels.find((item) => item.dataset.resumePanel === tab.dataset.resumeTab);
    tab.setAttribute('role', 'tab');
    tab.setAttribute('aria-controls', panel.id);
    panel.setAttribute('role', 'tabpanel');
    panel.setAttribute('aria-labelledby', tab.id);
    panel.tabIndex = 0;
    tab.addEventListener('click', (event) => {
      event.preventDefault();
      selectTab(tab, false, true);
    });
    tab.addEventListener('keydown', (event) => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      selectTab(tabs[next], true, true);
    });
  });
  selectFromHash();
  window.addEventListener('hashchange', selectFromHash);
});
