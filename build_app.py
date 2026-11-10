import os
import json

def build_app():
    with open("podcast/screens_manifest.json", "r", encoding="utf-8") as f:
        screens = json.load(f)

    # Categories
    categorized = {
        "onboarding": [],
        "auth": [],
        "home": [],
        "player": [],
        "live": [],
        "recording": [],
        "profile": [],
        "all": screens
    }

    for s in screens:
        name_lower = s["name"].lower()
        if "onboarding" in name_lower or "welcome" in name_lower or s["nodeId"] in ["1:4812", "1:4081"]:
            categorized["onboarding"].append(s)
        elif "sign in" in name_lower or "otp" in name_lower or "input form" in name_lower or "password" in name_lower or "success" in name_lower or "complete profile" in name_lower:
            categorized["auth"].append(s)
        elif "home" in name_lower or "discover" in name_lower or "search" in name_lower or "favorite" in name_lower:
            categorized["home"].append(s)
        elif "play" in name_lower or "detail" in name_lower or "notification" in name_lower or s["nodeId"] in ["1:4206"]:
            categorized["player"].append(s)
        elif "live" in name_lower:
            categorized["live"].append(s)
        elif "record" in name_lower or "group recording" in name_lower:
            categorized["recording"].append(s)
        elif "setting" in name_lower or "profile" in name_lower or "visibility" in name_lower:
            categorized["profile"].append(s)
        else:
            categorized["home"].append(s)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>Podcast Pro - Complete Figma Experience</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="manifest" href="manifest.webmanifest">
  <style>
    :root {{
      --primary: #10B981;
      --bg: #090D16;
    }}
    * {{
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: #F8FAFC;
      user-select: none;
      -webkit-user-select: none;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 5px;
      height: 5px;
    }}
    .custom-scrollbar::-webkit-scrollbar-track {{
      background: #0B0F19;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #1E293B;
      border-radius: 9999px;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
      background: #334155;
    }}
    .phone-mockup {{
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7), 0 0 0 12px #1E293B, 0 0 0 14px #334155;
    }}
    @media (max-width: 640px) {{
      .phone-mockup {{
        box-shadow: none;
        border-radius: 0 !important;
        border: none !important;
      }}
    }}
  </style>
