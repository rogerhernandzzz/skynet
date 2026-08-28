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

# ===== CSS RADIAL MENU (SIN ANIMACIONES) =====
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

/* ===== RADIAL MENU CONTAINER ===== */
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

/* ===== RADIAL MENU ITEMS ===== */
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

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .center-logo {
        font-size: 2rem;
    }

    .center-circle {
        width: 100px;
        height: 100px;
    }

    .menu-item {
        --radius: 180px;
        width: 70px;
        height: 70px;
    }

    .item-icon {
        font-size: 1.8rem;
    }

    .item-label {
        font-size: 0.7rem;
    }
}

/* ===== HUD TEXT ===== */
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
"""

# ===== HOME PAGE (RADIAL MENU) =====
@app.get("/", response_class=HTMLResponse)
def get_home():
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
        <title>Skynet - La Resistencia</title>
        <style>{CSS_RADIAL}</style>
    </head>
    <body>
        <div class="hud-text">
            SKYNET v<span>1.0</span> | ONLINE
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
                <a href="/registro" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">📝</span>
                    <span class="item-label">Registro</span>
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
                <a href="https://t.me/rogerhernandzzz" class="menu-item">
                    <div class="item-circle"></div>
                    <span class="item-icon">📱</span>
                    <span class="item-label">Contacto</span>
                </a>
            </nav>
        </div>
    </body>
    </html>
    """

# ===== REGISTRO PAGE =====
@app.get("/registro", response_class=HTMLResponse)
def get_registro():
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skynet - Registro</title>
        <style>
            {CSS_RADIAL}

            .registro-wrapper {{
                position: fixed;
                inset: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 1000;
            }}

            .registro-card {{
                background: rgba(255, 255, 255, 0.02);
                border: 2px solid var(--white-30);
                padding: 3rem;
                max-width: 450px;
                width: 90%;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 40px rgba(255, 0, 0, 0.2);
            }}

            .registro-card h1 {{
                font-family: 'Space Mono', monospace;
                font-size: 1.75rem;
                text-align: center;
                margin-bottom: 1rem;
                letter-spacing: 2px;
            }}

            .registro-subtitle {{
                text-align: center;
                color: var(--white-60);
                margin-bottom: 2rem;
                font-size: 0.9rem;
            }}

            .form-group {{
                margin-bottom: 1.5rem;
            }}

            .form-group label {{
                display: block;
                margin-bottom: 0.5rem;
                font-weight: 500;
                font-size: 0.875rem;
                letter-spacing: 0.5px;
            }}

            .form-group input {{
                width: 100%;
                padding: 0.75rem;
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid var(--white-30);
                color: var(--white-100);
                font-size: 0.9rem;
                transition: all 0.3s ease;
            }}

            .form-group input:focus {{
                outline: none;
                border-color: var(--accent-red);
                background: rgba(255, 255, 255, 0.05);
                box-shadow: 0 0 20px rgba(255, 0, 0, 0.2);
            }}

            .submit-btn {{
                width: 100%;
                padding: 0.875rem;
                background: var(--white-100);
                color: var(--black);
                border: 1px solid var(--white-100);
                font-weight: 600;
                font-size: 0.875rem;
                letter-spacing: 1px;
                cursor: pointer;
                transition: all 0.3s ease;
                text-transform: uppercase;
            }}

            .submit-btn:hover {{
                background: var(--accent-red);
                border-color: var(--accent-red);
                color: var(--white-100);
            }}

            .back-link {{
                text-align: center;
                margin-top: 1.5rem;
            }}

            .back-link a {{
                color: var(--white-60);
                text-decoration: none;
                font-size: 0.875rem;
            }}

            .back-link a:hover {{
                color: var(--accent-red);
            }}
        </style>
    </head>
    <body>
        <div class="registro-wrapper">
            <div class="registro-card">
                <h1>🚀 SKYNET</h1>
                <p class="registro-subtitle">Únete a la Resistencia</p>

                <form onsubmit="return handleSubmit(event)">
                    <div class="form-group">
                        <label for="username">Usuario</label>
                        <input type="text" id="username" placeholder="Tu usuario" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" placeholder="tu@email.com" required>
                    </div>
                    <div class="form-group">
                        <label for="cedula">Cédula</label>
                        <input type="text" id="cedula" placeholder="V-12345678" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Contraseña</label>
                        <input type="password" id="password" placeholder="Min. 8 caracteres" required>
                    </div>
                    <button type="submit" class="submit-btn">Registrarse</button>
                </form>

                <div class="back-link">
                    <a href="/">← Volver</a>
                </div>
            </div>
        </div>

        <script>
            function handleSubmit(event) {{
                event.preventDefault();
                alert('✅ Bienvenido a la Resistencia');
                window.location.href = '/';
                return false;
            }}
        </script>
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
