document.getElementById("b").onclick = async () => {
  let t = document.getElementById("in").value;
  let j = JSON.parse(t);

  let r = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(j),
  });

  let d = await r.json();
  let o = document.getElementById("out");
  o.innerHTML = "";

  d.forEach((i) => {
    let c = document.createElement("div");
    c.className = "card";

    let clockSvg = `
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="12" r="10" stroke="#5d0775" stroke-width="2"/>
        <line x1="12" y1="12" x2="12" y2="7" stroke="#5d0775" stroke-width="2"/>
        <line x1="12" y1="12" x2="16" y2="12" stroke="#5d0775" stroke-width="2"/>
      </svg>
    `;

    c.innerHTML = `
      <div class="top-row">
        <h4 class="t">${i.title}</h4>
        <div class="due">Due: <span>${i.due_date}</span></div>
      </div>

      <div class="mid-left">
        <div class="row">Score: <span>${i.score}</span></div>
        <div class="row">Importance: <span>${i.importance}</span></div>
        <div class="row"><div class="clock-box">
        ${clockSvg}
      </div>Hours: <span>${i.estimated_hours}</span></div>
      </div>

      
    `;

    o.appendChild(c);
  });
};
