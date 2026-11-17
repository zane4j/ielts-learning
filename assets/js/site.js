/* IELTS Learning · Shared lightweight interactions. No dependencies. */
(() => {
  "use strict";
  const root = document.documentElement;
  const stateLabel = (button, label) => {
    if (!button) return;
    const previous = button.dataset.originalLabel || button.textContent.trim();
    button.dataset.originalLabel = previous;
    button.textContent = label;
    window.setTimeout(() => { button.textContent = previous; }, 1600);
  };
  async function copyRichEssay(id, button) {
    const source = document.getElementById(id);
    if (!source) return;
    const clone = source.cloneNode(true);
    const sourceMarks = source.querySelectorAll("mark");
    const targetMarks = clone.querySelectorAll("mark");
    for (let i = 0; i < sourceMarks.length; i++) {
      const style = window.getComputedStyle(sourceMarks[i]);
      targetMarks[i].setAttribute("style", [
        "background-color:" + style.backgroundColor,
        "color:" + style.color,
        "font-weight:" + style.fontWeight,
        "text-decoration:" + style.textDecorationLine,
        "border-radius:2px",
        "padding:0 2px"
      ].join(";"));
    }
    const sourceParagraphs = source.querySelectorAll("p");
    const targetParagraphs = clone.querySelectorAll("p");
    for (let i = 0; i < sourceParagraphs.length; i++) {
      targetParagraphs[i].setAttribute("style", "margin:0 0 1.1em 0;font-family:Georgia,'Times New Roman',serif;font-size:17px;line-height:1.85;color:#172438");
    }
    const plainText = [...sourceParagraphs].map(p => p.textContent.trim()).join("\n\n");
    const htmlText = '<div>' + clone.innerHTML + '</div>';
    try {
      if (window.isSecureContext && navigator.clipboard && window.ClipboardItem) {
        await navigator.clipboard.write([
          new ClipboardItem({
            "text/html": new Blob([htmlText], {type:"text/html"}),
            "text/plain": new Blob([plainText], {type:"text/plain"})
          })
        ]);
        stateLabel(button,"已复制富文本");
        return;
      }
      const helper = document.createElement("div");
      helper.innerHTML = htmlText;
      helper.setAttribute("contenteditable","true");
      helper.style.cssText = "position:fixed;left:-9999px;top:0;white-space:normal;";
      document.body.appendChild(helper);
      const range = document.createRange();
      range.selectNodeContents(helper);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      const success = document.execCommand("copy");
      selection.removeAllRanges();
      helper.remove();
      if (success) {stateLabel(button,"已复制富文本");return;}
    } catch (err) {
      // Clipboard formats may be blocked by browsers/OS. Fall back to plain text.
    }
    try {
      if (navigator.clipboard) {
        await navigator.clipboard.writeText(plainText);
        stateLabel(button,"已复制纯文本");
      } else {
        stateLabel(button,"请手动选择复制");
      }
    } catch (_err) {stateLabel(button,"请手动选择复制");}
  }
  document.addEventListener("click", event => {
    const button = event.target.closest("[data-copy],[data-action]");
    if (!button) return;
    if (button.dataset.copy) {
      copyRichEssay(button.dataset.copy,button);
    } else if (button.dataset.action === "toggle-highlight") {
      const hidden = document.body.classList.toggle("clean");
      button.textContent = hidden ? "显示高亮" : "隐藏高亮";
      button.setAttribute("aria-pressed",String(hidden));
    } else if (button.dataset.action === "toggle-size") {
      const large = document.body.classList.toggle("reading-large");
      button.textContent = large ? "恢复字号" : "放大正文";
      button.setAttribute("aria-pressed",String(large));
    } else if (button.dataset.action === "print") {
      window.print();
    }
  });
  // On site pages, link to the primary content on keyboard focus.
  if (!document.querySelector(".skip-link") && document.querySelector("main")) {
    const link = document.createElement("a");
    link.className = "skip-link";
    link.href = "#main-content";
    link.textContent = "跳转到正文";
    const main = document.querySelector("main");
    if (!main.id) main.id = "main-content";
    document.body.prepend(link);
  }
})();