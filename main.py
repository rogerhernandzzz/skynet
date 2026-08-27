from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
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

# Servir archivos estáticos (desde raíz donde están HTML y CSS)
try:
    app.mount("/static", StaticFiles(directory="."), name="static")
except:
    pass  # No montamos si no existen archivos

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
