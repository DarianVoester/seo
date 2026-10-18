import time
from pathlib import Path
import webbrowser

# Number A 
zahl_a = (X)
print(f"Zahl A: {zahl_a}")

# List of URLs
urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    # Extend list
]

# Create HTML file in the current directory
html_file = Path.cwd() / "/content/Test1.html"

# HTML-Template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Dynamische Links</title>
    <meta charset="UTF-8">
    <style>
        .count-display {
            font-size: 48px;
            text-align: center;
            margin: 20px 0;
            font-weight: bold;
            color: #333;
        }
        #link-container {
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        a {
            display: block;
            margin: 10px 0;
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    <script>
        var anzahl_urls = %s;
        var urls = %s;
        function loadLinks() {
            var html = "<div class='count-display'>Anzahl Links: " + anzahl_urls + "</div>";
            html += "<div id='link-container'>";
            for (var i = 0; i < anzahl_urls; i++) {
                html += '<a href="' + urls[i] + '" target="_blank">' + urls[i] + '</a>';
            }
            html += "</div>";
            document.body.innerHTML = html;
        }
        setInterval(loadLinks, 10000); // Aktualisiere alle 10 Sekunden
    </script>
</head>
<body onload="loadLinks()">
</body>
</html>
"""

# Initial HTML-Markup
html = html_template % (zahl_a, urls)
html_file.write_text(html, encoding="utf-8")

# Open HTML file in standard browser
webbrowser.open(str(html_file))

while True:
    # Select time period (X, X, X or X minutes)
    zeitspanne = ([X, X, X, X])
    print(f"Zahl A ({zahl_a}) bleibt für {zeitspanne} Minuten gleich.")
    
    # Convert time span to seconds and wait
    warte_sekunden = zeitspanne * 60
    time.sleep(warte_sekunden)
    
    # Generate number C
    zahl_c = (X)
    
    # Deciding whether the number C is added to or subtracted from the number A
    operation = (['+', '-'])
    neue_zahl = zahl_a
    if operation == '+':
        neue_zahl += zahl_c
    else:
        neue_zahl -= zahl_c
    
    # Limit new number to value range X-X
    neue_zahl = max(X, min(neue_zahl, X))
    
    print(f"Neue Zahl: {neue_zahl} (Zahl A bleibt {zahl_a})")
    
    # Create updated HTML markup and write to file
    html = html_template % (neue_zahl, urls)
    html_file.write_text(html, encoding="utf-8")
