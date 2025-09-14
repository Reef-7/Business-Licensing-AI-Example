const apiUrl = "http://127.0.0.1:8000/api/generate-report";

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
        // simple visualization of the report 
        document.getElementById('result').innerText = data.report || JSON.stringify(data, null, 2);
    } catch (err) {
        document.getElementById('result').innerText = "שגיאה: " + err;
    }
});