</head>
<body class="h-screen w-screen overflow-hidden flex flex-col bg-[#070A12]">

  <!-- Top App Navigation Bar -->
  <header class="h-16 flex-none bg-[#0B0F1D]/90 backdrop-blur-md border-b border-slate-800/80 px-4 md:px-8 flex items-center justify-between z-50">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-emerald-500/20 text-xl font-bold text-white">
        🎙️
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="font-bold text-sm md:text-base text-white tracking-tight">Podcast App</h1>
          <span class="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">64 Telas Ativas</span>
        </div>
        <p class="text-xs text-slate-400 hidden sm:block">Figma Design System 100% Interativo</p>
      </div>
    </div>

    <!-- Center Flow Navigator -->
    <div class="hidden lg:flex items-center gap-1 bg-slate-900/80 p-1 rounded-xl border border-slate-800 text-xs">
      <button onclick="setFlow('all')" id="tab-all" class="flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all">Todas</button>
      <button onclick="setFlow('onboarding')" id="tab-onboarding" class="flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all">Onboarding</button>
      <button onclick="setFlow('auth')" id="tab-auth" class="flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all">Login / Auth</button>
      <button onclick="setFlow('home')" id="tab-home" class="flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all">Home & Feed</button>
      <button onclick="setFlow('player')" id="tab-player" class="flow-btn px-3 py-1.5 rounded-lg bg-emerald-600 text-white font-medium transition-all">Player & Detalhes</button>
      <button onclick="setFlow('live')" id="tab-live" class="flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all">Ao Vivo (Live)</button>
      <button onclick="setFlow('recording')" id="tab-recording" class="flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all">Gravação</button>
      <button onclick="setFlow('profile')" id="tab-profile" class="flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all">Ajustes</button>
    </div>

    <!-- Quick Actions -->
    <div class="flex items-center gap-2">
      <button onclick="toggleDeviceMode()" id="btn-device-mode" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium flex items-center gap-1.5 transition-colors">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
        <span class="hidden sm:inline">Moldura Mobile</span>
      </button>

      <button onclick="openCurrentFullscreen()" class="p-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-medium transition-colors" title="Tela Cheia">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
      </button>
    </div>
  </header>

  <!-- Interactive Workspace -->
  <div class="flex-1 flex overflow-hidden">
    <!-- Left Drawer / Navigation -->
    <aside class="w-72 md:w-80 flex-none bg-[#090D18] border-r border-slate-800/80 flex flex-col h-full z-20">
      <!-- Search & Flow Filter -->
      <div class="p-3 border-b border-slate-800 space-y-2">
        <div class="relative">
          <input 
            id="search-input"
            type="text" 
            placeholder="Filtrar 64 designs..." 
            class="w-full bg-slate-900/90 border border-slate-700/80 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 pl-8 transition-colors"
          />
          <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>
      </div>

      <!-- Screen List -->
      <div id="screen-list" class="flex-1 overflow-y-auto custom-scrollbar p-2 space-y-1">
        <!-- Rendered via JS -->
      </div>

      <!-- Quick Switcher Footer -->
      <div class="p-3 border-t border-slate-800 bg-[#070A14] flex items-center justify-between text-xs text-slate-400">
        <span id="screen-counter-badge">1 de 64</span>
        <div class="flex items-center gap-1">
          <button onclick="prevScreen()" class="p-1 rounded hover:bg-slate-800 text-slate-300">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
          </button>
          <button onclick="nextScreen()" class="p-1 rounded hover:bg-slate-800 text-slate-300">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>
    </aside>

    <!-- Center Stage / Active App View -->
    <main class="flex-1 bg-[#05070E] flex flex-col items-center justify-center p-2 sm:p-6 overflow-hidden relative">
      <!-- Header Info of current screen -->
      <div class="absolute top-4 left-6 right-6 flex items-center justify-between pointer-events-none z-10">
        <div class="bg-slate-900/80 backdrop-blur-md px-3.5 py-1.5 rounded-full border border-slate-800 text-xs text-slate-300 pointer-events-auto flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span id="active-screen-name" class="font-semibold text-white">Carregando...</span>
          <span id="active-screen-node" class="text-slate-500 font-mono">1:4295</span>
        </div>

        <div class="flex items-center gap-2 pointer-events-auto">
          <!-- Flow shortcuts -->
          <button onclick="goToScreenByNode('1:4295')" class="text-[11px] bg-slate-900/80 hover:bg-slate-800 border border-slate-800 px-2.5 py-1 rounded-lg text-slate-300 transition-colors">Home</button>
          <button onclick="goToScreenByNode('1:4206')" class="text-[11px] bg-slate-900/80 hover:bg-slate-800 border border-slate-800 px-2.5 py-1 rounded-lg text-slate-300 transition-colors">Player</button>
          <button onclick="goToScreenByNode('1:5450')" class="text-[11px] bg-slate-900/80 hover:bg-slate-800 border border-slate-800 px-2.5 py-1 rounded-lg text-slate-300 transition-colors">Live</button>
          <button onclick="goToScreenByNode('134:10340')" class="text-[11px] bg-slate-900/80 hover:bg-slate-800 border border-slate-800 px-2.5 py-1 rounded-lg text-slate-300 transition-colors">Ajustes</button>
        </div>
      </div>

      <!-- Phone Frame Container -->
      <div id="phone-wrapper" class="relative w-[375px] h-[812px] max-h-full rounded-[44px] overflow-hidden phone-mockup bg-white flex flex-col transition-all duration-300">
        <!-- Dynamic Island / Speaker notch placeholder -->
        <div class="absolute top-0 left-0 right-0 h-10 flex items-center justify-center pointer-events-none z-30">
          <div class="w-24 h-4 bg-black/80 rounded-full mt-2"></div>
        </div>

        <!-- The Live Screen Iframe -->
        <iframe id="main-app-frame" src="screens/1_4295.html" class="w-full h-full border-0 select-auto"></iframe>
      </div>
    </main>
  </div>

  <script>
    const ALL_SCREENS = {json.dumps(screens, ensure_ascii=False)};
    const CATEGORIES = {json.dumps(categorized, ensure_ascii=False)};

    let currentFlow = 'home';
    let currentScreens = CATEGORIES[currentFlow] || ALL_SCREENS;
    let activeScreenIndex = 0;
    let isMockupActive = true;

    function init() {{
      renderScreensList();
      if (currentScreens.length > 0) {{
        loadScreen(0);
      }}
      setupSearch();
    }}

    function setFlow(flow) {{
      currentFlow = flow;
      document.querySelectorAll('.flow-btn').forEach(b => {{
        b.className = 'flow-btn px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all';
      }});
      const activeTab = document.getElementById('tab-' + flow);
      if (activeTab) {{
        activeTab.className = 'flow-btn px-3 py-1.5 rounded-lg bg-emerald-600 text-white font-medium transition-all';
      }}

      currentScreens = (flow === 'all') ? ALL_SCREENS : (CATEGORIES[flow] || ALL_SCREENS);
      activeScreenIndex = 0;
      renderScreensList();
      if (currentScreens.length > 0) {{
        loadScreen(0);
      }}
    }}

    function renderScreensList(filtered = null) {{
      const list = document.getElementById('screen-list');
      const data = filtered || currentScreens;

      list.innerHTML = data.map((s, idx) => {{
        const isSelected = (!filtered && idx === activeScreenIndex);
        return `
          <button onclick="onScreenSelected(${{idx}}, ${{filtered ? 'true' : 'false'}})" class="w-full text-left px-3 py-2.5 rounded-xl text-xs transition-all flex items-center justify-between group ${{isSelected ? 'bg-emerald-600/20 text-emerald-300 border border-emerald-500/40' : 'text-slate-400 hover:bg-slate-800/60 hover:text-slate-200'}}">
            <div class="truncate pr-2">
              <span class="font-medium text-slate-200 block truncate">${{s.name}}</span>
              <span class="text-[10px] text-slate-500 font-mono">${{s.nodeId}}</span>
            </div>
            <span class="text-[10px] font-mono text-slate-600 group-hover:text-emerald-400">${{idx + 1}}</span>
          </button>
        `;
      }}).join('');

      document.getElementById('screen-counter-badge').textContent = `${{activeScreenIndex + 1}} de ${{currentScreens.length}}`;
    }}

    function onScreenSelected(idx, isFiltered) {{
      if (isFiltered) {{
        const inputVal = document.getElementById('search-input').value.toLowerCase();
        const filtered = ALL_SCREENS.filter(s => s.name.toLowerCase().includes(inputVal) || s.nodeId.toLowerCase().includes(inputVal));
        const s = filtered[idx];
        const globalIdx = currentScreens.findIndex(item => item.nodeId === s.nodeId);
        if (globalIdx !== -1) {{
          activeScreenIndex = globalIdx;
        }} else {{
          currentScreens = ALL_SCREENS;
          activeScreenIndex = ALL_SCREENS.findIndex(item => item.nodeId === s.nodeId);
        }}
      }} else {{
        activeScreenIndex = idx;
      }}
      renderScreensList();
      loadScreen(activeScreenIndex);
    }}

    function loadScreen(idx) {{
      const s = currentScreens[idx];
      if (!s) return;
      document.getElementById('active-screen-name').textContent = s.name;
      document.getElementById('active-screen-node').textContent = s.nodeId;
      document.getElementById('main-app-frame').src = s.screenFile;
      document.getElementById('screen-counter-badge').textContent = `${{idx + 1}} de ${{currentScreens.length}}`;
    }}

    function goToScreenByNode(nid) {{
      const idx = currentScreens.findIndex(s => s.nodeId === nid);
      if (idx !== -1) {{
        activeScreenIndex = idx;
        renderScreensList();
        loadScreen(idx);
      }} else {{
        setFlow('all');
        setTimeout(() => {{
          const allIdx = ALL_SCREENS.findIndex(s => s.nodeId === nid);
          if (allIdx !== -1) {{
            activeScreenIndex = allIdx;
            renderScreensList();
            loadScreen(allIdx);
          }}
        }}, 50);
      }}
    }}

    function prevScreen() {{
      if (activeScreenIndex > 0) {{
        activeScreenIndex--;
        renderScreensList();
        loadScreen(activeScreenIndex);
      }}
    }}

    function nextScreen() {{
      if (activeScreenIndex < currentScreens.length - 1) {{
        activeScreenIndex++;
        renderScreensList();
        loadScreen(activeScreenIndex);
      }}
    }}

    function toggleDeviceMode() {{
      isMockupActive = !isMockupActive;
      const wrapper = document.getElementById('phone-wrapper');
      if (isMockupActive) {{
        wrapper.className = "relative w-[375px] h-[812px] max-h-full rounded-[44px] overflow-hidden phone-mockup bg-white flex flex-col transition-all duration-300";
      }} else {{
        wrapper.className = "relative w-full h-full rounded-none overflow-hidden bg-white flex flex-col transition-all duration-300";
      }}
    }}

    function openCurrentFullscreen() {{
      const s = currentScreens[activeScreenIndex];
      if (s) {{
        window.open(s.screenFile, '_blank');
      }}
    }}

    function setupSearch() {{
      const inp = document.getElementById('search-input');
      inp.addEventListener('input', (e) => {{
        const q = e.target.value.toLowerCase().trim();
        if (!q) {{
          renderScreensList();
          return;
        }}
        const filtered = ALL_SCREENS.filter(s => s.name.toLowerCase().includes(q) || s.nodeId.toLowerCase().includes(q));
        renderScreensList(filtered);
      }});
    }}

    window.onload = init;
  </script>
</body>
</html>
"""

    with open("podcast/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("podcast/index.html updated successfully with realistic app layout!")

if __name__ == "__main__":
    build_app()
