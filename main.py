from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Skynet API",
    description="La API de la Resistencia Venezolana",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "service": "Skynet API",
        "version": "1.0.0"
    }

# ===== CSS RADIAL MENU (8 ITEMS) =====
CSS_RADIAL = """
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;500;600;700;800&display=swap');

:root {
    --black: #000000;
    --white-100: #f0f0fa;
    --white-80: rgba(240, 240, 250, 0.8);
    --white-60: rgba(240, 240, 250, 0.6);
    --white-30: rgba(240, 240, 250, 0.3);
    --accent-red: #ff0000;
    --accent-cyan: #00ffff;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    width: 100%;
    height: 100%;
}

body {
    font-family: 'Syne', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: radial-gradient(circle at center, #0a0a1a 0%, #000000 50%, #000000 100%);
    color: var(--white-100);
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.radial-menu-wrapper {
    position: relative;
    width: 100vmin;
    height: 100vmin;
    max-width: 100vh;
    max-height: 100vh;
}

.radial-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 10;
    text-align: center;
}

.center-logo {
    font-family: 'Space Mono', monospace;
    font-size: clamp(2rem, 8vmin, 4rem);
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 1rem;
    text-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
}

.center-subtitle {
    font-size: clamp(0.8rem, 2vmin, 1.2rem);
    color: var(--white-60);
    letter-spacing: 2px;
    text-transform: uppercase;
}

.center-circle {
    position: absolute;
    width: clamp(80px, 15vmin, 200px);
    height: clamp(80px, 15vmin, 200px);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: 2px solid var(--white-30);
    border-radius: 50%;
    z-index: 5;
}

.center-circle::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255, 0, 0, 0.1) 0%, transparent 70%);
}

.radial-menu {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
}

.menu-item {
    position: absolute;
    width: clamp(60px, 12vmin, 140px);
    height: clamp(60px, 12vmin, 140px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    color: var(--white-100);
}

.menu-item:nth-child(1) { --angle: 0deg; }
.menu-item:nth-child(2) { --angle: 45deg; }
.menu-item:nth-child(3) { --angle: 90deg; }
.menu-item:nth-child(4) { --angle: 135deg; }
.menu-item:nth-child(5) { --angle: 180deg; }
.menu-item:nth-child(6) { --angle: 225deg; }
.menu-item:nth-child(7) { --angle: 270deg; }
.menu-item:nth-child(8) { --angle: 315deg; }

.menu-item {
    --radius: clamp(120px, 35vmin, 400px);
    top: 50%;
    left: 50%;
    transform:
        translate(-50%, -50%)
        rotate(var(--angle))
        translateY(calc(var(--radius) * -1))
        rotate(calc(var(--angle) * -1));
}

.item-icon {
    font-size: clamp(1.5rem, 4vmin, 3rem);
    margin-bottom: 0.5rem;
    display: block;
    filter: drop-shadow(0 0 8px rgba(255, 0, 0, 0.3));
    transition: all 0.3s ease;
}

.item-label {
    font-family: 'Space Mono', monospace;
    font-size: clamp(0.6rem, 1.5vmin, 0.9rem);
    letter-spacing: 1px;
    text-transform: uppercase;
    white-space: nowrap;
    transition: all 0.3s ease;
}

.item-circle {
    position: absolute;
    inset: 0;
    border: 2px solid var(--white-30);
    border-radius: 50%;
    z-index: -1;
    transition: all 0.3s ease;
}

.menu-item:hover .item-circle {
    border-color: var(--accent-red);
    box-shadow:
        0 0 15px rgba(255, 0, 0, 0.5),
        inset 0 0 15px rgba(255, 0, 0, 0.2);
    transform: scale(1.1);
}

.menu-item:hover {
    transform:
        translate(-50%, -50%)
        rotate(var(--angle))
        translateY(calc(var(--radius) * -1))
        rotate(calc(var(--angle) * -1))
        scale(1.15);
    z-index: 100;
}

.menu-item:hover .item-label {
    color: var(--accent-red);
    text-shadow: 0 0 10px rgba(255, 0, 0, 0.6);
}

.menu-item:hover .item-icon {
    filter: drop-shadow(0 0 20px rgba(255, 0, 0, 0.8));
    transform: scale(1.2);
}

@media (max-width: 768px) {
    .center-logo { font-size: 2rem; }
    .center-circle { width: 100px; height: 100px; }
    .menu-item { --radius: 180px; width: 70px; height: 70px; }
    .item-icon { font-size: 1.8rem; }
    .item-label { font-size: 0.7rem; }
}

.hud-text {
    position: fixed;
    top: 20px;
    left: 20px;
    font-family: 'Space Mono', monospace;
    font-size: 0.875rem;
    letter-spacing: 2px;
    color: var(--white-60);
    z-index: 1;
}

.hud-text span {
    color: var(--accent-red);
}

/* ===== AUTH PANEL (TOP RIGHT) ===== */
.auth-panel {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 100;
    display: flex;
    align-items: center;
    gap: 1rem;
    font-family: 'Space Mono', monospace;
}

.auth-button {
    background: transparent;
    border: 1px solid var(--white-30);
    color: var(--white-100);
    padding: 0.5rem 1rem;
    cursor: pointer;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 1px;
    text-decoration: none;
    transition: all 0.3s ease;
    text-transform: uppercase;
    display: inline-block;
}

.auth-button:hover {
    border-color: var(--accent-red);
    color: var(--accent-red);
}

.user-display {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.5rem 1rem;
    border: 1px solid var(--white-30);
    border-radius: 4px;
    color: var(--accent-red);
}

.user-alias {
    font-size: 0.875rem;
    letter-spacing: 1px;
}

.logout-btn {
    background: transparent;
    border: none;
    color: var(--white-60);
    cursor: pointer;
    font-size: 1rem;
    transition: color 0.3s ease;
}

.logout-btn:hover {
    color: var(--accent-red);
}

/* ===== MODALS ===== */
.modal {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.8);
    z-index: 1000;
    align-items: center;
    justify-content: center;
}

.modal.active {
    display: flex;
}

.modal-card {
    background: rgba(255, 255, 255, 0.02);
    border: 2px solid var(--white-30);
    padding: 2rem;
    max-width: 400px;
    width: 90%;
    backdrop-filter: blur(10px);
    border-radius: 8px;
}

.modal-title {
    font-family: 'Space Mono', monospace;
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    text-align: center;
    letter-spacing: 1px;
}

.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 0.875rem;
    letter-spacing: 0.5px;
}

.form-group input {
    width: 100%;
    padding: 0.75rem;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--white-30);
    color: var(--white-100);
    font-size: 0.9rem;
    transition: all 0.3s ease;
}

.form-group input:focus {
    outline: none;
    border-color: var(--accent-red);
    background: rgba(255, 255, 255, 0.05);
}

.submit-btn {
    width: 100%;
    padding: 0.75rem;
    background: var(--white-100);
    color: var(--black);
    border: 1px solid var(--white-100);
    font-weight: 600;
    font-size: 0.875rem;
    letter-spacing: 1px;
    cursor: pointer;
    text-transform: uppercase;
    transition: all 0.3s ease;
    margin-top: 1rem;
}

.submit-btn:hover {
    background: var(--accent-red);
    border-color: var(--accent-red);
    color: var(--white-100);
}

.close-modal {
    position: absolute;
    top: 10px;
    right: 10px;
    background: transparent;
    border: none;
    color: var(--white-60);
    font-size: 1.5rem;
    cursor: pointer;
    transition: color 0.3s ease;
}

.close-modal:hover {
    color: var(--accent-red);
}

/* ===== PAGE STYLES ===== */
.back-button {
    position: fixed;
    top: 20px;
    right: 20px;
    background: transparent;
    border: 1px solid var(--white-30);
    color: var(--white-100);
    padding: 0.5rem 1.5rem;
    cursor: pointer;
    font-family: 'Space Mono', monospace;
    text-decoration: none;
    transition: all 0.3s ease;
    z-index: 1;
}

.back-button:hover {
    border-color: var(--accent-red);
    color: var(--accent-red);
}

.page-container {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
}

.page-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--white-30);
    padding: 3rem;
    max-width: 600px;
    width: 100%;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 40px rgba(255, 0, 0, 0.1);
}

.page-title {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    margin-bottom: 1rem;
    letter-spacing: 2px;
}

.page-subtitle {
    color: var(--white-60);
    margin-bottom: 2rem;
    font-size: 1rem;
}

.profile-section {
    margin-bottom: 2rem;
}

.profile-name {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.profile-title {
    color: var(--accent-red);
    font-size: 0.9rem;
    margin-bottom: 1rem;
    letter-spacing: 1px;
}

.profile-bio {
    color: var(--white-80);
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

.social-links {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.social-link {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    border: 1px solid var(--white-15);
    border-radius: 4px;
    color: var(--white-100);
    text-decoration: none;
    transition: all 0.3s ease;
    font-size: 0.875rem;
}

.social-link:hover {
    border-color: var(--accent-red);
    background: rgba(255, 0, 0, 0.05);
    color: var(--accent-red);
}

.ai-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.ai-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--white-15);
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    transition: all 0.3s ease;
}

.ai-card:hover {
    border-color: var(--accent-red);
    background: rgba(255, 0, 0, 0.05);
}

.ai-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.ai-name {
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.ai-desc {
    color: var(--white-60);
    font-size: 0.875rem;
}
"""

