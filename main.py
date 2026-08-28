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

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== HEALTH CHECK =====
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "service": "Skynet API",
        "version": "1.0.0"
    }

# ===== CSS INSPIRED BY SPACEX =====
CSS_SPACEX = """
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;500;600;700;800&display=swap');

:root {
    --black: #000000;
    --white-100: #f0f0fa;
    --white-90: rgba(240, 240, 250, 0.9);
    --white-80: rgba(240, 240, 250, 0.8);
    --white-60: rgba(240, 240, 250, 0.6);
    --white-30: rgba(240, 240, 250, 0.3);
    --white-15: rgba(240, 240, 250, 0.15);
    --gray-80: rgba(37, 38, 40, 0.8);
    --gray-60: rgba(37, 38, 40, 0.6);
    --accent: #ffffff;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Syne', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--black);
    color: var(--white-100);
    line-height: 1.6;
    overflow-x: hidden;
}

/* ===== NAVBAR ===== */
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--white-15);
    z-index: 1000;
    padding: 1.5rem 0;
}

.nav-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 3rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-family: 'Space Mono', monospace;
    font-size: 1.2rem;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--white-100);
    text-transform: uppercase;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 4rem;
    align-items: center;
}

.nav-menu a {
    color: var(--white-80);
    text-decoration: none;
    font-size: 0.875rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    transition: color 0.3s ease;
    font-family: 'Space Mono', monospace;
}

.nav-menu a:hover {
    color: var(--white-100);
}

.nav-menu a::after {
    content: '';
    display: block;
    width: 0;
    height: 1px;
    background: var(--white-100);
    transition: width 0.3s ease;
    margin-top: 4px;
}

.nav-menu a:hover::after {
    width: 100%;
}

/* ===== HERO SECTION ===== */
.hero {
    position: relative;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: space-between;
    overflow: hidden;
    margin-top: 60px;
    padding: 0 3rem;
    background: linear-gradient(135deg, #000000 0%, #0a0a0a 100%);
}

.hero-content {
    flex: 1;
    z-index: 2;
    max-width: 600px;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(3.5rem, 8vw, 5.5rem);
    font-weight: 800;
    letter-spacing: -2px;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    animation: slideInLeft 0.8s ease-out;
}

.hero-subtitle {
    font-size: clamp(1.1rem, 2vw, 1.5rem);
    color: var(--white-80);
    margin-bottom: 3rem;
    letter-spacing: 0.5px;
    animation: slideInLeft 0.8s ease-out 0.2s backwards;
    line-height: 1.6;
}

.hero-cta-group {
    display: flex;
    gap: 2rem;
    animation: slideInLeft 0.8s ease-out 0.4s backwards;
    flex-wrap: wrap;
}

.btn {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2.5rem;
    border: 1px solid var(--white-100);
    background: transparent;
    color: var(--white-100);
    text-decoration: none;
    font-size: 0.875rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-family: 'Space Mono', monospace;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 600;
}

.btn:hover {
    background: var(--white-100);
    color: var(--black);
    transform: translateY(-2px);
}

.btn-primary {
    background: var(--white-100);
    color: var(--black);
}

.btn-primary:hover {
    background: var(--white-80);
}

.hero-image {
    flex: 1;
    z-index: 1;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.hero-visual {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 8rem;
    animation: fadeInRight 0.8s ease-out;
}

.scroll-indicator {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    animation: bounce 2s infinite;
}

.scroll-indicator span {
    font-size: 0.75rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--white-60);
}

.scroll-arrow {
    width: 1px;
    height: 30px;
    background: var(--white-60);
}

/* ===== SECTION CONTAINER ===== */
section {
    padding: 6rem 3rem;
    position: relative;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
}

.section-header {
    text-align: center;
    margin-bottom: 5rem;
}

.section-header h2 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 1rem;
    animation: fadeInUp 0.8s ease-out;
}

.section-header p {
    font-size: 1.125rem;
    color: var(--white-80);
    letter-spacing: 0.5px;
    animation: fadeInUp 0.8s ease-out 0.1s backwards;
}

/* ===== RESISTENCIA SECTION ===== */
.resistencia {
    background: linear-gradient(180deg, #000000 0%, #0a0a0a 100%);
    border-top: 1px solid var(--white-15);
}

.resistencia-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2.5rem;
}

.resistencia-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--white-15);
    padding: 3rem 2rem;
    text-align: center;
    transition: all 0.3s ease;
    animation: fadeInUp 0.8s ease-out;
}

.resistencia-card:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: var(--white-100);
    transform: translateY(-5px);
}

.card-icon {
    font-size: 3.5rem;
    margin-bottom: 1.5rem;
    display: inline-block;
}

.resistencia-card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
    letter-spacing: 0.5px;
}

.resistencia-card p {
    color: var(--white-80);
    font-size: 0.95rem;
    line-height: 1.7;
}

/* ===== DONACIONES SECTION ===== */
.donaciones {
    background: linear-gradient(180deg, #0a0a0a 0%, #000000 100%);
    border-top: 1px solid var(--white-15);
}

.donaciones-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 2.5rem;
}

.donacion-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--white-15);
    padding: 2.5rem 2rem;
    text-align: center;
    transition: all 0.3s ease;
    animation: fadeInUp 0.8s ease-out;
}

.donacion-card:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: var(--white-100);
    transform: translateY(-5px);
}

.donacion-icon {
    font-size: 3rem;
    margin-bottom: 1.5rem;
}

.donacion-card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.donacion-card p {
    color: var(--white-80);
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
}

/* ===== LUZ SECTION ===== */
.luz-crypto {
    background: linear-gradient(180deg, #000000 0%, #0a0a0a 100%);
    border-top: 1px solid var(--white-15);
    border-bottom: 1px solid var(--white-15);
}

.luz-info {
    max-width: 900px;
    margin: 0 auto;
}

.luz-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.stat-box {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--white-15);
    padding: 2.5rem 2rem;
    text-align: center;
    transition: all 0.3s ease;
    animation: fadeInUp 0.8s ease-out;
}

.stat-box:hover {
    border-color: var(--white-100);
    background: rgba(255, 255, 255, 0.05);
}

.stat-number {
    display: block;
    font-family: 'Space Mono', monospace;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: var(--white-100);
}

.stat-label {
    display: block;
    font-size: 0.875rem;
    color: var(--white-80);
    letter-spacing: 1px;
    text-transform: uppercase;
}

.luz-description {
    text-align: center;
    margin: 3rem 0;
}

.luz-description p {
    color: var(--white-80);
    font-size: 1.0625rem;
    line-height: 1.8;
}

.luz-cta {
    display: flex;
    gap: 2rem;
    justify-content: center;
    flex-wrap: wrap;
}

/* ===== FOOTER ===== */
.footer {
    background: rgba(0, 0, 0, 0.8);
    border-top: 1px solid var(--white-15);
    padding: 4rem 3rem 2rem;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 3rem;
    max-width: 1400px;
    margin: 0 auto;
    margin-bottom: 2rem;
}

.footer-section h4 {
    font-family: 'Space Mono', monospace;
    font-size: 0.875rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    color: var(--white-100);
}

.footer-section ul {
    list-style: none;
}

.footer-section a {
    color: var(--white-80);
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.3s ease;
    display: block;
    margin-bottom: 0.75rem;
}

.footer-section a:hover {
    color: var(--white-100);
}

.footer-bottom {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid var(--white-15);
    color: var(--white-60);
    font-size: 0.875rem;
    max-width: 1400px;
    margin: 0 auto;
}

/* ===== ANIMATIONS ===== */
@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-60px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(60px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeInRight {
    from {
        opacity: 0;
        transform: translateX(40px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes bounce {
    0%, 100% {
        transform: translateX(-50%) translateY(0);
    }
    50% {
        transform: translateX(-50%) translateY(15px);
    }
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .nav-menu {
        gap: 1.5rem;
    }

    .nav-menu a {
        font-size: 0.75rem;
    }

    .hero {
        flex-direction: column;
        text-align: center;
        padding: 2rem;
    }

    .hero-content {
        max-width: 100%;
        margin-bottom: 3rem;
    }

    .hero-cta-group {
        justify-content: center;
    }

    .hero-image {
        min-height: 300px;
    }

    section {
        padding: 3rem 1.5rem;
    }

    .nav-container {
        padding: 0 1.5rem;
    }
}
"""

