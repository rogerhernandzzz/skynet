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

# CORS - Permitir todos los orígenes
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

# ===== SERVE HOME PAGE =====
@app.get("/", response_class=HTMLResponse)
def get_home():
    """Servir página principal"""
    return """
    <html>
        <head>
            <title>Skynet - La Resistencia Venezolana</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 100%);
                    color: #e8e8f0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    min-height: 100vh;
                    padding: 40px 20px;
                }
                .container {
                    max-width: 900px;
                    margin: 0 auto;
                    text-align: center;
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 20px;
                    background: linear-gradient(135deg, #6C5CE7 0%, #FF7A00 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                }
                h2 {
                    color: #6C5CE7;
                    margin-bottom: 30px;
                }
                .status {
                    background: rgba(108, 92, 231, 0.1);
                    border: 1px solid #6C5CE7;
                    border-radius: 10px;
                    padding: 20px;
                    margin: 30px 0;
                }
                .status p {
                    font-size: 18px;
                    margin: 10px 0;
                }
                .badge {
                    display: inline-block;
                    background: #6C5CE7;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 20px;
                    font-weight: bold;
                    margin: 5px;
                }
                .endpoints {
                    background: rgba(18, 18, 26, 0.5);
                    border: 1px solid rgba(108, 92, 231, 0.3);
                    border-radius: 12px;
                    padding: 30px;
                    margin: 30px 0;
                    text-align: left;
                }
                .endpoints h3 {
                    text-align: center;
                    margin-bottom: 20px;
                    color: #FF7A00;
                }
                .endpoints ul {
                    list-style: none;
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 15px;
                }
                .endpoints li {
                    background: rgba(255, 255, 255, 0.05);
                    padding: 12px;
                    border-radius: 8px;
                    border-left: 3px solid #6C5CE7;
                    text-align: left;
                    font-size: 14px;
                }
                code {
                    background: rgba(0, 0, 0, 0.3);
                    padding: 2px 6px;
                    border-radius: 4px;
                    color: #FF7A00;
                    font-weight: bold;
                }
                .cta {
                    margin-top: 40px;
                }
                .button {
                    display: inline-block;
                    background: linear-gradient(135deg, #6C5CE7 0%, #FF7A00 100%);
                    color: white;
                    padding: 12px 30px;
                    border-radius: 25px;
                    text-decoration: none;
                    font-weight: bold;
                    margin: 10px;
                    transition: transform 0.3s;
                }
                .button:hover {
                    transform: scale(1.05);
                }
                .info {
                    font-size: 12px;
                    color: #999;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Skynet</h1>
                <h2>La Resistencia Venezolana</h2>

                <div class="status">
                    <p><span class="badge">✅ LIVE</span></p>
                    <p style="font-size:16px; margin:15px 0">API completamente operacional 24/7</p>
                    <p style="font-size:13px; color:#aaa">Servidor en Render • SQLite • Blockchain</p>
                </div>

                <div class="endpoints">
                    <h3>📡 Endpoints API</h3>
                    <ul>
                        <li><code>GET /health</code> - Estado del servicio</li>
                        <li><code>GET /</code> - Esta página</li>
                        <li><code>POST /api/auth/register</code> - Registrarse</li>
                        <li><code>POST /api/auth/login</code> - Iniciar sesión</li>
                        <li><code>GET /api/news</code> - Noticias</li>
                        <li><code>POST /api/news</code> - Publicar noticia</li>
                        <li><code>GET /api/forum</code> - Foro anónimo</li>
                        <li><code>POST /api/forum</code> - Crear post</li>
                        <li><code>GET /api/donations/stats</code> - Donaciones</li>
                        <li><code>POST /api/donations/create</code> - Donar</li>
                        <li><code>GET /api/leader</code> - Líder</li>
                        <li><code>PUT /api/leader</code> - Actualizar</li>
                        <li><code>GET /api/trader/sim</code> - Trading</li>
                        <li><code>GET /api/crypto/luz</code> - Cripto LUZ</li>
                        <li><code>GET /api/contracts/transparency</code> - Contratos</li>
                    </ul>
                </div>

                <div class="cta">
                    <a href="/registro" class="button">Ir a Registro</a>
                </div>

                <div class="info">
                    <p>Skynet v1.0 • 2026</p>
                </div>
            </div>
        </body>
    </html>
    """

