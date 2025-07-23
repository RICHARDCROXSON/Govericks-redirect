fetch("config.json")
  .then(response => response.json())
  .then(config => {
    const { vectors, image } = config;
    const pageText = document.body.innerText.toLowerCase();

    const matched = vectors.toLowerCase().split(",").some(phrase =>
      pageText.includes(phrase.trim().toLowerCase())
    );

    if (matched) {
      const bubble = document.createElement("div");
      bubble.innerHTML = `
        <div style="font-weight:bold;">🔍 Advisory:</div>
        <div>
          This content relates to delivery risk that I advise on.
          <a href="https://www.govericks.com" target="_blank">To see more, click here.</a>
        </div>
        ${image ? <img src="${image}" style="max-width:100px;margin-top:10px;"> : ""}
      `;
      bubble.style.position = "fixed";
      bubble.style.bottom = "20px";
      bubble.style.right = "20px";
      bubble.style.background = "#fff";
      bubble.style.border = "1px solid #ccc";
      bubble.style.padding = "15px";
      bubble.style.zIndex = "9999";
      bubble.style.boxShadow = "0 0 10px rgba(0,0,0,0.2)";
      bubble.style.fontFamily = "sans-serif";
      bubble.style.maxWidth = "300px";
      document.body.appendChild(bubble);
    }
  });