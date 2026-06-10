import operator

search_terms = {
    "Club Penguin Armies": "#87d1ff",
    "CPA Battleground": "#ff4d4d",
    "Club Penguin Army Judges": "#ff3366",
    "Water Vikings": "#3399ff",
    "Army of Club Penguin": "#00cc00",
    "Elite Guardians of Club Penguin": "#b0b0b0",
    "Special Weapons and Tactics": "#00ff00",
    "Silver Empire": "#ffffff",
    "People's Imperial Confederation": "#9966ff",
    "Dark Pirates": "#ff3333",
    "Templars": "#ffcc00",
    "Rebel Penguin Federation": "#ffffff",
    "Winged Hussars": "#ff3333",
    "Help Force": "#3366ff",
    "Smart Penguins": "#ff6666",
    "Warlords of Kosmos": "#888888",
    "Freeland" : "#666666"
}

with open('map.js', 'r') as file:
    content = file.read()

# 1. Calcular e Ordenar
army_data = []
for term, color in search_terms.items():
    count = content.lower().count(term.lower()) - 1
    if count >= 1:
        army_data.append({ "name": term, "count": count, "color": color })

army_data.sort(key=operator.itemgetter('count'), reverse=False)

# 2. Gerar HTML com NO-CACHE META TAGS
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

    /* ESTILO GERAL */
    body {
        background: transparent;
        font-family: 'Rajdhani', sans-serif;
        margin: 0;
        padding: 5px 10px 5px 5px;
        overflow-x: hidden;
        overflow-y: auto;
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
print("army_code.html updated with NO-CACHE tags.")