# ===== HOME PAGE =====
@app.get("/", response_class=HTMLResponse)
def get_home():
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skynet - La Resistencia</title>
        <style>{CSS_RADIAL}</style>
    </head>
    <body>
        <div class="hud-text">SKYNET v<span>1.0</span> | ONLINE</div>

        <div class="auth-panel" id="authPanel">
            <button class="auth-button" onclick="openRegistro()">Registro</button>
            <button class="auth-button" onclick="openIngresar()">Ingresar</button>
        </div>

        <!-- MODALS -->
        <div class="modal" id="registroModal">
            <div class="modal-card">
                <button class="close-modal" onclick="closeRegistro()">✕</button>
                <div class="modal-title">🚀 REGISTRO</div>
                <form onsubmit="return handleRegistro(event)">
                    <div class="form-group">
                        <label>Usuario</label>
                        <input type="text" id="regUsername" placeholder="Tu usuario" required>
                    </div>
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" id="regEmail" placeholder="tu@email.com" required>
                    </div>
                    <div class="form-group">
                        <label>Cédula</label>
                        <input type="text" id="regCedula" placeholder="V-12345678" required>
                    </div>
                    <div class="form-group">
                        <label>Contraseña</label>
                        <input type="password" id="regPassword" placeholder="Min. 8 caracteres" required>
                    </div>
                    <button type="submit" class="submit-btn">Registrarse</button>
                </form>
            </div>
        </div>

        <div class="modal" id="ingresarModal">
            <div class="modal-card">
                <button class="close-modal" onclick="closeIngresar()">✕</button>
                <div class="modal-title">⚡ INGRESAR</div>
                <form onsubmit="return handleIngresar(event)">
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" id="ingEmail" placeholder="tu@email.com" required>
                    </div>
                    <div class="form-group">
                        <label>Contraseña</label>
                        <input type="password" id="ingPassword" placeholder="Tu contraseña" required>
                    </div>
                    <button type="submit" class="submit-btn">Ingresar</button>
                </form>
            </div>
        </div>

        <div class="radial-menu-wrapper">
            <div class="center-circle"></div>
            <div class="radial-center">
                <div class="center-logo">🚀 SKYNET</div>
                <div class="center-subtitle">La Resistencia</div>
            </div>

            <nav class="radial-menu">
                <a href="#resistencia" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">🔒</span>
                    <span class="item-label">Resistencia</span>
                </a>
                <a href="#donaciones" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">💳</span>
                    <span class="item-label">Donar</span>
                </a>
                <a href="#luz" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">₿</span>
                    <span class="item-label">Cripto LUZ</span>
                </a>
                <a href="#foro" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">💬</span>
                    <span class="item-label">Comunidad</span>
                </a>
                <a href="#noticias" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">📡</span>
                    <span class="item-label">Noticias</span>
                </a>
                <a href="#trader" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">📈</span>
                    <span class="item-label">Trader</span>
                </a>
                <a href="/perfil" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">🤖</span>
                    <span class="item-label">Yo Cibernético</span>
                </a>
                <a href="/ia" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">⚡</span>
                    <span class="item-label">IA</span>
                </a>
            </nav>
        </div>

        <script>
            function updateAuthPanel() {{
                const username = localStorage.getItem('username');
                const authPanel = document.getElementById('authPanel');

                if (username) {{
                    authPanel.innerHTML = `
                        <div class="user-display">
                            <span class="user-alias">\${{username}}</span>
                            <button class="logout-btn" onclick="logout()">✕</button>
                        </div>
                    `;
                }} else {{
                    authPanel.innerHTML = `
                        <button class="auth-button" onclick="openRegistro()">Registro</button>
                        <button class="auth-button" onclick="openIngresar()">Ingresar</button>
                    `;
                }}
            }}

            function openRegistro() {{
                document.getElementById('registroModal').classList.add('active');
            }}

            function closeRegistro() {{
                document.getElementById('registroModal').classList.remove('active');
            }}

            function openIngresar() {{
                document.getElementById('ingresarModal').classList.add('active');
            }}

            function closeIngresar() {{
                document.getElementById('ingresarModal').classList.remove('active');
            }}

            function handleRegistro(event) {{
                event.preventDefault();
                const username = document.getElementById('regUsername').value;
                localStorage.setItem('username', username);
                alert('✅ Bienvenido: ' + username);
                closeRegistro();
                updateAuthPanel();
                return false;
            }}

            function handleIngresar(event) {{
                event.preventDefault();
                const email = document.getElementById('ingEmail').value;
                localStorage.setItem('username', email.split('@')[0]);
                alert('✅ Ingreso exitoso');
                closeIngresar();
                updateAuthPanel();
                return false;
            }}

            function logout() {{
                localStorage.removeItem('username');
                updateAuthPanel();
            }}

            updateAuthPanel();

            document.addEventListener('click', (e) => {{
                if (e.target.id === 'registroModal') closeRegistro();
                if (e.target.id === 'ingresarModal') closeIngresar();
            }});
        </script>
    </body>
    </html>
    """

# ===== PERFIL PAGE =====
@app.get("/perfil", response_class=HTMLResponse)
def get_perfil():
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Roger Hernández - Yo Cibernético</title>
        <style>{CSS_RADIAL}</style>
    </head>
    <body>
        <a href="/" class="back-button">← VOLVER</a>

        <div class="page-container">
            <div class="page-card">
                <div class="profile-section">
                    <div style="text-align: center; font-size: 4rem; margin-bottom: 1rem;">🤖</div>
                    <div class="profile-name">Roger Hernández</div>
                    <div class="profile-title">Cibernético | Fundador de Skynet</div>
                </div>

                <div class="profile-bio">
                    Ingeniero de sistemas y activista político dedicado a la liberación digital de Venezuela.
                    Fundador de Skynet, una plataforma descentralizada para coordinar la resistencia.
                    Especialista en seguridad, blockchain y automatización.
                </div>

                <div class="profile-section">
                    <h3 style="margin-bottom: 1rem; letter-spacing: 1px;">CONTACTO Y REDES</h3>
                    <div class="social-links">
                        <a href="https://t.me/rogerhernandzzz" target="_blank" class="social-link">
                            <span>📱</span> Telegram: @rogerhernandzzz
                        </a>
                        <a href="https://github.com/rogerhernandzzz" target="_blank" class="social-link">
                            <span>💻</span> GitHub: rogerhernandzzz
                        </a>
                        <a href="mailto:contact@skynet.com" class="social-link">
                            <span>📧</span> Email: contact@skynet.com
                        </a>
                        <a href="https://twitter.com/rogerhernandzzz" target="_blank" class="social-link">
                            <span>𝕏</span> Twitter: @rogerhernandzzz
                        </a>
                    </div>
                </div>

                <div class="profile-section">
                    <h3 style="margin-bottom: 1rem; letter-spacing: 1px;">ESPECIALIDADES</h3>
                    <div style="color: var(--white-80); display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; font-size: 0.9rem;">
                        <div>• Seguridad Cibernética</div>
                        <div>• Blockchain</div>
                        <div>• Automatización</div>
                        <div>• IA & Bots</div>
                        <div>• FastAPI</div>
                        <div>• DevOps</div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

# ===== IA PAGE =====
@app.get("/ia", response_class=HTMLResponse)
def get_ia():
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inteligencia Artificial - Skynet</title>
        <style>{CSS_RADIAL}</style>
    </head>
    <body>
        <a href="/" class="back-button">← VOLVER</a>

        <div class="page-container">
            <div class="page-card">
                <div class="page-title">⚡ INTELIGENCIA ARTIFICIAL</div>
                <div class="page-subtitle">Agentes y Sistemas Autónomos 24/7</div>

                <div class="ai-grid">
                    <div class="ai-card">
                        <div class="ai-icon">🤖</div>
                        <div class="ai-name">Marketing Agent</div>
                        <div class="ai-desc">Monitor de campañas, análisis de métricas, optimización automática</div>
                    </div>
                    <div class="ai-card">
                        <div class="ai-icon">📊</div>
                        <div class="ai-name">Analytics Agent</div>
                        <div class="ai-desc">Análisis de datos en tiempo real, reportes automáticos</div>
                    </div>
                    <div class="ai-card">
                        <div class="ai-icon">📱</div>
                        <div class="ai-name">Social Agent</div>
                        <div class="ai-desc">Publicación automática, gestión de comunidad, engagement</div>
                    </div>
                    <div class="ai-card">
                        <div class="ai-icon">🔐</div>
                        <div class="ai-name">Security Agent</div>
                        <div class="ai-desc">Monitoreo de seguridad, detección de anomalías, alertas</div>
                    </div>
                    <div class="ai-card">
                        <div class="ai-icon">⚙️</div>
                        <div class="ai-name">Automation Agent</div>
                        <div class="ai-desc">Tareas repetitivas, flujos automáticos, optimización</div>
                    </div>
                    <div class="ai-card">
                        <div class="ai-icon">🧠</div>
                        <div class="ai-name">Claude Integration</div>
                        <div class="ai-desc">Procesamiento de lenguaje, análisis, decisiones inteligentes</div>
                    </div>
                </div>

                <div class="profile-section" style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--white-15);">
                    <h3 style="margin-bottom: 1rem;">ESTADO DE AGENTES</h3>
                    <div style="color: var(--white-80); font-size: 0.9rem; line-height: 2;">
                        <div>✅ 12 Agentes Operacionales 24/7</div>
                        <div>✅ 18 Tareas Celery Beat Automáticas</div>
                        <div>✅ Monitoreo Continuo</div>
                        <div>✅ Integración Claude Sonnet</div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

# ===== API ENDPOINTS =====
@app.post("/api/auth/register")
def register(username: str, email: str, password: str, cedula: str):
    return {"success": True, "message": "Registro completado"}

@app.post("/api/auth/login")
def login(email: str, password: str):
    return {"success": True, "token": "jwt_token"}

@app.get("/api/news")
def get_news():
    return {"news": [{"id": 1, "title": "Skynet está LIVE"}]}

@app.get("/api/donations/stats")
def get_donation_stats():
    return {"total_donations": 0, "total_amount": 0}

@app.get("/api/crypto/luz")
def get_luz_info():
    return {"name": "Luz", "symbol": "LUZ", "total_supply": 20000000, "current_price": 0.10}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
