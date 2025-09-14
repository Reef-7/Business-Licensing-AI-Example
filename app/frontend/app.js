const apiUrl = "http://127.0.0.1:8000/api/generate-report";
function colorByPriority(priority) {
    switch (priority) {
        case "high": return "red";
        case "medium": return "orange";
        case "low": return "green";
        default: return "black";
    }
}

document.getElementById('send').addEventListener('click', async () => {
    const body = {
        name: document.getElementById('name').value || "עסק לדוגמה",
        area_sqm: Number(document.getElementById('area').value || 0),
        seating: Number(document.getElementById('seating').value || 0),
        uses_gas: document.getElementById('gas').checked,
        serves_meat: document.getElementById('meat').checked,
        delivers: document.getElementById('deliver').checked
    };

    document.getElementById('result').innerText = "מייצר דוח...";

    try {
        const res = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });
        const data = await res.json();

        // אם קיימות דרישות ממופות
        const mapped = data.mapped_requirements || [];

        // מיון לפי סדר עדיפות
        const priorityOrder = { high: 1, medium: 2, low: 3 };
        mapped.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);

        // הצגה מסודרת לפי קטגוריות
        document.getElementById('result').innerHTML = `
    <h4>דרישות חלות:</h4>
    ${mapped.map(item => `<div style="color:${colorByPriority(item.priority)}">
        <strong>${item.title}</strong>: ${item.details}</div>`).join("")}

    <h4>סדר עדיפויות:</h4>
    <ul>
    ${mapped.map(item => `<li>${item.title} (${item.priority})</li>`).join("")}</ul>

    <h4>דוח מלא:</h4>
    <pre>${data.report}</pre>
    `;

        // כפתור הורדה
        document.getElementById('downloadBtn').onclick = () => {
            const blob = new Blob([data.report], { type: "text/plain;charset=utf-8" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "report.txt";
            a.click();
            URL.revokeObjectURL(url);
        };

    } catch (err) {
        document.getElementById('result').innerText = "שגיאה: " + err;
    }

});
