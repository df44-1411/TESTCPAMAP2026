import json
import os
import re

# 1. PREPARAR PASTAS
if not os.path.exists('data'):
    os.makedirs('data')
    print("✅ Pasta 'data/' criada.")

# 2. MIGRAR EXÉRCITOS (de army_code.py para armies.json)
print("🔄 A migrar exércitos...")
try:
    with open('/workspaces/CPAMap2026_Testing/army_code.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extrair o dicionário search_terms usando Regex
    match = re.search(r'search_terms\s*=\s*({[^}]+})', content, re.DOTALL)
    if match:
        # Converter string python dictionary para json valid string (aspas simples para duplas se necessário)
        dict_str = match.group(1)
        # Executar como código python para obter o dict real com segurança
        search_terms = eval(dict_str)
        
        armies_data = {}
        for name, color in search_terms.items():
            armies_data[name] = {
                "color": color,
                "wealth": 0, # Valor inicial
                "description": "No description available."
            }
            
        with open('data/armies.json', 'w', encoding='utf-8') as f:
            json.dump(armies_data, f, indent=2, ensure_ascii=False)
        print("✅ 'data/armies.json' gerado com sucesso.")
    else:
        print("⚠️ Não foi possível encontrar 'search_terms' em army_code.py")

except Exception as e:
    print(f"❌ Erro ao migrar exércitos: {e}")

# 3. MIGRAR SERVIDORES (de map.js para servers.json)
print("🔄 A migrar servidores do mapa...")
try:
    with open('/workspaces/CPAMap2026_Testing/map.js', 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Extrair mapData. Procura por "var mapData = [" até o "];"
    # Esta regex é robusta para capturar o array de objetos JSON
    match = re.search(r'var mapData\s*=\s*(\[.*?\]);', js_content, re.DOTALL)
    
    if match:
        json_str = match.group(1)
        # O Javascript pode ter vírgulas soltas ou chaves sem aspas, mas o teu ficheiro parece JSON válido.
        # Vamos tentar carregar diretamente.
        try:
            servers_data = json.loads(json_str)
            
            with open('data/servers.json', 'w', encoding='utf-8') as f:
                json.dump(servers_data, f, indent=2, ensure_ascii=False)
            print("✅ 'data/servers.json' gerado com sucesso.")
            
        except json.JSONDecodeError as je:
            print(f"⚠️ O conteúdo de mapData não é um JSON puro (verifique vírgulas finais): {je}")
            # Fallback: Tenta limpar vírgulas trailling se existirem
            json_str_clean = re.sub(r',\s*([\]}])', r'\1', json_str)
            servers_data = json.loads(json_str_clean)
            with open('data/servers.json', 'w', encoding='utf-8') as f:
                json.dump(servers_data, f, indent=2, ensure_ascii=False)
            print("✅ 'data/servers.json' gerado com sucesso (após limpeza).")
            
    else:
        print("⚠️ Não foi possível encontrar 'var mapData' em map.js")

except Exception as e:
    print(f"❌ Erro ao migrar servidores: {e}")

print("\n--- FIM DO PASSO 1 ---")
print("Verifica se tens a pasta 'data' com 'armies.json' e 'servers.json' dentro.")
