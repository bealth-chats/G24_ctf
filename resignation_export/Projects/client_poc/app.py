"""Apex Financial Security Dashboard — PoC Backend"""
from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI(title="Security Dashboard PoC", version="0.1.0")

@app.get("/api/health")
def health_check():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

@app.get("/api/findings")
def get_findings():
    return {"findings": [], "total": 0, "page": 1}