# ===== HOME PAGE =====
@app.get("/", response_class=HTMLResponse)
def get_home():
    """Página principal - Inspired by SpaceX"""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skynet - La Resistencia de Venezuela</title>
        <style>
            {CSS_SPACEX}
        </style>
    </head>
    <body>
        <!-- NAVBAR -->
        <nav class="navbar">
            <div class="nav-container">
                <div class="logo">🚀 SKYNET</div>
                <ul class="nav-menu">
                    <li><a href="#home">Inicio</a></li>
                    <li><a href="#resistencia">Resistencia</a></li>
                    <li><a href="#donaciones">Donaciones</a></li>
                    <li><a href="#luz">Luz</a></li>
                    <li><a href="/registro">Acceso</a></li>
                </ul>
            </div>
        </nav>

        <!-- HERO SECTION -->
        <section id="home" class="hero">
            <div class="hero-content">
                <h1 class="hero-title">La Resistencia</h1>
                <p class="hero-subtitle">Plataforma de coordinación descentralizada para la liberación de Venezuela. Transparencia, seguridad y acción coordinada.</p>
                <div class="hero-cta-group">
                    <a href="/registro" class="btn btn-primary">Únete Ahora</a>
                    <a href="#resistencia" class="btn">Conoce Más</a>
                </div>
            </div>
            <div class="hero-image">
                <div class="hero-visual">🌐</div>
            </div>
            <div class="scroll-indicator">
                <span>Scroll</span>
                <div class="scroll-arrow"></div>
            </div>
        </section>

        <!-- RESISTENCIA SECTION -->
        <section id="resistencia" class="resistencia">
            <div class="container">
                <div class="section-header">
                    <h2>Sobre La Resistencia</h2>
                    <p>Pilares fundamentales de Skynet</p>
                </div>
                <div class="resistencia-grid">
                    <div class="resistencia-card">
                        <div class="card-icon">🔒</div>
                        <h3>Encriptación Total</h3>
                        <p>Tus datos están protegidos con los más altos estándares de seguridad. Privacidad garantizada.</p>
                    </div>
                    <div class="resistencia-card">
                        <div class="card-icon">⛓️</div>
                        <h3>Blockchain</h3>
                        <p>Transparencia verificable en cada transacción. Auditoría pública e inmutable.</p>
                    </div>
                    <div class="resistencia-card">
                        <div class="card-icon">🤝</div>
                        <h3>Comunidad</h3>
                        <p>Miles de venezolanos coordinados. Red descentralizada de resistencia activa.</p>
                    </div>
                    <div class="resistencia-card">
                        <div class="card-icon">💡</div>
                        <h3>Innovación</h3>
                        <p>Herramientas tecnológicas avanzadas para la liberación. Desarrollo continuo.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- DONACIONES SECTION -->
        <section id="donaciones" class="donaciones">
            <div class="container">
                <div class="section-header">
                    <h2>Dona Por La Libertad</h2>
                    <p>Tu contribución financia operaciones de resistencia</p>
                </div>
                <div class="donaciones-grid">
                    <div class="donacion-card">
                        <div class="donacion-icon">💳</div>
                        <h3>Tarjeta de Crédito</h3>
                        <p>Stripe - Seguro y rápido</p>
                        <a href="#" class="btn">Donar</a>
                    </div>
                    <div class="donacion-card">
                        <div class="donacion-icon">₿</div>
                        <h3>Bitcoin</h3>
                        <p>Privacidad y seguridad</p>
                        <a href="#" class="btn">Donar</a>
                    </div>
                    <div class="donacion-card">
                        <div class="donacion-icon">💰</div>
                        <h3>Binance</h3>
                        <p>Cripto directo</p>
                        <a href="#" class="btn">Donar</a>
                    </div>
                    <div class="donacion-card">
                        <div class="donacion-icon">📱</div>
                        <h3>Pago Móvil</h3>
                        <p>Para usuarios en Venezuela</p>
                        <a href="#" class="btn">Donar</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- LUZ SECTION -->
        <section id="luz" class="luz-crypto">
            <div class="container">
                <div class="section-header">
                    <h2>Cripto LUZ</h2>
                    <p>La moneda de la libertad - 20 millones de unidades</p>
                </div>
                <div class="luz-info">
                    <div class="luz-stats">
                        <div class="stat-box">
                            <span class="stat-number">20M</span>
                            <span class="stat-label">Suministro Total</span>
                        </div>
                        <div class="stat-box">
                            <span class="stat-number">\$0.10</span>
                            <span class="stat-label">Precio Actual</span>
                        </div>
                        <div class="stat-box">
                            <span class="stat-number">100%</span>
                            <span class="stat-label">Transparencia</span>
                        </div>
                    </div>
                    <div class="luz-description">
                        <p>LUZ es una criptomoneda diseñada para financiar la resistencia. Cada transacción es verificable en blockchain y totalmente transparente.</p>
                    </div>
                    <div class="luz-cta">
                        <a href="#" class="btn btn-primary">Compra LUZ</a>
                        <a href="#" class="btn">Whitepaper</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- FOOTER -->
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Skynet</h4>
                    <p style="color:var(--white-80); font-size:0.9rem;">La plataforma de la resistencia venezolana</p>
                </div>
                <div class="footer-section">
                    <h4>Enlaces</h4>
                    <ul>
                        <li><a href="#resistencia">Resistencia</a></li>
                        <li><a href="#donaciones">Donaciones</a></li>
                        <li><a href="#luz">Cripto LUZ</a></li>
                        <li><a href="/health">Status API</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Contacto</h4>
                    <ul>
                        <li><a href="https://t.me/rogerhernandzzz" target="_blank">Telegram</a></li>
                        <li><a href="#">Email</a></li>
                        <li><a href="#">WhatsApp</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Recursos</h4>
                    <ul>
                        <li><a href="#">Documentación</a></li>
                        <li><a href="#">GitHub</a></li>
                        <li><a href="/health">API Status</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Skynet - La Resistencia. Todos los derechos reservados.</p>
            </div>
        </footer>
    </body>
    </html>
    """

@app.get("/registro", response_class=HTMLResponse)
def get_registro():
    """Página de registro"""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skynet - Registro</title>
        <style>
            {CSS_SPACEX}

            .registro-wrapper {{
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 2rem;
                margin-top: 60px;
            }}

            .registro-card {{
                background: rgba(255, 255, 255, 0.02);
                border: 1px solid var(--white-15);
                padding: 3rem;
                max-width: 450px;
                width: 100%;
                backdrop-filter: blur(10px);
                animation: fadeInUp 0.8s ease-out;
            }}

            .registro-card h1 {{
                font-family: 'Syne', sans-serif;
                font-size: 1.75rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 0.5rem;
            }}

            .registro-subtitle {{
                text-align: center;
                color: var(--white-80);
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
                border: 1px solid var(--white-15);
                color: var(--white-100);
                font-size: 0.9rem;
                transition: all 0.3s ease;
            }}

            .form-group input:focus {{
                outline: none;
                border-color: var(--white-100);
                background: rgba(255, 255, 255, 0.05);
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
                background: var(--white-80);
            }}

            .back-link {{
                text-align: center;
                margin-top: 1.5rem;
            }}

            .back-link a {{
                color: var(--white-80);
                text-decoration: none;
                font-size: 0.875rem;
            }}

            .back-link a:hover {{
                color: var(--white-100);
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
                    <a href="/">← Volver al inicio</a>
                </div>
            </div>
        </div>

        <script>
            function handleSubmit(event) {{
                event.preventDefault();
                alert('✅ Registro exitoso - Bienvenido a la resistencia');
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
    return {"success": True, "message": "Registro completado", "user": {"username": username, "email": email}}

@app.post("/api/auth/login")
def login(email: str, password: str):
    return {"success": True, "message": "Login exitoso", "token": "jwt_token"}

@app.get("/api/news")
def get_news():
    return {"news": [{"id": 1, "title": "Skynet está LIVE", "created_at": datetime.now().isoformat()}]}

@app.get("/api/donations/stats")
def get_donation_stats():
    return {"total_donations": 0, "total_amount": 0, "currency": "USD"}

@app.get("/api/crypto/luz")
def get_luz_info():
    return {"name": "Luz", "symbol": "LUZ", "total_supply": 20000000, "current_price": 0.10}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
