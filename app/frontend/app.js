const apiUrl = "http://127.0.0.1:8000/api/generate-report";

function colorByPriority(priority) {
    switch (priority) {
        case "high": return "high";
        case "medium": return "medium";
        case "low": return "low";
        default: return "";
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

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<span class="loading">🕐 מייצר דוח...</span>';

    try {
        const res = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });
        const data = await res.json();

        const mapped = data.mapped_requirements || [];
        const priorityOrder = { high: 1, medium: 2, low: 3 };
        mapped.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);

        // הצגת דוח בכרטיסים לפי עדיפות
        const cardsHtml = mapped.map(item => `
            <div class="card ${colorByPriority(item.priority)}">
                <strong>${item.title}</strong><br>
                ${item.details}<br>
                <em>עדיפות: ${item.priority}</em>
            </div>
        `).join('');

        // דוח מלא
        const fullReport = `<h4>דוח מלא:</h4><pre>${data.report}</pre>`;

        resultDiv.innerHTML = cardsHtml + fullReport;

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
        resultDiv.innerHTML = "<span style='color:red;'>שגיאה: " + err + "</span>";
    }
});
