// Material for MkDocs owns Mermaid rendering and calls mermaid.initialize()
// itself with its own theme. Merge our one setting into that call: wide
// flowcharts keep their natural size (scrollable) instead of being scaled
// down until the labels are unreadable.
(() => {
  const mermaid = window.mermaid;
  if (!mermaid) return;
  const initialize = mermaid.initialize.bind(mermaid);
  mermaid.initialize = (options = {}) =>
    initialize({
      ...options,
      flowchart: { ...options.flowchart, useMaxWidth: false },
    });
})();
