import operator
import re

search_terms = {
    "Red Team": "#e00007",
    "Green Team": "#02990e",
    "Blue Team": "#0074ad",
    "Black Team": "#202024",
    "Teutons": "#020061",
    "Locked Land": "#051020",
    "Dfs Testing Army": "#adbfde",
    "Scarlet Republic": "#a51010",
    "Club Penguin Armies": "#87d1ff",
    "CPA Battleground": "#ff4d4d",
    "Club Penguin Army Judges": "#ff3366",
    "Templars": "#f1c40f",
    "Army of Club Penguin": "#2b8b1f",
    "Doritos of Club Penguin": "#ff6a13",
    "Special Weapons and Tactics": "#40ff40",
    "Help Force": "#000dff",
    "Rebel Penguin Federation": "#060505",
    "Aliens": "#90ee90",
    "Water Vikings": "#043acf",
    "Penguins of Agartha": "#12690e",
    "Fire Vikings": "#8b0000",
    "Elite Guardians of Club Penguin": "#787e7f",
    "Elite Guardians of CP": "#787e7f", 
    "Star Force": "#000050",
    "Dark Warriors": "#080808",
    "Shreks of CP": "#b0c400",
    "Peoples Imperial Confederation": "#aa54ff",
    "wii phone": "#ffffff",
    "Romans": "#730000",
    "Seraphic Imperium": "#c3ccd3",
    "Void Troops": "#3d0eac",
    "Shadow Legionaries": "#2d0b7d",
    "Marines": "#46b8ff",
    "Kanye West Army": "#853082",
    "Tsunamis of Club Penguin": "#0099cc",
    "Winged Hussars": "#ff3333",
    "Smart Penguins": "#ff6666",
    "Freeland" : "#666666"
}

with open('map.js', 'r') as file:
    content = file.read()

# 1. Calculate and Sort using Regex
# This looks strictly for '"controller": "Army Name"' to avoid counting code logic.
army_data = []
for term, color in search_terms.items():
    # Regex pattern: "controller" followed by colon, whitespace, quote, Army Name, quote
    # re.IGNORECASE ensures it captures variations in capitalization if they exist
    pattern = r'"controller":\s*"' + re.escape(term) + r'"'
    count = len(re.findall(pattern, content, re.IGNORECASE))
    
    if count >= 1:
        army_data.append({ "name": term, "count": count, "color": color })

army_data.sort(key=operator.itemgetter('count'), reverse=False)

# 2. Generate HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">

<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap" rel="stylesheet">
<style>
    /* CUSTOM SCROLLBAR */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.2); border-radius: 4px; }
    ::-webkit-scrollbar-thumb { background: #1c3d5e; border-radius: 4px; border: 1px solid rgba(0, 243, 255, 0.1); }
    ::-webkit-scrollbar-thumb:hover { background: #00f3ff; box-shadow: 0 0 10px #00f3ff; }
    html { scrollbar-width: thin; scrollbar-color: #1c3d5e rgba(0, 0, 0, 0.2); }

    /* GENERAL STYLE */
    body {
        background: transparent;
        font-family: 'Rajdhani', sans-serif;
        margin: 0;
        padding: 5px 10px 5px 5px;
        overflow-x: hidden;
        overflow-y: auto;
        user-select: none;
    }

    .army-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(20, 30, 50, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left-width: 5px;
        margin-bottom: 8px;
        padding: 12px 15px;
        border-radius: 4px;
        backdrop-filter: blur(4px);
        transition: transform 0.2s, background 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        cursor: pointer;
        position: relative;
    }

    .army-card:hover {
        transform: translateX(5px);
        background: rgba(40, 50, 80, 0.95);
        border-color: rgba(0, 243, 255, 0.3);
    }

    .army-name {
        color: #e0e6ed;
        font-weight: 700;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .army-count {
        background: rgba(255,255,255,0.1);
        color: #fff;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.85rem;
        font-weight: bold;
    }
</style>
</head>
<body>
"""

for army in army_data:
    html_content += f'''
    <div class="army-card" style="border-left-color: {army['color']};">
        <span class="army-name">{army['name']}</span>
        <span class="army-count">{army['count']}</span>
    </div>
    '''

html_content += """
<script>
    const cards = document.querySelectorAll('.army-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            const name = card.querySelector('.army-name').innerText;
            window.parent.postMessage({ type: 'hoverArmy', army: name }, '*');
        });
        card.addEventListener('mouseleave', () => {
            window.parent.postMessage({ type: 'resetMap' }, '*');
        });
    });
</script>
</body>
</html>
"""

with open("army_code.html", 'w') as file:
    file.write(html_content)
print("army_code.html updated. Logic fixed to exclude code comments/assignments.")

with open("army_code.html", 'w') as file:
    file.write(html_content)
print("army_code.html updated with NO-CACHE tags.")
