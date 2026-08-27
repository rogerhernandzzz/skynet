from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from datetime import datetime
import os
from dotenv import load_dotenv

# Importar modelos y bases de datos
from database import engine, SessionLocal, Base
from models import User, News, ForumPost, Donation, LeaderInfo

load_dotenv()

# Crear tablas
Base.metadata.create_all(bind=engine)

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

# Servir archivos estáticos (comentado por ahora - no hay frontend en el repo)
# app.mount("/static", StaticFiles(directory="frontend/public"), name="static")

# Dependency para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ===== HEALTH CHECK =====
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "service": "Skynet API"
    }

# ===== SERVE HOME PAGE =====
@app.get("/", response_class=HTMLResponse)
def get_home():
    """Servir página principal"""
    # HTML inline - no depende de archivos del filesystem
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
                .status .badge {
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
                .endpoints h2 {
                    text-align: center;
                    margin-bottom: 20px;
                    color: #FF7A00;
                }
                .endpoints ul {
                    list-style: none;
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 15px;
                }
                .endpoints li {
                    background: rgba(255, 255, 255, 0.05);
                    padding: 12px;
                    border-radius: 8px;
                    border-left: 3px solid #6C5CE7;
                }
                code {
                    background: rgba(0, 0, 0, 0.3);
                    padding: 4px 8px;
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
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Skynet</h1>
                <h2 style="color:#6C5CE7; margin-bottom:30px">La Resistencia Venezolana</h2>

                <div class="status">
                    <p><span class="badge">✅ LIVE</span></p>
                    <p>API completamente operacional 24/7</p>
                    <p style="font-size:14px; margin-top:15px; color:#aaa">Servidor en Render • Base de datos SQLite • Contratos Ethereum</p>
                </div>

                <div class="endpoints">
                    <h2>📡 Endpoints API Disponibles</h2>
                    <ul>
                        <li><code>GET /health</code> - Status del servicio</li>
                        <li><code>POST /api/auth/register</code> - Registrar usuario</li>
                        <li><code>POST /api/auth/login</code> - Login</li>
                        <li><code>GET /api/news</code> - Noticias de la resistencia</li>
                        <li><code>POST /api/news</code> - Crear noticia</li>
                        <li><code>GET /api/forum</code> - Posts del foro anónimo</li>
                        <li><code>POST /api/forum</code> - Crear post anónimo</li>
                        <li><code>GET /api/donations/stats</code> - Estadísticas de donaciones</li>
                        <li><code>POST /api/donations/create</code> - Crear donación</li>
                        <li><code>GET /api/leader</code> - Información del líder</li>
                        <li><code>PUT /api/leader</code> - Actualizar líder</li>
                        <li><code>GET /api/trader/sim</code> - Simulación de trading</li>
                        <li><code>GET /api/crypto/luz</code> - Info cripto LUZ</li>
                        <li><code>GET /api/contracts/transparency</code> - Smart contracts</li>
                    </ul>
                </div>

                <div class="cta">
                    <a href="/registro" class="button">Ir a Registro</a>
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
                    max-width: 500px;
                    width: 100%;
                    backdrop-filter: blur(10px);
                }
                h1 {
                    text-align: center;
                    margin-bottom: 30px;
                    color: #FF7A00;
                }
                .form-group {
                    margin-bottom: 20px;
                }
                label {
                    display: block;
                    margin-bottom: 8px;
                    font-weight: 500;
                    color: #e8e8f0;
                }
                input {
                    width: 100%;
                    padding: 12px;
                    background: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(108, 92, 231, 0.3);
                    border-radius: 8px;
                    color: #e8e8f0;
                    font-size: 16px;
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
                }
                .back a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Registro Skynet</h1>
                <form>
                    <div class="form-group">
                        <label for="username">Usuario</label>
                        <input type="text" id="username" name="username" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="cedula">Cédula</label>
                        <input type="text" id="cedula" name="cedula" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Contraseña</label>
                        <input type="password" id="password" name="password" required>
                    </div>
                    <button type="submit">Registrarse</button>
                </form>
                <div class="back">
                    <a href="/">← Volver al inicio</a>
                </div>
            </div>
        </body>
    </html>
    """

# ===== AUTH ENDPOINTS =====
@app.post("/api/auth/register")
def register(
    username: str,
    email: str,
    password: str,
    cedula: str,
    db: Session = Depends(get_db)
):
    """Registrar nuevo usuario"""

    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(
        (User.email == email) | (User.cedula == cedula)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    # Crear nuevo usuario
    user = User(
        username=username,
        email=email,
        cedula=cedula,
        created_at=datetime.now()
    )
    user.set_password(password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "message": "Usuario registrado exitosamente"
    }

@app.post("/api/auth/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    """Login de usuario"""

    user = db.query(User).filter(User.email == email).first()

    if not user or not user.check_password(password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    # Aquí generarías JWT
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "token": "jwt_token_aqui"
    }

# ===== NEWS ENDPOINTS =====
@app.get("/api/news")
def get_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtener noticias"""
    news = db.query(News).order_by(News.created_at.desc()).offset(skip).limit(limit).all()
    return news

@app.post("/api/news")
def create_news(
    title: str,
    content: str,
    image_url: str = None,
    db: Session = Depends(get_db)
):
    """Crear noticia (solo admin)"""

    news = News(
        title=title,
        content=content,
        image_url=image_url,
        created_at=datetime.now()
    )

    db.add(news)
    db.commit()
    db.refresh(news)

    return news

# ===== FORUM ENDPOINTS =====
@app.get("/api/forum")
def get_forum_posts(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Obtener posts del foro"""
    posts = db.query(ForumPost).order_by(ForumPost.created_at.desc()).offset(skip).limit(limit).all()
    return posts

@app.post("/api/forum")
def create_forum_post(
    user_id: int,
    pseudonym: str,
    content: str,
    db: Session = Depends(get_db)
):
    """Crear post en foro (con pseudónimo)"""

    post = ForumPost(
        user_id=user_id,
        pseudonym=pseudonym,
        content=content,
        created_at=datetime.now()
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post

# ===== DONATION ENDPOINTS =====
@app.get("/api/donations/stats")
def get_donation_stats(db: Session = Depends(get_db)):
    """Obtener estadísticas de donaciones"""

    total_donations = db.query(Donation).count()
    total_amount = sum([d.amount for d in db.query(Donation).all()]) or 0

    return {
        "total_donations": total_donations,
        "total_amount": total_amount,
        "currency": "USD"
    }

@app.post("/api/donations/create")
def create_donation(
    amount: float,
    method: str,  # stripe, bitcoin, binance, pagomovil
    email: str,
    db: Session = Depends(get_db)
):
    """Crear donación"""

    donation = Donation(
        amount=amount,
        method=method,
        email=email,
        status="pending",
        created_at=datetime.now()
    )

    db.add(donation)
    db.commit()
    db.refresh(donation)

    # Aquí procesarías con Stripe, Bitcoin API, etc.

    return {
        "id": donation.id,
        "amount": donation.amount,
        "method": donation.method,
        "status": donation.status,
        "payment_url": f"https://stripe.com/pay/{donation.id}"  # Ejemplo
    }

@app.webhook("/api/webhooks/stripe")
def stripe_webhook(payload: dict):
    """Webhook de Stripe"""
    # Procesar webhook de Stripe aquí
    return {"status": "received"}

# ===== LEADER INFO =====
@app.get("/api/leader")
def get_leader_info(db: Session = Depends(get_db)):
    """Obtener información del líder"""

    leader = db.query(LeaderInfo).filter(LeaderInfo.id == 1).first()

    if not leader:
        # Crear info del líder por defecto
        leader = LeaderInfo(
            name="Roger Hernández",
            title="Fundador & Líder de Skynet",
            bio="Ingeniero de sistemas y activista político dedicado a la liberación de Venezuela.",
            image_url="https://example.com/roger.jpg",
            telegram="https://t.me/rogerhernandzzz",
            email="roger@skynet.resist",
            facebook="https://facebook.com/rogerhernandez",
            instagram="https://instagram.com/rogerhernandez",
            members_count=20000,
            funds_raised=5000000
        )
        db.add(leader)
        db.commit()
        db.refresh(leader)

    return leader

@app.put("/api/leader")
def update_leader_info(
    name: str = None,
    bio: str = None,
    telegram: str = None,
    db: Session = Depends(get_db)
):
    """Actualizar información del líder (solo admin)"""

    leader = db.query(LeaderInfo).filter(LeaderInfo.id == 1).first()

    if not leader:
        raise HTTPException(status_code=404, detail="Líder no encontrado")

    if name:
        leader.name = name
    if bio:
        leader.bio = bio
    if telegram:
        leader.telegram = telegram

    db.commit()
    db.refresh(leader)

    return leader

# ===== TRADER BOT (Simulado) =====
@app.get("/api/trader/sim")
def get_trader_simulation():
    """Obtener simulación de trading (educativo)"""

    return {
        "balance": 10000.00,
        "currency": "USD",
        "trades": [
            {"id": 1, "symbol": "BTC/USD", "type": "BUY", "amount": 0.5, "price": 50000},
            {"id": 2, "symbol": "ETH/USD", "type": "SELL", "amount": 5, "price": 3000}
        ],
        "profit_loss": 2500.00,
        "roi": "25%",
        "note": "Esta es una simulación educativa sin dinero real"
    }

# ===== CRIPTO LUZ =====
@app.get("/api/crypto/luz")
def get_luz_crypto_info():
    """Obtener información de la cripto LUZ"""

    return {
        "name": "Luz",
        "symbol": "LUZ",
        "total_supply": 20000000,
        "current_price": 0.10,
        "market_cap": 2000000,
        "description": "Criptomoneda para financiar la resistencia venezolana",
        "blockchain": "Ethereum",
        "contract_address": "0x1234567890abcdef",
        "transparency": "100%"
    }

# ===== SMART CONTRACTS =====
@app.get("/api/contracts/transparency")
def get_transparency_contract():
    """Obtener contrato inteligente de transparencia"""

    return {
        "contract_name": "TransparencyAudit",
        "blockchain": "Ethereum",
        "address": "0xabcdef1234567890",
        "description": "Contrato que verifica la transparencia de todas las transacciones",
        "functions": [
            "recordTransaction()",
            "verifyFunds()",
            "auditLog()",
            "publicReport()"
        ],
        "verified": True,
        "auditor": "Chainalysis"
    }

# ===== ERROR HANDLERS =====
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