@app.get("/registro", response_class=HTMLResponse)
def get_registro():
    """Servir página de registro"""
    return """
    <html>
        <head>
            <title>Skynet - Registro</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 100%);
                    color: #e8e8f0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 20px;
                }
                .container {
                    background: rgba(18, 18, 26, 0.8);
                    border: 1px solid rgba(108, 92, 231, 0.3);
                    border-radius: 12px;
                    padding: 40px;
                    max-width: 450px;
                    width: 100%;
                    backdrop-filter: blur(10px);
                }
                h1 {
                    text-align: center;
                    margin-bottom: 10px;
                    font-size: 28px;
                    background: linear-gradient(135deg, #6C5CE7 0%, #FF7A00 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                }
                .subtitle {
                    text-align: center;
                    color: #999;
                    margin-bottom: 30px;
                    font-size: 14px;
                }
                .form-group {
                    margin-bottom: 20px;
                }
                label {
                    display: block;
                    margin-bottom: 8px;
                    font-weight: 500;
                    color: #e8e8f0;
                    font-size: 14px;
                }
                input {
                    width: 100%;
                    padding: 12px;
                    background: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(108, 92, 231, 0.3);
                    border-radius: 8px;
                    color: #e8e8f0;
                    font-size: 14px;
                    transition: border-color 0.3s;
                }
                input:focus {
                    outline: none;
                    border-color: #6C5CE7;
                    box-shadow: 0 0 10px rgba(108, 92, 231, 0.3);
                }
                button {
                    width: 100%;
                    padding: 12px;
                    background: linear-gradient(135deg, #6C5CE7 0%, #FF7A00 100%);
                    color: white;
                    border: none;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 16px;
                    cursor: pointer;
                    transition: transform 0.3s;
                    margin-top: 10px;
                }
                button:hover {
                    transform: scale(1.02);
                }
                .back {
                    text-align: center;
                    margin-top: 20px;
                }
                .back a {
                    color: #6C5CE7;
                    text-decoration: none;
                    font-size: 14px;
                }
                .back a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Skynet</h1>
                <p class="subtitle">Registro de Usuario</p>

                <form onsubmit="return handleSubmit(event)">
                    <div class="form-group">
                        <label for="username">Usuario</label>
                        <input type="text" id="username" name="username" placeholder="Tu usuario" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" name="email" placeholder="tu@email.com" required>
                    </div>
                    <div class="form-group">
                        <label for="cedula">Cédula</label>
                        <input type="text" id="cedula" name="cedula" placeholder="V-12345678" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Contraseña</label>
                        <input type="password" id="password" name="password" placeholder="Min. 8 caracteres" required>
                    </div>
                    <button type="submit">Registrarse</button>
                </form>

                <div class="back">
                    <a href="/">← Volver al inicio</a>
                </div>
            </div>

            <script>
                function handleSubmit(event) {
                    event.preventDefault();
                    alert('Formulario de registro - Integración con API próximamente');
                    return false;
                }
            </script>
        </body>
    </html>
    """

# ===== API ENDPOINTS BÁSICOS =====
@app.post("/api/auth/register")
def register(username: str, email: str, password: str, cedula: str):
    """Registrar nuevo usuario"""
    return {
        "success": True,
        "message": "Registro completado",
        "user": {
            "username": username,
            "email": email,
            "cedula": cedula
        }
    }

@app.post("/api/auth/login")
def login(email: str, password: str):
    """Login de usuario"""
    return {
        "success": True,
        "message": "Login exitoso",
        "token": "jwt_token_aqui"
    }

@app.get("/api/news")
def get_news(skip: int = 0, limit: int = 10):
    """Obtener noticias"""
    return {
        "news": [
            {
                "id": 1,
                "title": "Skynet está LIVE",
                "content": "La plataforma de la resistencia está operacional",
                "created_at": datetime.now().isoformat()
            }
        ]
    }

@app.post("/api/news")
def create_news(title: str, content: str):
    """Crear noticia"""
    return {
        "success": True,
        "news": {"title": title, "content": content}
    }

@app.get("/api/forum")
def get_forum(skip: int = 0, limit: int = 20):
    """Obtener posts del foro"""
    return {"posts": []}

@app.post("/api/forum")
def create_forum_post(pseudonym: str, content: str):
    """Crear post anónimo"""
    return {"success": True, "post": {"pseudonym": pseudonym, "content": content}}

@app.get("/api/donations/stats")
def get_donation_stats():
    """Estadísticas de donaciones"""
    return {
        "total_donations": 0,
        "total_amount": 0,
        "currency": "USD"
    }

@app.post("/api/donations/create")
def create_donation(amount: float, method: str, email: str):
    """Crear donación"""
    return {
        "success": True,
        "donation": {
            "amount": amount,
            "method": method,
            "status": "pending"
        }
    }

@app.get("/api/leader")
def get_leader():
    """Obtener información del líder"""
    return {
        "name": "Roger Hernández",
        "title": "Fundador & Líder de Skynet",
        "bio": "Ingeniero de sistemas dedicado a la liberación de Venezuela",
        "members_count": 20000,
        "funds_raised": 5000000
    }

@app.get("/api/trader/sim")
def get_trader_sim():
    """Simulación de trading"""
    return {
        "balance": 10000.00,
        "currency": "USD",
        "profit_loss": 2500.00,
        "roi": "25%"
    }

@app.get("/api/crypto/luz")
def get_luz_info():
    """Información de cripto LUZ"""
    return {
        "name": "Luz",
        "symbol": "LUZ",
        "total_supply": 20000000,
        "current_price": 0.10,
        "market_cap": 2000000
    }

@app.get("/api/contracts/transparency")
def get_contracts():
    """Smart contracts"""
    return {
        "contract_name": "TransparencyAudit",
        "blockchain": "Ethereum",
        "verified": True
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
